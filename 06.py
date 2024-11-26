import cv2
from pytesseract import pytesseract
from PIL import ImageGrab
import cv2
import numpy as np
import time
import pyautogui


pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


time.sleep(3)





while True:

    captchasorgu = pyautogui.locateCenterOnScreen('captcha.png', region=(0, 0, 1920, 1080), grayscale=True,
                                                  confidence=0.85)

    if captchasorgu is not None:
        screenshot = np.array(ImageGrab.grab(bbox=(0, 0, 1024, 800)))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
        cv2.imwrite("ss.png", screenshot)
        time.sleep(1)
        img2 = cv2.imread("ss.png")
        img = img2[355:415, 385:635]
        words_in_image = pytesseract.image_to_string(img)

        ifix = words_in_image.replace("I", "1")
        sfix = ifix.replace("S", "5")
        rfix = sfix.replace("r", "1")
        ofix = rfix.replace("o", "0")
        tfix = ofix.replace("T", "1")
        boslukfix = ofix.replace(" ", "")
        gfix = boslukfix.replace("G", "6")
        print(gfix)

        time.sleep(1)
        pyautogui.write(gfix)
        pyautogui.click(512, 468)  #confrim



