import base64
import os
import requests
import cv2


def capture():
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    video_capture.release()
    cv2.imwrite('/tmp/cheese.png', frame)


def get_camera(_):
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
    img_data = requests.get("http://10.251.251.110:1337/camera").content
    with open("/tmp/cam.png", 'wb') as x:
        x.write(img_data)
    img = base64.b64encode(img_data).decode('ascii')

    with open("/tmp/img.html", "w") as page:
        page.write(html_template % img)
    # Image.open("/tmp/shit.png").show()
    os.system("google-chrome --app=file:///tmp/img.html")
    return ""
