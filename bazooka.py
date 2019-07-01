import threading


from prompt import BazookaPrompt
from server import start_server

from commands import COMMANDS


if __name__ == '__main__':
    t_server = threading.Thread(target=start_server)
    t_server.setName("BazookaServer")
    t_server.setDaemon(True)
    t_server.start()
    t_prompt = BazookaPrompt(COMMANDS)
    t_prompt.start()

    threads = [t_server, t_prompt]
