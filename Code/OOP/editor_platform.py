from care_taker import Caretaker
from editor import Editor

if __name__ == '__main__':
    #print("input a word")
    #first_input = input()
    editor = Editor("eerste input")

    caretaker = Caretaker(editor)
    caretaker.backup()
    editor.type_word("tweede input")
    caretaker.backup()
    editor.type_word("derde input")
    caretaker.backup()
    editor.type_word("vierde input")
    caretaker.backup()
    print(f"{caretaker.get_old_input(0)}, {caretaker.get_old_input(1)}, {caretaker.get_old_input(2)}, {caretaker.get_old_input(3)}")