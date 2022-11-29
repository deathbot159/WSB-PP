from typing import Optional

from Macierze.Matrix import Matrix, MatrixSizeHelper


class MatrixHelper:

    @staticmethod
    def inputMatrix(addSize: Optional[MatrixSizeHelper] = None):
        res = None
        if not addSize:
            res = Matrix()
            inp = input("Podaj wielkosc macierzy w formacie: XxY (np. 3x2): ")
            splited = inp.split("x")
            if len(splited) != 2:
                print("Nie poprawna wielkość macierzy.")
                return None
            try:
                res.size(int(splited[0]), int(splited[1]))
            except ValueError:
                print("Nie poprawne wartości wielkości macierzy.")
                return None
        else:
            res = Matrix(size=addSize)
            print(f"Podaj wiesze macierzy o wielkości {res.size.x}x{res.size.y}.")
        sl = []
        res.content = []
        for i in range(1, res.size.x + 1):
            if i == 1:
                print("Wiersze podawaj w postaci liczb przedzielonych przecinkiem.\nNp. 1,2.75,3,4.5")
            inp = input(f"Wiersz {i}: ")
            inp = inp.split(",")
            if len(inp) != res.size.y:
                print("Podano za dużo lub za mało elementów w wierszu.")
                return None
            for n in inp:
                try:
                    sl.append(float(n))
                except ValueError:
                    print("Nie prawidłowa wartość!")
                    return None
            res.content.append(sl)
            sl = []
        return res

    @staticmethod
    def compare(A: Matrix, B: Matrix) -> bool:
        return A == B

    @staticmethod
    def getTotality(A: Matrix, B: Matrix) -> Matrix:
        C = Matrix(size=A.size)
        for i in range(len(A.content)):
            l = []
            rowA = A.getRow(i)
            rowB = B.getRow(i)
            for idx in range(len(rowA)):
                l.append(rowA[idx] + rowB[idx])
            C.replaceRow(i, l)
        return C

    @staticmethod
    def isOpposite(A: Matrix, B: Matrix) -> bool:
        for i in range(len(A.content)):
            for j in range(len(A.getRow(i))):
                if A.getByPosition(i, j) + B.getByPosition(i, j) != 0:
                    return False
        return True

    @staticmethod
    def getProduct(A: Matrix, B: Matrix) -> Matrix | None:
        if A.size.y != B.size.x:
            return None
        C = Matrix(size=MatrixSizeHelper(A.size.x, B.size.y))
        for i in range(C.size.x):
            for j in range(C.size.y):
                for k in range(A.size.y):
                    C.content[i][j] += A.getByPosition(i, k)*B.getByPosition(k, j)
        return C

    @staticmethod
    def getDifference(A: Matrix, B: Matrix) -> Matrix:
        C = Matrix(size=A.size)
        for i in range(C.size.x):
            for j in range(C.size.y):
                C.putInPosition(i, j, (A.getByPosition(i, j) - B.getByPosition(i, j)))
        return C

    @staticmethod
    def getTransposed(A: Matrix) -> Matrix:
        C = Matrix(size=MatrixSizeHelper(A.size.y, A.size.x))
        for i in range(A.size.x):
            for j in range(A.size.y):
                C.putInPosition(j, i, A.getByPosition(i, j))
        return C
