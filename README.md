<img src="https://github.com/DPHAD/Celestia-Retro-PC/assets/28654887/75a2acb6-9124-4564-93f9-c229a80a8da7" height=320><img src="https://github.com/DPHAD/Celestia-Retro-PC/assets/28654887/144b4d59-ff8d-47ed-b714-08328db7f169" height=320>

# Celestia DIY Retro PC
The **Celestia** is a retro styled, one-piece PC using a **Raspberry Pi** (Pi400 or SBC + Official Pi keyboard). Currently designed around the [**Elecrow CrowVision 11.6"**](https://www.elecrow.com/wiki/index.php?title=CrowVision_11.6%27%27_Capacitive_Touch_Screen_Portable_HD_1366*768_IPS_LCD_Display) display, which is the only display that really matched what I was going for. As a bonus, it integrates a touchscreen, meaning a mouse is not necessary and helps preserve the one-piece aesthetic!

## What is it?
This is a 3D printable enclosure (a bit of a work in progress) that accommodates a display (11.6" Elecrow CrowVision display with touchscreen) and a Raspberry Pi, although any SBC would work. This design is highly flexible about the Pi in particular. 

One can mount any of the single-board computers to the back of the display, or one can simply use a Raspberry Pi 400 (a combo keyboard and computer.) 

Ports on the back allows integrating a single power jack and a small USB hub for convenience.

The result is a one-piece system with some real retro aesthetics; exactly what I wanted ever since coming across the Callisto-2 project (see below). 

## A few words about the keyboard
The keyboard is either the Raspberry Pi 400, or the official Raspberry Pi USB Keyboard. Both have (almost!) the same dimensions. (The official Pi keyboard will sit about 1mm higher at the front than the Pi400, but they both "fit".) Both allow full access to the ports on the back. Both have a matte white finish that blends well if the case is printed in matte white PLA. [Check out this image for a fuller understanding](https://github.com/DPHAD/Celestia-Retro-PC/assets/28654887/1cfccf38-2211-4b9c-8e7b-8b4d5b4fb883).

## Inspiration
I was always very inspired by the Callisto-2 project, but I wanted a bigger screen. I wasn't satisfied by any of the existing thin or light HDMI displays; the big ones always had bezel designs that made them awkward to integrate into DIY cases, and/or connectors in awkward positions. The Elecrow CrowVision display solved both problems, and had a touchscreen integrated, to boot!

The Callisto-2: https://www.printables.com/model/65887-callisto-2-fully-printable-retro-computer

Callisto-2's siblings: https://www.solarhardwarecomputers.com/

## Cool Retro Terminal
Completing the look is the Cool Retro Term software. I adjusted the taskbar at the top of the Raspberry Pi desktop to auto-hide, and run cool-retro-term in fullscreen mode. Right-click while it's running to access more configuration (I think it looks best on this display by removing screen curvature and eliminating margin.) The only downside is it runs slowly on a Raspberry Pi 4, but it's worth it.
https://snapcraft.io/install/cool-retro-term/raspbian

Launching Max Woolf's [simpleaichat](https://github.com/minimaxir/simpleaichat#simpleaichat) to create an 80s AI to interact with via the retro terminal is [the icing on the cake](https://github.com/DPHAD/Celestia-Retro-PC/assets/28654887/9ee3ed6e-96f8-408c-9d77-863f1e0091e9).

## Sample AI Chat Code
My code for making the chat work is provided, it is commented in a way that I hope will help people make sense of what goes into something like this. It requires Max Woolf's [simpleaichat](https://github.com/minimaxir/simpleaichat#simpleaichat) and it also requires an OpenAI API key (because that's what simpleaichat interfaces with on the back end at this writing.)

The code has a neat example in it of using a cool feature called logits_bias to effectively evaluate whether the user is attempting to end the chat, and to do so in a programmatic & deterministic way. (The "quit" command always works but the user could say for example "ok bye" and the AI will dutifully terminate the chat.) 

**This is actually a *somewhat* more complex problem** than just asking the LLM "does the user want to quit y/n?" (which only moves the problem) and I hope my sample function helps people make sense of it.

https://github.com/DPHAD/Celestia-Retro-PC/tree/main/Code


## Notes on making it
* I had to use a new spool of filament (different brand) 4/5 of the way into the print and the slight color change is kind of noticeable! Oh well!
* The 3D model is still a work in progress. Add adhesive or cable management where needed and desired. (For example, there is no positive retention for the keyboard. A bit of adhesive should solve that.)
* The USB hub at the back is just a separate unit I attached to the Raspberry Pi and glued in. It's handy to attach a USB stick, a mouse, etc.
* Printing this in one piece requires a big build platform. The only parts that should need supports are the ports at the back and the "crossbar" above the keyboard.
* The "fins" at the upper end on the inside, nearest the top, help everything print without supports. The set of fins nearest the open face where the screen goes are only slightly connected, making them easy to cut/pull out after printing to make room for cables. [I suggest removing at least this one](https://github.com/DPHAD/Celestia-Retro-PC/assets/28654887/8e2114d2-f115-4b87-bd76-186c321ac375) to make room for the cables connected to the display. The other two fins (the "back" ones) are much more solidly connected and you'll probably need a rotary tool to remove *those*.
* I printed with a monstrous 0.8 mm nozzle. It's a big print. There's plenty of space on the inside.
* Matte White PLA filament is a really good match for the Raspberry Pi keyboard!
* CAD model provided for your own development. The CAD model provides a few primitives that hopefully make fiddling and remixing a bit easier.
* At this time there is no means of screwing the display in to secure it. I suggest rolling your own solution to secure the screen to your personal comfort level. Personally, I made some custom little plastic tabs that I anchored in with E6000 glue, and those act as screw mounts. There is a 3D model of the assembly screw hole pattern, if you find it useful.
* The back access panel is magnetically attached (in my version). There are holes provided for gluing small disc magnets.
