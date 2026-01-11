from linalg import Matrix
from random import randint


def main() -> None:
    while True:
        n = int(input("n: "))

        A = Matrix.from_cols(
            [[float(randint(-4, 4)) for _ in range(n)] for _ in range(n)]
        )

        print(
            f"A = {A}\n[numpy] det(A) = {A.numpy_det()}\n[cof_exp] det(A) = {A.cofactor_expansion()}"
        )


if __name__ == "__main__":
    main()
