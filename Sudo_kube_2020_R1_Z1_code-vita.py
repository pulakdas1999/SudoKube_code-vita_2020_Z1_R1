def rot_90_clock(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    return A

def rot_90_anti_or_180(A, str):
    # Transpose
    for i in range(3):
        for j in range(i, 3):
            t = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = t
    # Reverse Columns
    for i in range(3):
        j = 0
        k = 2
        while j < k:
            t = A[j][i]
            A[j][i] = A[k][i]
            A[k][i] = t
            j += 1
            k -= 1
    if str == '-90':
        return A
    elif str == '180':
        # Transpose
        for i in range(3):
            for j in range(i, 3):
                t = A[i][j]
                A[i][j] = A[j][i]
                A[j][i] = t
        # Reverse Columns
        for i in range(3):
            j = 0
            k = 2
            while j < k:
                t = A[j][i]
                A[j][i] = A[k][i]
                A[k][i] = t
                j += 1
                k -= 1
    return A

def my_function(L, U, R, D, str):
    if str == '90':
        a = R[0][0]
        b = R[1][0]
        c = R[2][0]

        R[0][0] = U[2][0]
        R[1][0] = U[2][1]
        R[2][0] = U[2][2]

        U[2][0] = L[2][2]
        U[2][1] = L[1][2]
        U[2][2] = L[0][2]

        L[0][2] = D[0][0]
        L[1][2] = D[0][1]
        L[2][2] = D[0][2]

        D[0][0] = c
        D[0][1] = b
        D[0][2] = a
    if str == '-90':
        a = R[0][0]
        b = R[1][0]
        c = R[2][0]

        R[0][0] = D[0][2]
        R[1][0] = D[0][1]
        R[2][0] = D[0][0]

        D[0][0] = L[0][2]
        D[0][1] = L[1][2]
        D[0][2] = L[2][2]

        L[0][2] = U[2][2]
        L[1][2] = U[2][1]
        L[2][2] = U[2][0]

        U[2][0] = a
        U[2][1] = b
        U[2][2] = c
    if str == '180':
        a = R[0][0]
        b = R[1][0]
        c = R[2][0]

        R[0][0] = L[2][2]
        R[1][0] = L[1][2]
        R[2][0] = L[0][2]

        L[2][2] = a
        L[1][2] = b
        L[0][2] = c

        a = U[2][0]
        b = U[2][1]
        c = U[2][2]

        U[2][0] = D[0][2]
        U[2][1] = D[0][1]
        U[2][2] = D[0][0]

        D[0][0] = c
        D[0][1] = b
        D[0][2] = a
    return L, U, R, D

D = []
U = []
L = []
F = []
R = []
B = []
for x in range(0,3):
    a, b, c = map(int, input().split())
    D.append([a, b, c])
for x in range(0,3):
    a, b, c = map(int, input().split())
    U.append([a, b, c])
for x in range(0,3):
    a, b, c = map(int, input().split())
    L.append([a, b, c])
for x in range(0,3):
    a, b, c = map(int, input().split())
    F.append([a, b, c])
for x in range(0,3):
    a, b, c = map(int, input().split())
    R.append([a, b, c])
for x in range(0,3):
    a, b, c = map(int, input().split())
    B.append([a, b, c])
moves = list(map(str, input().split()))
print("D=", D, "U=", U, "L=", L, "F=", F, "R=", R, "B=", B, sep="\n")
print()
for x in moves:
    if 'F' in x:
        if "'" in x:
            F = rot_90_anti_or_180(F, '-90')
            L, U, R, D = my_function(L, U, R, D, '-90')
        elif "2" in x:
            F = rot_90_anti_or_180(F, '180')
            L, U, R, D = my_function(L, U, R, D, '180')
        else:
            F = rot_90_clock(F)
            L, U, R, D = my_function(L, U, R, D, '90')

    if 'L' in x:
        U = rot_90_anti_or_180(U, '-90')
        D = rot_90_clock(D)
        if "'" in x:
            L = rot_90_anti_or_180(L, '-90')
            B, U, F, D = my_function(B, U, F, D, '-90')
        elif "2" in x:
            L = rot_90_anti_or_180(L, '180')
            B, U, F, D = my_function(B, U, F, D, '180')
        else:
            L = rot_90_clock(L)
            B, U, F, D = my_function(B, U, F, D, '90')
        U = rot_90_clock(U)
        D = rot_90_anti_or_180(D, '-90')

    if 'R' in x:
        D = rot_90_anti_or_180(D, '-90')
        U = rot_90_clock(U)
        if "'" in x:
            R = rot_90_anti_or_180(R, '-90')
            F, U, B, D = my_function(F, U, B, D, '-90')
        elif "2" in x:
            R = rot_90_anti_or_180(R, '180')
            F, U, B, D = my_function(F, U, B, D, '180')
        else:
            R = rot_90_clock(R)
            F, U, B, D = my_function(F, U, B, D, '90')
        D = rot_90_clock(D)
        U = rot_90_anti_or_180(U, '-90')

    if 'B' in x:
        D = rot_90_anti_or_180(D, '180')
        U = rot_90_anti_or_180(U, '180')
        if "'" in x:
            B = rot_90_anti_or_180(B, '-90')
            R, U, L, D = my_function(R, U, L, D, '-90')
        elif "2" in x:
            B = rot_90_anti_or_180(B, '180')
            R, U, L, D = my_function(R, U, L, D, '180')
        else:
            B = rot_90_clock(B)
            R, U, L, D = my_function(R, U, L, D, '90')
        D = rot_90_anti_or_180(D, '180')
        U = rot_90_anti_or_180(U, '180')

    if 'U' in x:
        L = rot_90_clock(L)
        R = rot_90_anti_or_180(R, '-90')
        B = rot_90_anti_or_180(B, '180')
        if "'" in x:
            U = rot_90_anti_or_180(U, '-90')
            L, B, R, F = my_function(L, B, R, F, '-90')
        elif "2" in x:
            U = rot_90_anti_or_180(U, '180')
            L, B, R, F = my_function(L, B, R, F, '180')
        else:
            U = rot_90_clock(U)
            L, B, R, F = my_function(L, B, R, F, '90')
        L = rot_90_anti_or_180(L, '-90')
        R = rot_90_clock(R)
        B = rot_90_anti_or_180(B, '180')

    if 'D' in x:
        R = rot_90_clock(R)
        L = rot_90_anti_or_180(L, '-90')
        B = rot_90_anti_or_180(B, '180')
        if "'" in x:
            D = rot_90_anti_or_180(D, '-90')
            L, F, R, B = my_function(L, F, R, B, '-90')
        elif "2" in x:
            D = rot_90_anti_or_180(D, '180')
            L, F, R, B = my_function(L, F, R, B, '180')
        else:
            D = rot_90_clock(D)
            L, F, R, B = my_function(L, F, R, B, '90')
        R = rot_90_anti_or_180(R, '-90')
        L = rot_90_clock(L)
        B = rot_90_anti_or_180(B, '180')
print("D=", D, "U=", U, "L=", L, "F=", F, "R=", R, "B=", B, sep="\n")