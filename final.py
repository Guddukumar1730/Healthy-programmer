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
        f.write(f" {msg} {datetime.now()} \n ")

if __name__=='__main__':
    init_water=time()
    init_eyes=time()
    init_phy=time()
    watersecs=2700
    eyessecs=2400
    physecs=21
    while True:
        if time()-init_water>watersecs:
            print("drink water.\n Enter 'DRANK' to stop the alarm")
            musiconloop('Underwater-sound.mp3','DRANK')
            init_water=time()
            log_now("drank water at")
        if time() - init_eyes > eyessecs:
            print("tere naina time.\n Enter 'DONEEYES' to stop the alarm")
            musiconloop('close_eyes.mp3', 'DONEEYES')
            init_eyes = time()
            log_now("done eyes  at")
        if time() - init_phy > physecs:
            print("Aarambh hai prachand time.\n Enter 'DONEPHY' to stop the alarm")
            musiconloop('Workout Alarm.mp3', 'DONEPHY')
            init_phy = time()
            log_now("done exercise at")


