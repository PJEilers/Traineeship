from concrete_memento import ConcreteMemento
from memento import Memento


class Editor:

    _state = None

    def __init__(self, state: str):
        self._state = state

    def type_word(self, new_state):
        self._state = new_state

    def save(self) -> Memento:
        return ConcreteMemento(self._state)
