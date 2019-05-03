# Critter and Guitari Organelle on a Raspberry Pi, with OSC
## A Pure Data client that sonifys MQTT and OSC data

Most of what this project is about is making a more advanced main patch--the Desktop Mother, Pure Data Patch.
I needed to look better for when I use it on my desktop, and provide some information about the audio signals going in and out.

Ideally, Pure data and the Patches run on a headless Raspberry pi, automatically. Plug in the Pi and audio out and it automatically starts to run. There are some things left undone about this; it works fine if you hard code which patches you want to automatically run, but its very difficult to change the patch when running on a headless Raspberry Pi. Work has been done on this front, but its not done.

![Desktop Mother][Desktop Mother]


Most patches and desktop mother patches are from https://www.critterandguitari.com/organelle.

- [ ] Develop the ability to produce chords, like Kordbot: https://www.soundonsound.com/reviews/isla-instruments-kordbot.
- [x] Allow for data to be sent over UDP and send it to Organelle knob1-4, notes, and vol. https://github.com/sylatupa/Digital_Culture_Server
- [x] Automatically start Pure Data and the mother patch on Raspberry Pi Boot
- [x] Ability to open a new Pure Data patch, inside of Pure Data 


## parallel_projects

These scripts and Pure Data patches are built in the context of a Digital Culture, Arts Media and Engineering, Master of Arts program and some of the following project examples are with interactive art and media. 
* [Digital_Culture_Server](https://github.com/sylatupa/Digital_Culture_Server)
** A collection of Node-Red Flows and Python Scripts. This runs on a Raspberry Pi and is connected to WiFi.
** The Digital_Thing takes sensor data and sends it over an MQTT Network. Node Red recieves this data and sends it the ETC Video Synthesizer and the Digital_Culture_Sound_Client, over OSC.  
* [Digital_Culture_Sound_Client](https://github.com/sylatupa/Digital-Culture-Sound-Client)
** A sound synthesizer written in Pure Data. This runs on a Raspberry Pi and is connected to Wifi and controlled by Node-Red and This_Thing.
* [Video_Synth-ETC_Mother_and-Modes](https://github.com/sylatupa/Video_Synth-ETC_Mother_and-Modes)
** written by Critter and Guitari for the ETC. This is installed on a Raspberry Pi that is connected to WiFi and controlled by Node-Red and This_Thing.


## An Arizona State University Herberger, Institute for the Design and the Arts, Digital Culture Masters Final Project, 2019.

  
[Desktop Mother]: https://github.com/sylatupa/Pure_Data_Organelle_Patches_and_Mother/blob/master/Images/Desktop_Mother.png

