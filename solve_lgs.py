def string_to_matrix(matrix):
    # returns matrix in list statt string input
    # sodass kann man die Operationen machen.
        return [[int(x) for x in M1.split()] for M1 in matrix.split(",")]

def LU_decomposition(A):
    #diese funktion teilt die gegebene Matrix
    #in LU-Zerlegung.
    M=string_to_matrix(A)
    n=len(M)
    L= [[0]* n for _ in range(n) ]
    #leere  matrix in laenge der original matrix

    for i in range(n):
        L[i][i]=1
        #diagonal 1

    for k in range(n):
        for i in range(k+1,n):
            if M[k][k] == 0:
                return "ZeroDivisionError"
            factor = M[i][k] / M[k][k]
            #finden die factor, um die
            #erste elemente von untere row
            # null zu machen

            L[i][k] = factor
            # factor in die Lower Matrix addieren.

            for j in range(k,n):
                M[i][j] -= factor * M[k][j]
                # row operation.

    i=0
    j=0

    for i in range(n):
        for j in range(i,n):
            L[i][j]=M[i][j]

    #um die ausgabe wie beschriebenen String form zurueckzugeben.

    matrix_to_string = ', '.join([' '.join([f'{int(round(val))}' for val in row]) for row in L])

    return matrix_to_string

def LU_solo(A):
    '''
    Diese Funktion ist ganz genau mit obene LU_decomposition funktion.
    Aber weil in die LU_decomposition Funktion ist es erwartet, dass
    die Ausgaben in String zurueckzugeben, deswegen habe ich also diese
    Funktion geschrieben.

    Einzige Unterschiede ist dass hier keinen matrix_to_string gibt.
    '''
    M=string_to_matrix(A)
    n=len(M)
    L= [[0]* n for _ in range(n) ]

    for i in range(n):
        L[i][i]=1

    for k in range(n):
        for i in range(k+1,n):
            if M[k][k] == 0:
                return "ZeroDivisionError"
            factor = M[i][k] / M[k][k]

            L[i][k] = factor

            for j in range(k,n):
                M[i][j] -= factor * M[k][j]

    return M,L

def solve_LGS(A,B):
    '''
    Diese funktion loest die LGS, also
    A* xi= bi {i€ 1,...,k} der i-ten Spalte der
    Matrix B.
    '''

    Upper,Lower=LU_solo(A)
    B=string_to_matrix(B)
    n=len(Lower)
    # die Groeße der Matrix.

    x = [[0] * len(B[0]) for _ in range(n)]
    y = [[0] * len(B[0]) for _ in range(n)]

    #A*x = B
    # A= L*U
    # L*U*x= B
    # U*x=y
    # L*y= B

    # Loest L*y=B mithilfe der Vorwaertssubstitution
    for col in range(len(B[0])):
        for row in range(n):
            y[row][col] = B[row][col]
            for k in range(row):
                y[row][col] -= Lower[row][k] * y[k][col]
                #multiplikation von Spalten mit Row.


    # U*x= y mithilfe der Rueckwartssubstitution
    ''' U Beispiel:
        1 1 1
        0 1 1
        0 0 1
    '''

    for col in range(len(B[0])):
        for row in reversed(range(n)):
            x[row][col] = y[row][col]
            for k in range(row + 1, n):
                x[row][col] -= Upper[row][k] * x[k][col]
            if Upper[row][row]==0:
                pass
            else:
                x[row][col] /= Upper[row][row]

    #um die ausgabe wie beschriebenen String form zurueckzugeben.
    matrix_to_string = ', '.join([' '.join([f'{int(round(val))}' for val in row]) for row in x])

    return matrix_to_string
