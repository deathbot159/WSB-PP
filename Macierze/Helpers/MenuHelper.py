from Macierze.Matrix import Matrix, MatrixSizeHelper


class MenuHelper:
    @staticmethod
    def loadMatrixFromFile(path) -> Matrix:
        file = open(path, "r")
        reader = file.readlines()

        matrix = Matrix(MatrixSizeHelper(x=len(reader)))
        for idx, line in enumerate(reader):
            splited = line.split(" ")

            if idx == 0:
                matrix.size(y=len(splited))

            if len(splited) == 0:
                continue

            elif len(splited) != matrix.size.y:
                raise Exception(f"Niepoprawna długość znaków w linii {idx+1} względem linii 1. "
                                f"(Expected: {matrix.size.y}. Found: {len(splited)})")
            line = []
            for num in splited:
                try:
                    line.append(float(num.replace("\n", "")))
                except ValueError:
                    raise Exception(f"Odczytano znak niepoprawnego typu. (Expected: numeral types)")
            matrix.replaceRow(idx, line)
        return matrix
