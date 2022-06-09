from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")


if __name__=='__main__':
    init_water=time()
    init_eyes=time()
    init_phy=time()
    watersecs=2700
    eyessec=2400
    physecs=2100
    while True:
        if time()-init_water>watersecs:
            print("Time to drink.Enter 'DRANK' to stop the alarm")
            musiconloop("Underwater-sound.mp3","DRANK")
            init_water=time()
            log_now("Drank water at \n")
        if time()-init_eyes>eyessec:
            print("Time to relax eyes.Enter 'DONE E' to stop the alarm")
            musiconloop("close_eyes.mp3","DONE E")
            init_eyes=time()
            log_now("eyes relaxed at \n")
        if time()-init_phy>physecs:
            print("Time to streach body.Enter 'DONE S' to stop the alarm")
            musiconloop("Workout Alarm.mp3","DONE S")
            init_phy=time()
            log_now("body streached at \n")

