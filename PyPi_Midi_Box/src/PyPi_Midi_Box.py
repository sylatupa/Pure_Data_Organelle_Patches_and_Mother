import mido
import time
from collections import deque
import random
from mido import MidiFile

def search_for_midi():
    rtmidi = mido.Backend('mido.backends.rtmidi')   
    print(rtmidi)

def get_midi_output():
    #output = rtmidi.open_output('DigitalKBD 20:0')
    #output.send(mido.Message('note_on', note=60, velocity=64))
    print (mido.get_output_names()) # To list the output ports
    outname = mido.get_output_names()[1]
    inname = mido.get_input_names()[0]
    print (outname) # To list the input ports
    #name = "USB Midi 0"
    inport = mido.open_input(inname)
    outport = mido.open_output(outname)

def get_midi_input():
    #output = rtmidi.open_output('DigitalKBD 20:0')
    #output.send(mido.Message('note_on', note=60, velocity=64))
    print (mido.get_output_names()) # To list the output ports
    outname = mido.get_output_names()[1]
    inname = mido.get_input_names()[0]
    print (outname) # To list the input ports
    #name = "USB Midi 0"
    inport = mido.open_input(inname)
    outport = mido.open_output(outname)
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
    #num = int(random.random() * 127)

    print(num)
    #while inport.pending():
    #    msg = inport.receive()
    #    if msg.type != "clock":
    #        print(msg)
    #        msglog.append({"msg": msg, "due": time.time() + echo_delay})
    outport.send(mido.Message('note_on',note=num, velocity=100))
    time.sleep(.1)
    outpor.send(mido.Message('note_off',note=num, velocity=100))
