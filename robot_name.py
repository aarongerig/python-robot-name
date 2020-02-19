from string import ascii_uppercase, digits
from random import choices


class Robot:
    def __init__(self):
        self.name = self.__generate_name()

    def reset(self):
        while True:
            new_name = self.__generate_name()
            if new_name != self.name:
                break

        self.name = new_name

    @staticmethod
    def __generate_name():
        return ''.join(choices(ascii_uppercase, k=2) + choices(digits, k=3))
