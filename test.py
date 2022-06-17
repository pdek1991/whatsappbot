import pyautogui as pt
from time import sleep
import pyperclip
import random
import requests
import json
sleep(1)
msg=0
while msg < 1:
        position1 = pt.locateOnScreen("dot.png", confidence=.7)
        pt.moveTo(position1)
        pt.moveRel(-100, 0)
        pt.click()
        sleep(3)

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

        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

        payload = f"q={whatsapp_message}&target=por&source=en"
        headers = {
                "content-type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "application/gzip",
                "X-RapidAPI-Key": "ee61d44183mshe76e23555745b92p186385jsn69161f13882b",
                "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }

        response = requests.request("POST", url, data=payload, headers=headers)


        final = json.loads(response.text)
        print(final)
        test = str(final['data']['translations'][0]['translatedText'])

        sleep(2)
        position3 = pt.locateOnScreen("msg.png", confidence=.6)
        x = position3[0]
        y = position3[1]
        print(test)
        pt.moveTo(x + 200, y + 20, duration=.5)
        pt.click()
        pt.typewrite(test, interval=.01)
        pt.typewrite("\n", interval=.01)
        msg+=1
        sleep(2)