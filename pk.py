import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(1)

position1 = pt.locateOnScreen("msg.png", confidence=0.3)
print(position1)
x = position1[0]
y = position1[1]


# gets message
def get_message():
    position = pt.locateOnScreen("msg.png", confidence=.3)
    x = position[0]
    y = position[1]

    pt.moveTo(x, y, duration=.05)
    pt.moveTo(x - 40, y - 80, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()
    global whatsapp_message
    whatsapp_message = pyperclip.paste()
    pt.click()
    print(whatsapp_message)
    return whatsapp_message


def post_response(message):
    global x, y

    position = pt.locateOnScreen("msg.png", confidence=.3)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)


# get_message()
def process_response(message):
    if "hi" in str(message).lower():
        return "Hello"
    else:
        return None


def check_for_new_messages():
    pt.moveTo(x + 50, y - 45, duration=.5)

    position = pt.locateOnScreen("circle.png", confidence=.6)
    sleep(3)
    if position is not None:
        pt.moveTo(position)
        pt.moveRel(-100, 0)
        pt.click()
        processed_message = process_response(get_message())
        post_response(processed_message)
        sleep(1)

    else:
        print("No messages")
        sleep(10)


check_for_new_messages()
# processed_message = process_response(get_message())
# post_response(processed_message)
