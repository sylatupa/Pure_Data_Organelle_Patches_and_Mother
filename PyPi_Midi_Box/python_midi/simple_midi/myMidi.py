import mido
import time
from collections import deque
import random

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


from mido import MidiFile

mid = MidiFile('Murder_Was_The_Case.mid', clip=True)
mid = MidiFile('bone_thugs_Crossroads.mid', clip=True)


msglog = deque()
echo_delay = 2
num = 0
cnum = 0
div = 13
vnum = 0
tnum = 0
print(mid.tracks)
# 4

for track in mid.tracks[2]:
    print("here")
    track = track.dict()
    try:
      num = track["note"]
      vnum = track["velocity"]
      tnum = track["time"]/1000
      print(tnum)
    except Exception as e:
      print(e)
    outport.send(mido.Message('note_on',note=num, velocity=vnum))
    time.sleep(tnum)
    outport.send(mido.Message('note_off',note=num, velocity=vnum))
    print(track)
    print(track)


while True:
    if cnum >= 127:
      cnum = 0
      num = 0
    elif cnum + div  	>=127:
      cnum = 0
      num = 0
    else:
      cnum = cnum + div
      num = cnum

      
    #num = int(random.random() * 127)

    print(num)
    #while inport.pending():
    #    msg = inport.receive()
    #    if msg.type != "clock":
    #        print(msg)
    #        msglog.append({"msg": msg, "due": time.time() + echo_delay})
    outport.send(mido.Message('note_on',note=num, velocity=100))	
    time.sleep(.1)
    outport.send(mido.Message('note_off',note=num, velocity=100))
