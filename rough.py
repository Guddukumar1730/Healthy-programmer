


from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("01 Jeene Laga Hoon (Ramaiya Vastavaiya) Atif.mp3")

# Setting the volume
mixer.music.set_volume(1.0)

# Start playing the song
mixer.music.play()

# infinite loop
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input(" ")

    if query =="e"

        # Stop the mixer
        mixer.music.stop()

