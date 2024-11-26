import pyautogui


import time
time.sleep(2)
pyautogui.keyDown('v')
time.sleep(2)

captchasorgu = pyautogui.locateCenterOnScreen('npc.png', region=(0, 0, 1920, 1080), grayscale=True,
                                              confidence=0.60)
pyautogui.keyUp('v')
if captchasorgu is not None:
    pyautogui.click(captchasorgu[0], captchasorgu[1] + 100)


time.sleep(1)
npcac = pyautogui.locateCenterOnScreen('npcac.png', region=(0, 0, 1920, 1080), grayscale=True,
                                              confidence=0.70)
if npcac is not None:
    pyautogui.click(npcac[0],npcac[1])