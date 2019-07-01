import requests
import clipboard


def get_local_clipboard():
    return clipboard.paste()


def set_local_clipboard(data):
    clipboard.copy(data)


def get_remote_clipboard(_):
    clip = requests.get("http://10.251.251.110:1337/clipboard").text
    print(clip)


def set_remote_clipboard(data):
    requests.post("http://10.251.251.110:1337/clipboard", data=data)
