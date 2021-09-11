def func(matrix):
    for stroka in matrix:
        stroka /= stroka[0]
    for stroka in matrix[1:]:
        stroka -= matrix[0]