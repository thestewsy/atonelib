import atonelib
import threading
from time import sleep

def notes_snd(stop):

    tonearray = atonelib.open_tone(7000)

    notes = [[230, 0.25], [260, 0.25], [290, 0.25], [230, 0.25], [230, 0.25],
             [260, 0.25], [290, 0.25], [230, 0.25]]

    for x in notes:
        if stop():
            break
        
        atonelib.play_tone(tonearray, x[0], x[1])    
        
    atonelib.close_tone(tonearray)       

stopSound = False 

soundThread = threading.Thread(target=notes_snd, args=(lambda: stopSound,))
soundThread.start()

sleep(3) # Wait a while before interrupting the soundThread

stopSound = True
soundThread.join() 
