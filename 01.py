from PIL import ImageGrab
import cv2
import numpy as np
import time



screenshot = np.array(ImageGrab.grab(bbox=(0, 0, 1024, 800)))
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)

cv2.imwrite("ss.png", screenshot)
time.sleep(1)

