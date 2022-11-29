from copy import deepcopy
from typing import Optional


class MatrixSizeHelper:
    x: int = 0
    y: int = 0

    def __init__(self, x: Optional[int] = None, y: Optional[int] = None):
        if x:
            self.x = x
        if y:
            self.y = y

    def __call__(self, x: Optional[int] = None, y: Optional[int] = None):
        if x:
            self.x = x
        if y:
            self.y = y


class Matrix:
    size: MatrixSizeHelper = MatrixSizeHelper()
    content: list = []

    def __init__(self, size: Optional[MatrixSizeHelper] = None, content: Optional[list] = None):
        if size:
            self.size = size
            if not content:
                self.content = [[0] * self.size.y for i in range(self.size.x)]
        if content:
            self.content = content

    def __str__(self) -> str:
        return "\n".join(map(str, self.content))

    def __eq__(self, other: 'Matrix') -> bool:
        return self.content == other.content

    def isSquare(self) -> bool:
        return self.size.x == self.size.y

    def getByPosition(self, row: int, column: int):
        if row < 0 or column < 0:
            raise Exception(f"Podane wartości są ujemne.")
        if row > self.size.x - 1 or column > self.size.y - 1:
            raise Exception(f"Podane wartości wykraczają poza wielkość macierzy. ({row}x{column})")
        return self.content[row][column]

    def putInPosition(self, row: int, column: int, expr: float | int) -> 'Matrix':
        if row < 0 or column < 0:
            raise Exception(f"Podane wartości są ujemne.")
        if row > self.size.x - 1 or column > self.size.y - 1:
            raise Exception(f"Podane wartości wykraczają poza wielkość macierzy. ({row}x{column})")
        self.content[row][column] = expr
        return self

    def removeRow(self, row: int) -> 'Matrix':
        self.content.pop(row)
        self.size(x=self.size.x - 1)
        return self

    def addRow(self, nums: list[float | int]) -> 'Matrix':
        self.content.append(nums)
        self.size(x=self.size.x + 1)
        return self

    def replaceRow(self, idx: int, row: list[float | int]) -> 'Matrix':
        if idx < 0 or idx > self.size.x-1:
            raise Exception(f"Index {idx} is not included in Matrix size")
        self.content[idx] = row
        return self

    def getRow(self, idx: int):
        return self.content[idx]

    def getColumns(self):
        cols = [[0] * self.size.x for i in range(self.size.y)]
        for j in range(self.size.y):
            for i in range(len(self.content) - 1, -1, -1):
                cols[j][len(self.content) - 1 - i] = self.content[i][j]
        return cols

    def removeColumn(self, column) -> 'Matrix':
        for i in range(len(self.content)):
            self.content[i].pop(column)
        self.size(y=self.size.y - 1)
        return self

    def getCopyWithout(self, row: int, col: int) -> 'Matrix':
        return deepcopy(self).removeRow(row).removeColumn(col)
