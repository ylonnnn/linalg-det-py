class MatrixError(RuntimeError):
    pass


class NonUniformVectorLengthError(MatrixError):
    def __init__(self, len: int) -> None:
        super().__init__(f"expected length of all vectors: {len}")


class NonSquareMatrixError(MatrixError):
    def __init__(self, dim: tuple[int, int]) -> None:
        super().__init__(f"non-square matrix provided with dimension {dim[0]}x{dim[1]}")
