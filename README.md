<img src="https://github.com/DPHAD/Celestia-Retro-PC/assets/28654887/75a2acb6-9124-4564-93f9-c229a80a8da7" height=320><img src="https://github.com/DPHAD/Celestia-Retro-PC/assets/28654887/144b4d59-ff8d-47ed-b714-08328db7f169" height=320>

# Celestia DIY Retro PC
The **Celestia** is a retro styled, one-piece PC using a **Raspberry Pi** (Pi400 or SBC + Official Pi keyboard). Currently designed around the **Elecrow CrowVision 11.6"** display, which is the only display that really matched what I was going for. As a bonus, it integrates a touchscreen, meaning a mouse is not necessary and helps preserve the one-piece aesthetic!

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

Launching Max Woolf's [simpleaichat](https://github.com/minimaxir/simpleaichat#simpleaichat) to create an 80s AI to interact with via the retro terminal is the icing on the cake.

## Notes on making it
* The 3D model is still a work in progress. Add adhesive or cable management where needed and desired. (For example, there is no positive retention for the keyboard. A bit of adhesive should solve that.)
* The USB hub at the back is just a separate unit I attached to the Raspberry Pi and glued in. It's handy to attach a USB stick, a mouse, etc.
* Printing this in one piece requires a big build platform. The only parts that should need supports are the ports at the back and the "crossbar" above the keyboard.
* The "fins" at the upper end on the inside, nearest the top, help everything print without supports. The set of fins nearest the open face where the screen goes are only slightly connected, making them easy to cut/pull out after printing, should one need the room for cables, etc.
* I printed with a monstrous 0.8 mm nozzle. It's a big print. There's plenty of space on the inside.
* Matte White PLA filament is a really good match for the Raspberry Pi keyboard!
* CAD model provided for your own development. The CAD model provides a few primitives that hopefully make fiddling and remixing a bit easier.
* At this time there is no means of screwing the display in to secure it. I suggest rolling your own solution to secure the screen to your personal comfort level. Personally, I made some custom little plastic tabs that I anchored in with E6000 glue, and those act as screw mounts. There is a 3D model of the assembly screw hole pattern, if you find it useful.
* The back access panel is magnetically attached (in my version). There are holes provided for gluing small disc magnets.
