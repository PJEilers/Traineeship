# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from abc import abstractmethod, ABC


class Voertuig(ABC):

    def __init__(self, kleur):
        self.kleur = kleur

    @abstractmethod
    def toeter(self):
        pass


class Auto(Voertuig):

    def __init__(self, kleur, type_versnellingsbak):
        super().__init__(kleur)
        self.type_versnellingsbak = type_versnellingsbak

    def toeter(self):
        print("TOET TOET")


    def afstand(self, snelheid):
        return lambda tijd: tijd * snelheid

class RaceAuto(Auto):

    def racen(self):
        print("VROEM VROEM")


class Bus(Voertuig):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    auto = Auto('rood', 'automaat')
    print(f"{auto.kleur=}, {auto.type_versnellingsbak=}")
    auto.toeter()
    afstand_berekener = auto.afstand(100)
    print(f"Afstand afgelegd is {afstand_berekener(60)} meter")
    #auto.racen()
    auto = RaceAuto(auto.kleur, auto.type_versnellingsbak)
    auto.racen()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
