import pyautogui as pt
pt.PAUSE = 1
from time import sleep
import pyperclip
import random
import requests
import json

position = pt.locateOnScreen("msg.png", confidence=.6)
x = position[0]
y = position[1]
pt.moveTo(x, y, duration=.05)
pt.moveTo(x - 40, y - 80, duration=.5)

pt.tripleClick()
pt.rightClick()
pt.moveRel(12, 15)
pt.click()
whatsapp_message = pyperclip.paste()
print(whatsapp_message)
pt.click()

if 'Hi' in whatsapp_message:
    test = "Hello, How are you"
else:
    test = "What do you mean"
position3 = pt.locateOnScreen("msg.png", confidence=.6)
x = position3[0]
y = position3[1]
print(test)
pt.moveTo(x + 30, y + 30, duration=.5)
pt.doubleClick()
sleep(2)
pt.typewrite(test, interval=.01)
pt.typewrite("\n", interval=.01)

