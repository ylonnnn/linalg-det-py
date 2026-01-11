import numpy as np
from typing import Self, TypeVar

from linalg.matrix_error import NonUniformVectorLengthError, NonSquareMatrixError

T = TypeVar("T")


type Vector = list[float]


class Matrix:
    m: int
    n: int

    data: list[list[float]]

    @classmethod
    def from_size(cls, m: int, n: int) -> Self:
        return cls([[0.0 for _ in range(0, n)] for _ in range(0, m)])

    @classmethod
    def from_rows(cls, rows: list[Vector]) -> Self:
        return cls(rows)

    @classmethod
    def from_cols(cls, cols: list[Vector]) -> Self:
        n = cols.__len__()
        m = 0

        if n != 0:
            m = cols[0].__len__()
            if not all(len(data) == m for data in cols):
                raise NonUniformVectorLengthError(m)

        inst = cls.from_size(m, n)
        inst.data = [[cols[j][i] for j in range(0, n)] for i in range(0, m)]

        return inst

    """
    Initializes a matrix with the provided `data`.
    
    NOTE: Raises an error if the length of the vectors are not uniform

    """

    def __init__(self, data: list[Vector]) -> None:
        super().__init__()

        self.m, self.n = data.__len__(), 0

        # Uniform length validation
        if self.m != 0:
            if data[0]:
                self.n = data[0].__len__()
                if not all(len(data) == self.n for data in data):
                    raise NonUniformVectorLengthError(self.n)

            else:
                self.n = 0

        self.data = data

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        _str = "\n".join("".join("\t" + str(x) for x in row) for row in self.data)
        return f"[ {self.m}x{self.n}\n{_str}\n]"

    def column(self, j: int) -> Vector | None:
        return None if j < 0 or j >= self.n else [row[j] for row in self.data]

    def is_square(self) -> bool:
        return self.m == self.n

    def cofactor_expansion(self) -> float:
        if not self.is_square():
            raise NonSquareMatrixError((self.m, self.n))

        n = self.n
        if n == 0:
            return 1
        elif n == 1:
            return self.data[0][0]
        elif n == 2:
            # ad - bc
            data = self.data
            return (data[0][0] * data[1][1]) - (data[0][1] * data[1][0])
        else:
            top = self.data[0]
            det: float = sum(
                [
                    (1 if i % 2 == 0 else -1)  # Cofactor
                    * top[i]
                    * Matrix.from_rows(
                        [  # Minor Matrix Data
                            [self.data[r][c] for c in range(n) if c != i]
                            for r in range(1, n)
                        ]
                    ).cofactor_expansion()
                    for i in range(n)
                    if top[i] != 0
                ]
            )

            return det

    def numpy_det(self) -> float:
        if not self.is_square():
            raise NonSquareMatrixError((self.m, self.n))

        # NOTE: n = 0 and n = 1 are handled manually as numpy does not handle them
        # Conventionally, empty matrices have a determinant of 1 (according to some sources)
        if self.n == 0:
            return 1

        # Determinant of a single-dimensional matrix is the only entry it contains
        elif self.n == 1:
            return self.data[0][0]

        return np.linalg.det(np.array(self.data))
