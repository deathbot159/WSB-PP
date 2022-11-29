import sys

from Helpers.ConsoleHelper import ConsoleHelper
from Helpers.MatrixHelper import MatrixHelper
from Matrix import Matrix
from Menu import Menu
from os import path


def selection() -> Matrix | str:
    try:
        inp = int(input("Co chcesz zrobić?\n\t1.Podaj ścieżkę pliku.\n\t2.Wprowadź macierz.\n\tWybór: "))
        if inp in [1, 2]:
            if inp == 1:
                filePath = input("Podaj scieżkę do pliku (np. C:\\Users\\Jan\\Desktop\\macierz.txt): ")
                if not path.exists(filePath):
                    ConsoleHelper.clear()
                    print("Podana scieżka nie istnieje.\n\n")
                    selection()
                else:
                    return filePath
            elif inp == 2:
                return MatrixHelper.inputMatrix()
        else:
            ConsoleHelper.clear()
            print("Nie poprawny wybór.\n\n")
    except ValueError:
        ConsoleHelper.clear()
        print("Nie poprawny wybór.\n\n")


if __name__ == "__main__":
    try:
        sel = selection()
        if isinstance(sel, str):
            Menu(filePath=sel)
        else:
            Menu(preMatrix=sel)
    except KeyboardInterrupt:
        sys.exit(0)
