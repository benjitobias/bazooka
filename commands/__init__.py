from .sender import send_message, send_message_local, send_screengrab
from .exit import quit_bazooka
from screenshare import display_sreengrab
from .camera import capture, get_camera
from .clipboard import get_remote_clipboard, set_remote_clipboard, get_local_clipboard, set_local_clipboard

COMMANDS = {
    "message": send_message,
    "test": send_message_local,
    "exit": quit_bazooka,
    "display_screengrab": display_sreengrab,
    "send_screengrab": send_screengrab,
    "get_camera": get_camera,
    "get_clip": get_remote_clipboard,
    "set_clip": set_remote_clipboard,
}