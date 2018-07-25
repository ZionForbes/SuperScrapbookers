print "Scrap book"
def setup():
    
    size(1900, 1000)
    global BG 
    BG = None
    global DictionaryList
    
#photo toolbar L
    # rect(0, 0, 75, 100)#1
    # rect(75, 0, 75, 100)#2
    # rect(0, 100, 75, 100)#3
    # rect(75, 100, 75, 100)#4
    # rect(0, 200, 75, 100) #5
    # rect(75, 200, 75, 100)#6
    # rect(0, 300, 75, 100) #7
    # rect(75, 300, 75, 100)#8
    # rect(0, 400, 75, 100) #9
    # rect(75, 400, 75, 100)#10
    # rect(0, 500, 75, 100) #11
    # rect(75, 500, 75, 100)#12
    # rect(0, 600, 75, 100) #13
    # rect(75, 600, 75, 100)#14
    # rect(0, 700, 75, 100) #15
    # rect(75, 700, 75, 100)#16
    # rect(0, 800, 75, 100) #17
    # rect(75, 800, 75, 100)#18
    # rect(0, 900, 75, 100)#19
    # rect(75, 900, 75, 100)#20
    
    
    
#toolbar R
    rect(1770, 0, 130, 30)#sticker label
    fill(0)
    textSize(27)
    text("Stickers",1785,25)

#Sticker
    fill(255)
    rect(1770, 30, 65, 74)#1
    rect(1835, 30, 65, 74)#2
    rect(1770, 104, 65, 74)#3
    rect(1835, 104, 65, 74)#4
    rect(1770, 178, 65, 74)#5
    rect(1835, 178, 65, 74)#6
    rect(1770, 252, 65, 74)#7
    rect(1835, 252, 65, 74)#8
    rect(1770, 326, 65, 74)#9
    rect(1835, 326, 65, 74)#10
    
#Background
    rect(1770, 400, 130, 30)#bg label
    fill(0)
    textSize(22)
    text("Background", 1773, 423)
    fill(255)
    # rect(1770, 430, 65, 55)#1
    # rect(1835, 430, 65, 55)#2
    # rect(1770, 485, 65, 55)#3
    # rect(1835, 485, 65, 55)#4
    

    
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
    
    
    
#photo frames L
#     rect(200, 120, 300, 250)
#     rect(580, 630, 330, 260)
#     rect(350, 350, 400, 300)
#     rect(190, 670, 300, 250)
#     rect(580, 80, 300, 250)
    
 #photo frames R
#     rect(1000, 80, 350, 250)
#     rect(1365, 80, 350, 250)
#     rect(1160, 365, 400, 280)
#     rect(1000, 680, 350, 250)
#     rect(1365, 680, 350, 250)
    
#images
    # img = loadImage("Pic1.png")
    # image(img,0, 0, 75, 100)
    # img = loadImage("Pic2.png")
    # image(img,75, 0, 75, 100)
    # img = loadImage("Pic3.png")
    # image(img,0, 100, 75, 100)
    # img = loadImage("Pic4.png")
    # image(img,75, 100, 75, 100)
    # img = loadImage("Pic5.png")
    # image(img,0, 200, 75, 100)
    # img = loadImage("Pic6.png")
    # image(img,75, 200, 75, 100)
    # img = loadImage("Pic7.png")
    # image(img,0, 300, 75, 100)
    # img = loadImage("Pic8.png")
    # image(img,75, 300, 75, 100)
    # img = loadImage("Pic9.png")
    # image(img,0, 400, 75, 100)
    # img = loadImage("pic10.png")
    # image(img,75, 400, 75, 100)
    # img = loadImage("pic11.png")
    # image(img,0, 500, 75, 100)
    # img = loadImage("Pic12.png")
    # image(img,75, 500, 75, 100)
    # img = loadImage("pic13.png")
    # image(img,0, 600, 75, 100)
    # img = loadImage("Pic14.png")
    # image(img,75, 600, 75, 100)
    # img = loadImage("Pic15.png")
    # image(img,0, 700, 75, 100)
    # img = loadImage("Pic16.png")
    # image(img,75, 700, 75, 100)
    # img = loadImage("Pic17.png")
    # image(img,0, 800, 75, 100)
    # img = loadImage("Pic18.png")
    # image(img,75, 800, 75, 100)
    # img = loadImage("Pic19.png")
    # image(img,0, 900, 75, 100)
    # img = loadImage("Pic20.png")
    # image(img,75, 900, 75, 100)
    
    
#stickers
    # img = loadImage("stick1.png")
    # image(img,1770, 30, 65, 74)
    # img = loadImage("stick2.png")
    # image(img,1835, 30, 65, 74)
    # img = loadImage("stick3.png")
    # image(img,1770, 104, 65, 74)
    # img = loadImage("stick4.png")
    # image(img,1835, 104, 65, 74)
    # img = loadImage("stick5.png")
    # image(img,1770, 178, 65, 74)
    # img = loadImage("stick6.png")
    # image(img,1835, 178, 65, 74)
    # img = loadImage("stick7.png")
    # image(img,1770, 252, 65, 74)
    # img = loadImage("stick8.png")
    # image(img,1835, 252, 65, 74)
    # img = loadImage("stick9.png")
    # image(img,1770, 326, 65, 74)
    # img = loadImage("stick10.png")
    # image(img,1835, 326, 65, 74)
    
#bakgrounds

    # img = loadImage("BG1.2.png")
    # image(img,1770, 430, 65, 55)
    # img = loadImage("BG2.2.png")
    # image(img,1835, 430, 65, 55)
    # img = loadImage("BG3.2.png")
    # image(img,1770, 485, 65, 55)
    # img = loadImage("BG4.2.png")
    # image(img,1835, 485, 65, 55)
    
    # dict= []
    # dict.append({"Type": "BG", "Filename":
    
    DictionaryList= []
    # ImgList = ["Pic1.png", "Pic2.png", "Pic3.png", "Pic4.png", "Pic5.png",
    #            "Pic6.png", "Pic7.png", "Pic8.png", "Pic9.png", "Pic10.png",
    #            "Pic11.png", "Pic12.png", "Pic13.png", "Pic15.png", "Pic16.png",
    #            "Pic17.png", "Pic18.png", "Pic19.png", "Pic20.png"]
    # for ImageName in ImgList:
    #     obj.append({"Type": "Image", "img" : loadImage(ImageName), "x": 
                          
    DictionaryList.append({"Type": "Image", 
                           "Filename": "Pic1.png",
                           "x": 0, 
                           "y": 0,
                           "Width": 75,
                           "Height": 100 })
    DictionaryList.append({"Type": "Image", "Filename": "Pic2.png", "x": 75, "y": 0,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic3.png", "x": 0, "y": 100,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic4.png", "x": 75, "y": 100,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic5.png", "x": 0, "y": 200,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic6.png", "x": 75, "y": 200,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic7.png", "x": 0, "y": 300,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic8.png", "x": 75, "y": 300,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic9.png", "x": 0, "y": 400,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "pic10.png", "x": 75, "y": 400,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "pic11.png", "x": 0, "y": 500,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic12.png", "x": 75, "y": 500,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "pic13.png", "x": 0, "y": 600,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic14.png", "x": 75, "y": 600,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic15.png", "x": 0, "y": 700,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic16.png", "x": 75, "y": 700,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic17.png", "x": 0, "y": 800,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic18.png", "x": 75, "y": 800,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic19.png", "x": 0, "y": 900,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Image", "Filename": "Pic20.png", "x": 75, "y": 900,
                           "Width": 75, "Height": 100})
    DictionaryList.append({"Type": "Sticker", "Filename": "stick1.png", "x": 1770, "y": 30,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": "stick2.png", "x": 1835, "y": 30,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": "stick3.png", "x": 1770, "y": 104,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": "stick4.png", "x": 1835, "y": 104,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": "stick5.png", "x": 1770, "y": 178,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": "stick6.png", "x": 1835, "y": 178,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": "stick7.png", "x": 1770, "y": 252,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": "stick8.png", "x": 1835, "y": 252,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": "stick9.png", "x": 1770, "y": 326,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Sticker", "Filename": "stick10.png", "x": 1835, "y": 326,
                           "Width": 65, "Height": 74})
    DictionaryList.append({"Type": "Background", "Filename": "BG1.2.png", "x": 1770, "y": 430,
                           "Width": 65, "Height": 55})
    DictionaryList.append({"Type": "Background", "Filename": "BG2.2.png", "x": 1835, "y": 430,
                           "Width": 65, "Height": 55})
    DictionaryList.append({"Type": "Background", "Filename": "BG3.2.png", "x": 1770, "y": 485,
                           "Width": 65, "Height": 55})
    DictionaryList.append({"Type": "Background", "Filename": "BG4.2.png", "x": 1835, "y": 485,
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
    
    for Dictionaries in DictionaryList:
        if Dictionaries["Type"] == "Rectangle":
            noFill()
            rect(Dictionaries["x"], Dictionaries["y"], Dictionaries["Width"], Dictionaries["Height"])
        elif Dictionaries["Type"] == "Image":
            img = loadImage(Dictionaries["Filename"])
            image(img, Dictionaries["x"], Dictionaries["y"], Dictionaries["Width"], Dictionaries["Height"])
        elif Dictionaries["Type"] == "Sticker":
            img = loadImage(Dictionaries["Filename"])
            image(img, Dictionaries["x"], Dictionaries["y"], Dictionaries["Width"], Dictionaries["Height"])
        elif Dictionaries["Type"] == "Background":
            img = loadImage(Dictionaries["Filename"])
            image(img, Dictionaries["x"], Dictionaries["y"], Dictionaries["Width"], Dictionaries["Height"])
        

def draw():
    global BG
    for BGDict in DictionaryList:
        BGDict.get("Type")
        if BGDict.get("Type") == "Background":
             if mousePressed and mouseX >= 1770 and mouseX <= 1835 and mouseY >= 430 and mouseY <= 485:
                BG = loadImage("BG1.png")
        
            # {"Type": "Background", "Filename": "BG1.2.png", "x": 1770, "y": 430, "Width": 65, "Height": 55})
        
    #  if BG:
    #      image(BG,152,0,1615,1000)
    #  if mousePressed and mouseX >= 1770 and mouseX <= 1835 and mouseY >= 430 and mouseY <= 485:
    #     BG = loadImage("BG1.png")
    #  if BG:
    #      image(BG,152,0,1615,1000)
    # if mousePressed and mouseX >=1835 and mouseX <=1900 and mouseY >=430 and mouseY <=485 :
    #      BG = loadImage("BG2.png")

    
    
    
    
