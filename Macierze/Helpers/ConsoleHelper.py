from os import name, system


class ConsoleHelper:
    @staticmethod
    def clear():
        if name == "nt":
            _ = system('cls')
        else:
            system('clear')
