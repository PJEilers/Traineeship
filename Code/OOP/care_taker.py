from editor import *

class Caretaker():

    def __init__(self, editor: Editor) -> None:
        self._mementos = []
        self._editor = editor

    def backup(self):
        self._mementos.append(self._editor.save())

    def get_old_input(self, index):
        return self._mementos[index].get_state()
