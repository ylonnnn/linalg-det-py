# Linear Algebra Matrix Determinant Calculator

Matrix Determinant Calculator for Linear Algebra

### Usage

Use the constructor functions below from the `Matrix` class for matrix construction:

**`.from_size(m: int, n: int)`**

- Construct a zero matrix of the given dimension `m x n`.

```py
# example.py

# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
A = Matrix.from_size(3, 4)

```

**`.from_rows(rows: list[Vector])`**
`where Vector = list[float]`
**`.from_rows(rows: list[list[float]])`**

- Constructs a matrix from the provided list of row vectors.

```py
# example.py

#  1  2  0
# -1  1 -3
#  0 -2  1
A = Matrix.from_rows([
    [1, 2, 0],
    [-1, 1, -3],
    [0, -2, 1],
])

```

**NOTE**: May raise an error if the provided list of row vectors do not have uniform length.

**`.from_cols(cols: list[Vector])`**
`where Vector = list[float]`
**`.from_cols(cols: list[list[float]])`**

- Constructs a matrix from the provided list of column vectors.

```py
# example.py

# 1 4 7
# 2 5 8
# 3 6 9
A = Matrix.from_cols([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

```

**NOTE**: May raise an error if the provided list of column vectors do not have uniform length.

#### Determinant

To retrieve the determinant of a `Matrix`:

**`.numpy_det() -> float`**

- Uses `numpy.linalg.det()` which is faster as it uses a faster algorithm than cofactor expansion.

**`.cofactor_expansion() -> float`**

- Uses **Cofactor Expansion** to calculate the determinant of a matrix. Expected to be slow for large matrices.
