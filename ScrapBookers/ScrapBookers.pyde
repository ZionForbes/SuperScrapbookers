add_library("minim")

def setup():
    global Song
    size(200, 200)
    background(255) 
    minim = Minim(this)
    Song = minim.loadFile("DrakeSound.wav")
    
def draw():
    Song.play()
    # getVolume ( )
    # isLooping ( )
    # isMuted ( )
    # isPlaying ( )
