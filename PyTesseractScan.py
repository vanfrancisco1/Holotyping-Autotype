import cv2
import pytesseract
from PIL import ImageGrab
from pynput import keyboard
import time
Clear = True
def Image2Text(imag):
    ExtractedText = pytesseract.image_to_string(imag, config=("--psm 7"))
    return ExtractedText

def Grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def NoiseRemove(img):
    return cv2.blur(img, (1,3))

def thresholding(img):
    return cv2.threshold(img, 0 , 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def StartGame():
    print('Game Starting..')
    keyboard.Controller().press(keyboard.Key.enter)
    time.sleep(1)
    keyboard.Controller().press(keyboard.Key.enter)

# Press Ctrl + C to terminate
# Working Resolution: 1280 x 1024
def StartTyping():
    while True:
        GrabImg = ImageGrab.grab((400,490,850,540))
        GrabImg.save('SSImage.jpg')
        # GrabImg.show()
        image = cv2.imread('SSImage.jpg')
        image = Grayscale(image)
        # image = thresholding(image)
        image = NoiseRemove(image)
        res = Image2Text(image)
        if (res.replace(" ","").lower().lstrip().rstrip() == "qaa=e"):
            res = res.replace("a","&",1)
        elif(res.replace(" ","").lower().lstrip().rstrip() == "astrogir]"):
            res = res.replace("]","l",1)
        for i in res.replace(" ","").lower().lstrip().rstrip():
            if (i == "’"):
                i = "'"
            keyboard.Controller().press(i)
            keyboard.Controller().release(i)
            time.sleep(0.001)
        print(res.replace(" ","").lower().lstrip().rstrip())
        print(len(res.replace(" ","").lower().lstrip().rstrip()))

#3 seconds to change to the game
time.sleep(3)
StartGame()
time.sleep(5)
StartTyping()



