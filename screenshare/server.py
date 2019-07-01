import os
import base64
from PIL import ImageTk, Image
import tkinter as tk
from mss import mss


def grab_screen():
    with mss() as sct:
        sct.shot(mon=-1, output="/tmp/shit.png")


def display_sreengrab():
    html_template = """
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
<img src="data:image/png;base64, %s">
</body>
</html>
    """
    with open("/tmp/shit.png", "rb") as img:
        img_data = img.read()
    img = base64.b64encode(img_data).decode('ascii')

    with open("/tmp/img.html", "w") as page:
        page.write(html_template % img)
    # Image.open("/tmp/shit.png").show()
    os.system("google-chrome --app=file:///tmp/img.html")
    return ""
