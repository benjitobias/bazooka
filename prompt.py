from __future__ import unicode_literals
from threading import Thread

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import FuzzyWordCompleter


class BazookaPrompt(Thread):
    def __init__(self, commands):
        Thread.__init__(self)
        self.setName("BazookaPrompt")

        self.commands = commands
        completer = FuzzyWordCompleter(self.commands.keys())
        self.session = PromptSession(completer=completer)

    def run(self):
        while True:
            try:
                text = self.session.prompt('bazooka:> ')
                try:
                    command, args = text.split(None, 1)
                except ValueError:
                    command = text.strip()
                    args = ""
                try:
                    self.commands[command](args)

                except (NameError, KeyError):
                    print("%s is not a valid command" % text)

            except KeyboardInterrupt:
                continue
            except EOFError:
                break

