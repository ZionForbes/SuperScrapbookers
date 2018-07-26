add_library("minim")

def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

print "Scrap book"
def setup():
    
    size(1900, 1000)
    global BG, Song1, Song2, Song3, Song4, Song5, Song6, Choice, DictionaryList, CurrentImage, CurrentSticker, BackgroundCondition
    BackgroundCondition = True
    CurrentImage = None
    CurrentSticker = None
    Choice = "0"
    minim = Minim(this)
    Song1 = minim.loadFile("Biz Markie - Just a Friend.wav")
    Song2 = minim.loadFile("Drake - In My Feelings.wav")
    Song3 = minim.loadFile("Like Mike - We're Playing Basketball.wav")
    Song4 = minim.loadFile("Miley Cyrus - Party in the USA.wav")
    Song5 = minim.loadFile("Nicki Minaj - Chun Li.wav")
    Song6 = minim.loadFile("Sister Sledge - We are Family.wav")
    BG = None

#toolbar R
    rect(1770, 0, 130, 30)#sticker label
    fill(0)
    textSize(27)
    text("Stickers",1785,25)

#Sticker

#Background
    rect(1770, 400, 130, 30)#bg label
    fill(255)
    textSize(22)
    text("Background", 1773, 423)
    fill(255)


    
#Music
    rect(1770, 540, 130, 30)#music label
    fill(0)
    textSize(25)
    text("Music", 1802, 565)
    fill(255)
    rect(1770, 570, 130, 350)
    
#undo
    rect(1770, 920, 65, 80)#undo
    
#new pages 
    rect(1835, 920, 65, 80)#reset
    
    
    
#pages
    rect(150, 0, 820, 1000)
    rect(950, 0, 820, 1000)
    
    DictionaryList= []
                          
    DictionaryList.append({"Type": "Image", 
                           "Filename": loadImage("Pic1.png"),
                           "x": 0, 
                           "y": 0,
                           "Width": 75,
                           "Height": 100 })
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic2.png"), "x": 75, "y": 0,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic3.png"), "x": 0, "y": 100,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic4.png"), "x": 75, "y": 100,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic5.png"), "x": 0, "y": 200,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic6.png"), "x": 75, "y": 200,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic7.png"), "x": 0, "y": 300,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic8.png"), "x": 75, "y": 300,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic9.png"), "x": 0, "y": 400,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("pic10.png"), "x": 75, "y": 400,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("pic11.png"), "x": 0, "y": 500,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic12.png"), "x": 75, "y": 500,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("pic13.png"), "x": 0, "y": 600,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic14.png"), "x": 75, "y": 600,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic15.png"), "x": 0, "y": 700,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic16.png"), "x": 75, "y": 700,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic17.png"), "x": 0, "y": 800,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic18.png"), "x": 75, "y": 800,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic19.png"), "x": 0, "y": 900,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": loadImage("Pic20.png"), "x": 75, "y": 900,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Sticker", "Filename": loadImage("stick1.png"), "x": 1770, "y": 30,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": loadImage("stick2.png"), "x": 1835, "y": 30,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": loadImage("stick3.png"), "x": 1770, "y": 104,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": loadImage("stick4.png"), "x": 1835, "y": 104,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": loadImage("stick5.png"), "x": 1770, "y": 178,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": loadImage("stick6.png"), "x": 1835, "y": 178,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": loadImage("stick7.png"), "x": 1770, "y": 252,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": loadImage("stick8.png"), "x": 1835, "y": 252,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": loadImage("stick9.png"), "x": 1770, "y": 326,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": loadImage("stick10.png"), "x": 1835, "y": 326,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Background", "Filename": loadImage("BG1.2.png"), "BGImage": loadImage("BG1.png"), "x": 1770, "y": 430,
                           "Width": 65, "Height": 55})
    DictionaryList.append({"Type": "Background", "Filename": loadImage("BG2.2.png"),  "BGImage": loadImage("BG2.png"), "x": 1835, "y": 430,
                           "Width": 65, "Height": 55})
    DictionaryList.append({"Type": "Background", "Filename": loadImage("BG3.2.png"),  "BGImage": loadImage("BG3.png"), "x": 1770, "y": 485,
                           "Width": 65, "Height": 55})
    DictionaryList.append({"Type": "Background", "Filename": loadImage("BG4.2.png"),  "BGImage": loadImage("BG4.png"), "x": 1835, "y": 485,
                           "Width": 65, "Height": 55})
    DictionaryList.append({"Type": "Rectangle", "x": 0, "y": 0, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 75, "y": 0, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 0, "y":100, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 75, "y": 100, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 0, "y": 200, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 75, "y": 200, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 0, "y": 300, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 75, "y": 300, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 0, "y": 400, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 75, "y": 400, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 0, "y": 500, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x":75, "y": 500, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 0, "y": 600, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x":75, "y": 600, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 0, "y": 700, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 75, "y": 700, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 0, "y": 800, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 75, "y": 800, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 0, "y": 900, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 75, "y": 900, "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Rectangle", "x": 1770, "y": 430, "Width": 65, "Height": 55})
    DictionaryList.append({"Type": "Rectangle", "x": 1835, "y": 430, "Width": 65, "Height": 55})
    DictionaryList.append({"Type": "Rectangle", "x": 1770, "y": 485, "Width": 65, "Height": 55})
    DictionaryList.append({"Type": "Rectangle", "x": 1835, "y": 485, "Width": 65, "Height": 55})


def draw():
    global BG, CurrentImage, BackgroundCondition, CurrentSticker, Choice
    
    
    if BackgroundCondition == True:
        fill(255)
        rect(150, 0, 820, 1000)
        rect(950, 0, 820, 1000)
    else:
        image(BG, 150, 0, 1600, 1000)
    

                
    for Dictionaries in DictionaryList:
        if Dictionaries["Type"] == "Rectangle":
            noFill()
            rect(Dictionaries["x"], Dictionaries["y"], Dictionaries["Width"], Dictionaries["Height"])
        elif Dictionaries["Type"] == "Image":
            img = Dictionaries["Filename"]
            image(img, Dictionaries["x"], Dictionaries["y"], Dictionaries["Width"], Dictionaries["Height"])
            
            if mousePressed and not CurrentImage and mouseX >= Dictionaries["x"] and mouseX <= Dictionaries["x"] + 75 and mouseY >= Dictionaries["y"] and mouseY <= Dictionaries["y"] + 100:
                 CurrentImage = img
                
        elif Dictionaries["Type"] == "Sticker":
            img = Dictionaries["Filename"]
            image(img, Dictionaries["x"], Dictionaries["y"], Dictionaries["Width"], Dictionaries["Height"])
            
            if mousePressed and not CurrentSticker and mouseX >= Dictionaries["x"] and mouseX <= Dictionaries["x"] + 65 and mouseY >= Dictionaries["y"] and mouseY <= Dictionaries["y"] + 74:
                CurrentSticker = img
        elif Dictionaries["Type"] == "Background":
            img = Dictionaries["Filename"]
            image(img, Dictionaries["x"], Dictionaries["y"], Dictionaries["Width"], Dictionaries["Height"])
            
    if mousePressed and mouseX >= 1760 and mouseX <= 1840 and mouseY >= 560 and mouseY <= 640:
        Choice = input("Choose a Number:\n 1. Just a Friend\n 2. In my feelings\n 3. We're playing Basketball\n 4. Party in the USA\n 5. Chun Li\n 6. We are Family")
        type(Choice)
                
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
    elif Choice == "6":
        Song6.play()
        
    if CurrentImage:
        image(CurrentImage, mouseX, mouseY,200,300)
        
    if CurrentSticker:
        image(CurrentSticker, mouseX, mouseY, 65, 74)
        
    for BGDict in DictionaryList:
        # BGDict.get("Type")
        if BGDict["Type"] == "Background":
            if mousePressed and mouseX >= BGDict["x"] and mouseX <= BGDict["x"] + BGDict["Width"] and mouseY >= BGDict["y"] and mouseY <= BGDict["y"] + BGDict["Height"]:
                BG = BGDict["BGImage"]
                #image(BG,150,0,1600,1000)
                BackgroundCondition = False
                
    fill(0, 255, 0)
    ellipse(1800, 600, 40, 40)
    ellipse(1855, 600, 40, 40)
    fill(0)
    rect(1849, 590, 3, 25)
    rect(1859, 590, 3, 25)

    triangle(1792, 587, 1792, 613, 1809, 600)
    
    
    
    
def mouseReleased():
    global CurrentImage, CurrentSticker, DictionaryList
    if CurrentImage:
        DictionaryList.append({"Type": "Image",
                           "Filename": CurrentImage,
                           "x": mouseX,
                           "y": mouseY,
                           "Width": 200,
                           "Height": 300 })
    if CurrentSticker:
        DictionaryList.append({"Type": "Image",
                               "Filename": CurrentSticker,
                               "x": mouseX,
                               "y": mouseY,
                               "Width": 65,
                               "Height": 74 })
        
        
    CurrentImage = None
    CurrentSticker = None

        
                
    
                
                
                
    
        
        
       
    
    
    
