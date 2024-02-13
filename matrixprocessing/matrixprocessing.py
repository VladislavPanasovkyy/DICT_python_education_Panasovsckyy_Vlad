import numpy as np

def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")

        choice = int(input("Your choice: > "))

        if choice == 1:
            add_matrices()
        elif choice == 2:
            multiply_matrix_by_constant()
        elif choice == 3:
            multiply_matrices()
        elif choice == 4:
            transpose_matrix()
        elif choice == 5:
            calculate_determinant()
        elif choice == 6:
            inverse_matrix()
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def add_matrices():
    rowsA, colsA = map(int, input("Enter size of first matrix: > ").split())
    matrixA = read_matrix(rowsA, colsA)

    rowsB, colsB = map(int, input("Enter size of second matrix: > ").split())
    matrixB = read_matrix(rowsB, colsB)

    if rowsA == rowsB and colsA == colsB:
        result = [[matrixA[i][j] + matrixB[i][j] for j in range(colsA)] for i in range(rowsA)]
        print("The result is:")
        print_matrix(result)
    else:
        print("The operation cannot be performed.")


def multiply_matrix_by_constant():
    rows, cols = map(int, input("Enter size of matrix: > ").split())
    matrix = read_matrix(rows, cols)

    constant = float(input("Enter constant: > "))
    result = [[element * constant for element in row] for row in matrix]

    print("The result is:")
    print_matrix(result)


def multiply_matrices():
    rowsA, colsA = map(int, input("Enter size of first matrix: > ").split())
    matrixA = read_matrix(rowsA, colsA)

    rowsB, colsB = map(int, input("Enter size of second matrix: > ").split())
    matrixB = read_matrix(rowsB, colsB)

    if colsA == rowsB:
        result = [[sum(matrixA[i][k] * matrixB[k][j] for k in range(colsA)) for j in range(colsB)] for i in range(rowsA)]
        print("The result is:")
        print_matrix(result)
    else:
        print("The operation cannot be performed.")


def transpose_matrix():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")

    transpose_option = int(input("Your choice: > "))
    rows, cols = map(int, input("Enter matrix size: > ").split())
    matrix = read_matrix(rows, cols)

    if transpose_option == 1:
        result = [[matrix[j][i] for j in range(cols)] for i in range(rows)]
    elif transpose_option == 2:
        result = [list(reversed(row)) for row in reversed(list(zip(*matrix)))]
    elif transpose_option == 3:
        result = [list(reversed(row)) for row in matrix]
    elif transpose_option == 4:
        result = list(reversed(matrix))
    else:
        print("Invalid transpose option. Returning to the main menu.")
        return

    print("The result is:")
    print_matrix(result)


def read_matrix(rows, cols):
    print("Enter matrix:")
    matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def calculate_determinant():
    rows, cols = map(int, input("Enter matrix size: > ").split())
    if rows != cols:
        print("The matrix must be square to calculate the determinant.")
        return

    matrix = read_matrix(rows, cols)
    determinant = np.linalg.det(matrix)
    print("The result is:", determinant)


def inverse_matrix():
    rows, cols = map(int, input("Enter matrix size: > ").split())
    matrix = read_matrix(rows, cols)

    if np.linalg.det(matrix) == 0:
        print("This matrix doesn't have an inverse.")
        return

    inverse_matrix = np.linalg.inv(matrix)
    print("The result is:")
    print_matrix(inverse_matrix)


if __name__ == "__main__":
    main()
