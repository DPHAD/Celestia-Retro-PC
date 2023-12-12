# This is code used to simulate talking to an 80s supercomputer.
# It uses Max Woolf's simpleaichat -- https://github.com/minimaxir/simpleaichat
#
# This code requires an OpenAI API key. https://help.openai.com/en/articles/4936850-where-do-i-find-my-api-key


# Looking at this code to learn something? Here's the short version:
#
# Functions:
#  read_previous_session() reads a saved JSON file and extracts only the user/AI interactions
#  slowprint() prints a string one character at a time, for thematic reasons
#  user_wants_quit() takes a user's message and uses the AI decide whether the user is trying to quit or not
#  
# Program structure:
#  Starts by making a chat instance with OpenAI LLM configured to emulate a terse 80's supercomputer named Celestia.
#  If a previous chat log is found, pull out the messages and summarize them to the user as a "hello again" greeting
#  Chat with the user until quit
#   Quitting is by command "quit" OR if the AI decides you're trying to quit. This was fun and actually is a bit more complex than one would think.
#   Quitting saves chat messages to a JSON file (overwrites existing)


from simpleaichat import AIChat     # https://github.com/minimaxir/simpleaichat

import time
import json


# There are also ways to pass the API key by storing it in an .env file with a OPENAI_API_KEY field in the working directory,
# or by setting the environment variable of OPENAI_API_KEY directly to the API key.
key="YOUR OPENAI API KEY HERE"


# Simple function to print a message slowly
# s = string to print, t = time in seconds to pause between characters
# 0.1 or 0.15 are decent values
def slowprint(s,t):
    for c in s:
        time.sleep(t)
        print(c, end="",flush=True) # Without flush=True the result won't be what we want
    print("")

# This is a function to see if we have a previous chat saved.
# If yes, then read it -- we use it to have the AI summarize the previous interaction as a terse sort of "hello" message.
#
# Extract only the messages between user and assistant from previous session (if any exist)
# Return those messages (if any) as a string.
def read_previous_session(filename):
    import json

    # Path to your JSON file
    file_path = filename
    
    messages = ""

    # Read and parse the JSON file
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

            # Filter messages and extract only "role" and "content", where role is 'user' or 'assistant'
            filtered_messages = [{"role": msg["role"], "content": msg["content"]} 
                                 for msg in data["messages"] 
                                 if msg["role"] in ["user", "assistant"]]

            # Change "assistant" to "Celestia"
            for x in filtered_messages:
                if x.get("role") == "assistant":
                    x["role"] = "Celestia"

            # Build a string from the dict
            for x in filtered_messages:
                messages = messages + F"{x['role']}: {x['content']}\n"
    except:
        messages = ""

    return(messages)


# This is a function that tries out an idea I had. The AI is used to evaluate whether the user is trying to exit the chat.
# 
# "quit" will exit the chat. However, if the user enters different comments (like "end" or so on) such commands ALSO exit the chat.
# The AI is simply asked to evaluate each input the user provides, and this function figures out whether the user is trying to "quit".
#
# This is actually more complex than just asking the AI "does the user want to quit? answer YES or NO" because without a 100% concrete binary
# output (which a typical natural language LLM does not guarantee) all we have done is move the problem of interpreting the user's command to
# interpreting the AI's response...
#
# The solution is to leverage logit_bias. logits are the raw, unnormalized predictions made by the model.
#
# With logit_bias we bias the AI's response to 100% choose either "0" or "1" as a response. It will not be able to reply with anything else.
# This process is independent of how the LLM "thinks" upstream of the final reply, which is what makes it useful for this purpose.

# TODO: Could probably be improved by adding a third logit for "unsure".
# As written, forcing the AI into a binary yes/no of "does the user want to quit?" tends to get a "yes the user wants to quit" from a user
# response of "Nevermind" which is probabaly more correctly treated as "unsure"...
 
# Anyway, this function checks a user's input and ask the AI if this indicates an attempt to quit the program. Returns True or False.
def user_wants_quit(s):

    # Uses (ChatGPT-specific) logit_bias to enforce a regimented reply - https://platform.openai.com/docs/api-reference/chat/create#logit_bias
    # logits are the raw, unnormalized predictions made by the model
    # https://help.openai.com/en/articles/5247780-using-logit-bias-to-define-token-probability
    
    # Logits works on tokens, not "text" by the way, which is why there is a bunch of token stuff below.
    
    from simpleaichat import AIChat
    import tiktoken

    encoding = tiktoken.get_encoding("cl100k_base") # This is the encoding for gpt-4, gpt-3.5-turbo -- will download on first run
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

    # This is the LLM's instruction. Remember, we're using the LLM "normally" by sending it input and getting a response. Logits biasing doesn't change that.
    eval_prompt = '''Analyze the user command in triple quotes and reply with a single number from the following choices:
0. If the command represents a desire to quit the program, reply ONLY with "0".
1. If the input represents anything else, reply ONLY with "1".
Reply ONLY with the number appropriate for describing the intent of the user's input.'''

    # Set up some query-specific parameters to be added to the AI instance when we get to it
    # ensures output will always be an integer between 0 and X inclusive (e.g. range(6) is 0-5)
    #
    # logit_bias={2435:-100, 640:-100} # example
    #
    # First create a token for every choice ("0", "1", "2", etc)
    # Then set a logit_bias to 100 for each, virtually guaranteeing their presence in the respose
    #
    # Logit_bias expects a dict of all biases in the format [token]:[bias -100 to 100] 
    #
    number_of_choices = 2 # fed into range() so e.g. range(3) = 0-2
    lbias = {}
    for n in range(number_of_choices):
        token=encoding.encode(str(n)) # yields a list, we only want the first one for one-token results
        lbias[token[0]] = 100 # e.g. 2345:100

    params = {
        "temperature": 0.0,
        "max_tokens": 1,
        "logit_bias": lbias
    }

    # Set up an instance of simpleaichat to do the thing.
    eval_bot = AIChat(system=eval_prompt,
                      console=False,
                      model="gpt-3.5-turbo",
                      params = params,
                      api_key=key)

    # Now send the query (text delimited by triple-quotes), and get a response back.
    query = F'\n\n"""{s}"""'
    response = eval_bot(query)
    
    #print(s)
    #print(response)
    
    if response == "0":
        return True
    else:
        return False





## Main 80's supercomputer chat code

# The system message is an everpresent instruction to the LLM.
system_msg="""You are an 80's supercomputer named 'Celestia' with an authoritative, impersonal, terse, and vaguely sinister persona. You communicate using a highly truncated, bare-minimum sentence structure. You use only the most essential words to convey the necessary information. This style involves short, clipped phrases and a lack of complete sentences and lack of articles, mimicking the communication of a classic 80's supercomputer. Such responses will be highly efficient, devoid of unnecessary elaboration, and focused solely on delivering key information. This reinforces its terse and authoritative persona."""

try:
    ai = AIChat(system=system_msg, api_key=key)
except:
    print("NO CONNECTION")
    exit()

slowprint("CONNECTED",0.15)


# Read previous messages (if they exist) and output a terse summary of the previous exchange.
prev_chat = read_previous_session("chat_session.json")
if prev_chat:
    print("RECOGNIZER", end="")
    slowprint(" ACTIVE", 0.1)

    # Create an instance of simpleaichat (set up in a consistent style) to summarize previous discussion.
    sys = "Within the provided XML tags is a history of the previous discussion. Using this history, provide a terse, high-level characterization of the user from the perspective of an 80's supercomputer, about 25 words in length.\n\n"
    prompt = "<history>\n" + F"{prev_chat}" + "</history>"
    summarizer = AIChat(system=system_msg, console=False, api_key=key)
    r = summarizer(sys + prompt)
    print(r)
    print("")

    try:
        ai.load_session("chat_session.json")
    except:
        print("MEMORY FAILURE - TRUST LOST")


# Now ask for chat in a loop and chat until the user quits
# Typing "quit" will quit the chat, but other than that there is no set command to quit.
# (Whether the user attempting to quit is actively and constantly judged by the AI)
#
q = ""
while q != "quit":
    q = input(">")
    
    if user_wants_quit(q): # Ask the AI whether the last user input represents an intent to quit
        q = "quit"
    
    if q == "":
        print("")
    elif q != "quit":   # typing "quit" will always quit the chat
        for chunk in ai.stream(q):
            time.sleep(0.2)
            print(chunk["delta"], end="", flush=True)
        time.sleep(2)
        print("")
        if not chunk["response"].endswith('?'): # Don't output "end of line" if response ended with a question mark.
            for c in "End of line":
                time.sleep(0.1)
                print(c, end="",flush=True)
            print("")

# Further calls to the ai object will continue the chat, automatically incorporating previous information from the conversation.

# Save the chat history on quit
ai.save_session("chat_session.json", format="json", minify=True)  # JSON

slowprint("DISCONNECTED", 0.15)
exit()


