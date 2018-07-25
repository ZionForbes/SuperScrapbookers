def setup():
    background(255)
    size(1900, 1000)
    
    img = loadImage('StartPage.png')
    img2 = loadImage('notes1.png')
    img3 = loadImage('notes2.png')
    img4 = loadImage('notes3.png')
    
    #startPage
    image(img, 400, 0, 1000, 1000)
    #music notes
    image(img3, 300, 900, 80, 80)
    image(img4, 200, 100, 80, 80)
    image(img3, 1500, 500, 80, 80)
    image(img4, 1700, 800, 90, 90)
    image(img2, 1750, 200, 90, 90)
    image(img2, 100, 500, 90, 90)
    image(img3, 150, 700, 90, 90)
    image(img4, 1550, 100, 90, 90)
    
    
   
