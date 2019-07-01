import os
import sqlite3
import logging

from commands import send_message, set_local_clipboard, get_local_clipboard
from screenshare import *
from commands import capture

from werkzeug.utils import secure_filename

from jinja2 import utils
from flask import Flask, request, render_template, flash, redirect, send_file, jsonify, url_for

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

IP = "10.251.251.110"
TARGET = "http://%s:1337/message" % IP
UPLOAD_FOLDER = 'uploads'


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    return ""


@app.route('/message', methods=["POST"])
def msg():
    message = request.data
    if len(message) == 0:
        message = request.form.get("msg")
    with open("log", "a+") as log:
        log.write(message)
        log.write("\n")
    print("\nRecv :< \u001b[33m", message, "\u001b[0m")
    return ""


@app.route('/file', methods=['POST'])
def file():
    if 'file' not in request.files:
        flash('No file!')
        return 400
    r_file = request.files['file']
    if r_file.filename == '':
        flash('No selected file!')
        return 400

    if r_file:
        file_name = secure_filename(r_file.filename)
        r_file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        return 200


@app.route('/screenshot', methods=['POST'])
def screen_share():
    if 'image' not in request.files:
        flash('No image!')
        return 400
    image = request.files['image']
    image.save('/tmp/shit.png')
    return display_sreengrab()


@app.route('/camera', methods=['GET'])
def camera():
    capture()
    return send_file("/tmp/cheese.png", mimetype='image/png')


@app.route('/post', methods=["POST"])
def post():
    data = request.form.get("msg")
    send_message(data)
    return ""


@app.route('/clipboard', methods=["GET", "POST"])
def clipboard():
    if request.method == 'POST':
        clipboard_data = request.data.decode('utf-8')
        set_local_clipboard(clipboard_data)
        return ""
    if request.method == 'GET':
        return get_local_clipboard()
    return ""

@app.route('/log')
def log():
    try:
        with open('log', 'r') as log:
            data = log.read()
    except FileNotFoundError:
        open('log', 'w').close()
        data = ""
    data = str(utils.escape(data))
    data = data.replace('\n', '</br>')
    return data


@app.route('/test')
def test():
    db = sqlite3.connect("bazooka.db")
    messages = db.execute("select rowid, sender, content, type from chat").fetchall()
    db.close()
    chat = list()
    for msg_id, msg_sender, msg_content, msg_type in messages:
        chat.extend([{
            "id": msg_id,
            "sender": msg_sender,
            "content": msg_content,
            "type": msg_type
         }])

    return render_template('new.html', chat=chat)

@app.route('/test_msg', methods=["POST"])
def test_msg():
    db = sqlite3.connect("bazooka.db")
    message = request.data
    if len(message) == 0:
        message = request.form.get("msg")

    db.execute("insert into chat (sender, content, type) values ('Sagi', ?, 1)", (message,))
    db.commit()
    db.close()
    print("\nRecv :< \u001b[33m", message, "\u001b[0m")
    return ""

@app.route('/get_new')
def test_get_new():
    id = request.args.get('id')
    id = id.split('-')[-1]
    query = 'select rowid, sender, content, type from chat where rowid > ?'
    db = sqlite3.connect("bazooka.db")
    new_messages = db.execute(query, (int(id) + 1),).fetchall()
    db.close()

    chat = list()
    for msg_id, msg_sender, msg_content, msg_type in new_messages:
        chat.extend([{
            "id": msg_id,
            "sender": msg_sender,
            "content": msg_content,
            "type": msg_type,
            "sender_avatar": '/static/' + msg_sender + ".jpg"
        }])
    return jsonify(chat)


def start_server():
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(port=1337, host="0.0.0.0")


