import cv2
from pytesseract import pytesseract
from PIL import ImageGrab
import cv2
import numpy as np
import time


pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"



screenshot = np.array(ImageGrab.grab(bbox=(0, 0, 1024, 800)))
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
cv2.imwrite("ss.png", screenshot)
time.sleep(1)
img2 = cv2.imread("ss.png")
img = img2[355:415,385:635]
words_in_image = pytesseract.image_to_string(img)

print(words_in_image)


