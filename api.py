import pyautogui as pt
from time import sleep
import pyperclip
import random


position3 = pt.locateOnScreen("msg.png", confidence=.6)
x = position3[0]
y = position3[1]
print(type(position3))
chaltay = str(position3)
print(type(chaltay))
pt.moveTo(x + 200, y + 20, duration=.5)
pt.click()
pt.typewrite(chaltay, interval=.01)
pt.typewrite("\n", interval=.01)