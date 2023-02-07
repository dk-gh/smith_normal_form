import numpy as np
from itertools import product


def swap_rows(i0, i1, A):
    A[[i0, i1], :] = A[[i1, i0], :]


def swap_columns(j0, j1, A):
    A[:, [j0, j1]] = A[:, [j1, j0]]


def smith_normal_form(A):
    number_of_rows, number_of_columns = A.shape
    n = 0
    while n < min(number_of_columns, number_of_rows):
        for i, j in product(
            range(n, number_of_rows),
            range(n, number_of_columns)
        ):

            if A[i, j] == 1:
                swap_rows(n, i, A)
                swap_columns(n, j, A)
                break

        for i in range(n+1, number_of_rows):
            if A[i, n] == 1:
                A[i] = A[i] ^ A[n]

        for j in range(n+1, number_of_columns):
            if A[n, j] == 1:
                A[:, [j]] = A[:, [j]] ^ A[:, [n]]
        n = n+1

    return A


if __name__ == '__main__':

    X = np.array(
        [
            [0, 1, 1, 0],
            [1, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 1]
        ]
    )

    snf = smith_normal_form(X)
    print(snf)
