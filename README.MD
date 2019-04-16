# atonelib
atonelib v0.0.4 alpha - rev 2019/4/15
Original example code at https://askubuntu.com/a/55825
Adapted by Steve Weston (thestewsy) 2018/6/12, Github'ed 2019/4/15

I. Description
atonelib is a mini-library to be used in conjunction with PyAudio to generate audio tones at fixed frequencies. The sound is reminiscent of single-channel 1980's video game console sound chips.

II. Usage

1. Import
e.g. import atonelib

NOTE: atonelib will import the PyAudio library.

1. An array must be made which becomes the PyAudio object and stream and houses the PyAudio object, stream, and bitrate.
Thus, tonearray = atonelib.open_tone(bitrate)

The bitrate could be 8000, 11025, 22050, etc.

2. To play a tone
atonelib.play_tone(tonearray, frequency, length, *vartype, *bitrate)

frequency is in hertz and can be something like 230, 500, etc. Be aware that very low or very high frequencies may not be audible.

length is length in seconds. Fractions of seconds like 0.25 or 0.5 or even 0.004 can be used.

vartype is variable type used to store the frequency stream: 0 - byte integer (default), 1 - unicode integer 
Byte integer is a 'smoother' sound and takes up less variable space, unicode integer is a 'buzzier' sound and takes up more variable space.

bitrate overrides the bitrate used when opening the stream. This can be used for some odd effects.

*Parameter is optional

3. Close the array and PyAudio object and stream
atonelib.close_tone(tonearray)

III. Application

So what are some ways one can use this library? Well one can loop over an array with frequencies and tone lengths in it, like this:

notes = [[230, 0.25], [260, 0.25], [290, 0.25], [230, 0.25], [230, 0.25], [260, 0.25], [290, 0.25], [230, 0.25]]

for x in notes:
        atonelib.play_tone(tonearray, x[0], x[1])

A whole bank of 'notes' can be played this way.

Another thing one can do is play very short tones while changing the frequency in a for loop.

for x in range(0, 3, 1):
        for y in range(0, 100, 2):
                atonelib.play_tone(tonestream, 500 + (y * 30), 0.01)

This makes for a nifty *wooooOOOOOPP* noise.

IV. A Word About Threading
play_tone stops execution of other statements in python until the sound is finished playing. If you don't want that, one way around it is with threading. If you're not familiar with threading, it allows multiple processes in Python to be running at once and is very useful for tons of purposes.

1. import threading

2. Make a function for the thread to run
def notes_snd():

        tonearray = atonelib.open_tone(7000)

        notes = [[230, 0.25], [260, 0.25], [290, 0.25], [230, 0.25], [230, 0.25],
         [260, 0.25], [290, 0.25], [230, 0.25]]

        for x in notes:
                atonelib.play_tone(tonearray, x[0], x[1])

        atonelib.close_tone(tonearray)

3. Define the thread object
soundThread = threading.Thread(notes=notes_snd)

4. Start it
soundThread.start()

Now other statements can run with it making noise in the background. If the other statements finish before it is done, the program will wait until the soundThread is finished before Python stops running, which brings us to the next point.

5. Stopping the thread
There are several ways to stop thread code from executing. Generally it's not a good idea to have something outside of the thread kill a thread immediately. Threads may be juggling several balls, so to speak, and so it's better to notify a routine that it should be stopped, so that it can wind things down itself.

stopSound = False 
soundThread = threading.Thread(target=notes_snd, args=(lambda: stopSound,))

A lambda is an anonymous function. Passing a function as a parameter means every time the parameter is referenced, the function is run. In this case, the function returns the value of stopSound from the main program.
One can set stopSound = True at a later point in the main program to change what the parameter returns.

6. def notes_snd(stop)
Add the stop parameter, that will be the name of the anonymous function, do not put parenthesis yet.
In the for loop, or anywhere in notes_snd that you might want to check regularly to see if stopSound has changed, add the stop condition:

...
for x in notes
        if stop():
        break
...

7. stopsound = True
If stopSound is true, it would return true at the if statement and break out of the for loop, and fall to the atonelib.close_tone(tonearray) statement and finish out the routine and thread.

8. soundThread.join()
After setting stopsound = True, it's good practice to do a join. This joins the soundThread thread and main programs together so that the main program waits for the thread to close out before continuing. This is in case the main program would do something that would conflict with the thread not being stopped yet.

V. Acknowledgements

Thanks to the people at https://askubuntu.com/a/55825 for their discussion thread which inspired this library.

