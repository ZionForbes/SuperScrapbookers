add_library("minim")

def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def setup():
    global Song1, Song2, Song3, Song4, Song5, Song6, Choice
    size(200, 200)
    background(255) 
    Choice = input("Choose 1 - 6")
    type(Choice)
    minim = Minim(this)
    Song1 = minim.loadFile("Biz Markie - Just a Friend.wav")
    Song2 = minim.loadFile("Drake - In My Feelings.wav")
    Song3 = minim.loadFile("Like Mike - We're Playing Basketball.wav")
    Song4 = minim.loadFile("Miley Cyrus - Party in the USA.wav")
    Song5 = minim.loadFile("Nicki Minaj - Chun Li.wav")
    Song6 = minim.loadFile("Sister Sledge - We are Family.wav")
def draw():
    if Choice == "1":
        Song1.play()
    elif Choice == "2":
        Song2.play()
    elif Choice == "3":
        Song3.play()
    elif Choice == "4":
        Song4.play()
    elif Choice == "5":
        Song5.play()
    else:
        Song6.play()
    # getVolume ( )
    # isLooping ( )
    # isMuted ( )
    # isPlaying ( )
