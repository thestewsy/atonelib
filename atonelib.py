#atonelib v0.0.4 alpha - rev 2019/4/15
#Original example code at https://askubuntu.com/a/55825
#Adapted by Steve Weston (thestewsy) 2018/6/12, Github'ed 2019/4/15

import pyaudio
import math
import codecs

def open_tone(bitrate):
   PAObj = pyaudio.PyAudio()
   stream = PAObj.open(
       format=PAObj.get_format_from_width(1),
       channels=1,
       rate=bitrate,
       output=True,
       )
   return(PAObj, stream, bitrate)

def close_tone(stream):
   stream[1].stop_stream()
   stream[1].close()
   stream[0].terminate() 

def play_tone(stream, frequency = 261.63, length = 1.2232, bitoruni = 0, bitrate = 0):
   # bitrate is number of frames per second/frameset.    
   # frequency is Hz, waves per second, 261.63=C4-note.
   # length = 1.2232 is seconds to play sound

   if bitrate == 0:
      bitrate = stream[2]; # grab bitrate from opened object if bitrate blank

   numframes = int(bitrate * length)
   restframes = numframes % bitrate

   if bitoruni == 0:   
      wavedata = b'' # store the data in bytes
   else:
      wavedata = '' # store the data in unicode
   
   for x in range(numframes):
      if bitoruni == 0:
         wavedata += chr(int(math.sin(x / ((bitrate / frequency) / math.pi)) * 127 + 128)).encode('latin-1')
      else:
         wavedata += chr(int(math.sin(x / ((bitrate / frequency) / math.pi)) * 127 + 128))
    
   #fill remainder of frameset with silence
   for x in range(restframes):
      if bitoruni == 0:
         wavedata += chr(128).encode('latin-1')
      else:
         wavedata += chr(128)
   
   stream[1].write(wavedata)
