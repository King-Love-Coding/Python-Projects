from pygame import mixer
from pygame.examples.music_drop_fade import volume

mixer.init()                             #initialisation (init) or constructor call krna
mixer.music.load("Pehle Bhi Main.mp3")
mixer.music.play()
while(1):
    choice = int(input("\n 1.Pause \n2.unpause \n3.Stop"))
    if(choice==1):
        mixer.music.pause()
    elif(choice==2):
        mixer.music.unpause()
    elif(choice==3):
        mixer.music.stop()


