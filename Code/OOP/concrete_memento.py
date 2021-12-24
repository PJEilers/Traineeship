from memento import *

class ConcreteMemento(Memento):
    def __init__(self, state: str):
        self._state = state

    def get_state(self):
        return self._state
