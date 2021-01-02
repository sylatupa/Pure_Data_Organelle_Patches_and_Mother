import mido
import time
from collections import deque
import random
from mido import MidiFile
import menu as menu

rtmidi = mido.Backend('mido.backends.rtmidi')
#print(rtmidi)
#output = rtmidi.open_output('DigitalKBD 20:0')
#output.send(mido.Message('note_on', note=60, velocity=64))
print (mido.get_output_names()) # To list the output ports
outname = mido.get_output_names()[1]
inname = mido.get_input_names()[0]
print (outname) # To list the input ports

#name = "USB Midi 0"
inport = mido.open_input(inname)
outport = mido.open_output(outname)





def record_midi():
    pass

def browse_midi():

def play_midi():
    pass
    mid = MidiFile('Murder_Was_The_Case.mid', clip=True)
    print(mid)
    msglog = deque()
    echo_delay = 2
    num = 0
    while True:
        if num >= 127:
          num = 0
        else:
          num = num + 10:ex
        print(num)
        #while inport.pending():
        #    msg = inport.receive()
        #    if msg.type != "clock":
        #        print(msg)
        #        msglog.append({"msg": msg, "due": time.time() + echo_delay})
        outport.send(mido.Message('note_on',note=num, velocity=100))
        time.sleep(.1)
        outport.send(mido.Message('note_off',note=num, velocity=100))

if __name__=='main':
    import gui as gui_client
    global menu,device_name
    menu = menu.Menu()
    menu_event = menu.menu_event #getting the function for performance
    print(  "*****************************Welcome to the menu****************************************\n***********************************************")
    print("k: UP-CHOOSE |   j: DOWN-UNLOAD   |   h: LEFT-SELECT    |    l: RIGHT-SELECT   |   a: QUIT")
    menuDict =     {"k":"up","j":"down","h":"left","l":"right","a":"quit"}
    data = dict()
    #gui_client.prnt(menu, pubsub)
    while True:
        drctn = menuDict.get(getch())
        print(drctn)
        menu.menu_event(drctn)
        #time.sleep(.01275)
        #time.sleep(.215)
        time.sleep(mqtt_client.timeSleep)
        if type(drctn)!=type(None):
            gui_client.prnt(menu, pubsub)
            pass


