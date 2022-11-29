from typing import Optional

from Helpers.ConsoleHelper import ConsoleHelper
from Helpers.MatrixHelper import MatrixHelper
from Helpers.MenuHelper import MenuHelper
from os import path

from Matrix import Matrix


class Menu:
    # __matrixFilePath = path.join('macierz.txt')
    __leftBlockSize = 0
    __menuOptions = [1, 2, 3, 4, 5, 6]
    __lines = [
        f"Menu: (Wyjście -> CTRL+C)",
        f"1. A=B    -> Przyrównanie",
        f"2. A=(-B) -> Sprawdzenie przeciwności",
        f"3. C=A+B  -> Suma",
        f"4. C=A-B  -> Róznica",
        f"5. C=A*B  -> Iloczyn",
        f"6.        -> Transponowanie macierzy"
    ]
    __experimentalOptions = [
        f"7.        -> Sprawdzanie osobliwości/detA/itd."
    ]

    def __init__(self, filePath: Optional[bytes | str] = None, enableExperimental: bool = False, preMatrix: Optional[Matrix] = None):
        if filePath:
            self.matrix = MenuHelper.loadMatrixFromFile(filePath)
        else:
            self.matrix = preMatrix
        if enableExperimental:
            for idx, x in enumerate(self.__experimentalOptions):
                self.__menuOptions.append(len(self.__menuOptions)+idx+2)
                self.__lines.append(x)
            print("\033[31mTryb eksperymentalny XD\nAle tak całkiem poważnie, ja nie odpowiadam za to co sie tu może stać.\nTo jest ten moment w którym rzuciłem laptopem o ściane.\nJak wywali błędy to ostrzegałem :)\033[0m")
        self.generate()

    def generate(self):
        ConsoleHelper.clear()
        matrixContent = ("Wczytana macierz:\n"+str(self.matrix)).split("\n")
        loadedMatrixTextSize, rowSize, lastIndex = len(list(matrixContent[0])), len(list(matrixContent[1])), 0
        for idx, row in enumerate(matrixContent):
            if idx == 0:
                if loadedMatrixTextSize < rowSize:
                    self.__leftBlockSize = rowSize
                    row += " "*(rowSize-loadedMatrixTextSize)
            elif loadedMatrixTextSize > rowSize:
                self.__leftBlockSize = loadedMatrixTextSize
                row += " " * (loadedMatrixTextSize-rowSize)
            print(f"\t{row}\t\t|\t\t{self.__lines[idx] if idx < len(self.__lines) else ''}")
            lastIndex = idx
        if len(matrixContent) < len(self.__lines):
            while lastIndex < len(self.__lines) - 1:
                lastIndex += 1
                print(f"\t{' ' * (rowSize + (loadedMatrixTextSize-rowSize if loadedMatrixTextSize > rowSize else 0))}\t\t|\t\t{self.__lines[lastIndex]}")
        self.__handleInput()

    def __handleInput(self):
        inp = input(" "*self.__leftBlockSize+"\t\t\t|\t\tWybór: ")
        try:
            inp = int(inp)
            if inp not in self.__menuOptions:
                self.generate()
                return
            ConsoleHelper.clear()
            if inp == 1 or inp == 2 or inp == 3 or inp == 4:
                B = MatrixHelper.inputMatrix(self.matrix.size)
                if not B:
                    print("Podano nieprawidłową macierz.")
                else:
                    if inp == 1:
                        print(f"{'-'*10}\nWynik: \n"
                              f"Podane macierze {'są takie same' if MatrixHelper.compare(self.matrix, B) else 'nie są takie same'}.")
                    elif inp == 2:
                        print(f"{'-'*10}\nWynik:\n"
                              f"Podane macierze {'są przeciwne' if MatrixHelper.isOpposite(self.matrix, B) else 'nie są przeciwne'}.")
                    elif inp == 3:
                        print(f"{'-'*10}\nWynik:\n"
                              f"{str(MatrixHelper.getTotality(self.matrix, B))}")
                    elif inp == 4:
                        print(f"{'-'*10}\nWynik:\n"
                              f"{str(MatrixHelper.getDifference(self.matrix, B))}")
            elif inp == 6:
                print(f"Wynik:\n"
                      f"{MatrixHelper.getTransposed(self.matrix)}")
            elif inp == 7:
                raise Exception("Not implemented.")
            else:
                B = MatrixHelper.inputMatrix()
                if inp == 5:
                    res = MatrixHelper.getProduct(self.matrix, B)
                    if not res:
                        print("Ilośc kolumn wpisanej macierzy musi być równa ilości wierszy macierzy wczytanej.")
                    else:
                        print(f"{'-'*10}\nWynik:\n"
                              f"{str(res)}")
            self.__waitForAction()
        except ValueError:
            self.generate()

    def __waitForAction(self):
        input("Nacisnij \033[4mENTER\033[0m by wrócić do menu.")
        self.generate()
