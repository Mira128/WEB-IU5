
import math
import sys
import argparse

def check_params():
    parser = argparse.ArgumentParser()
    parser.add_argument ('A', nargs='?', default="" )
    parser.add_argument ('B', nargs='?', default="" )
    parser.add_argument ('C', nargs='?', default="" )
    namespace = parser.parse_args(sys.argv[1:])
    #print (namespace)
    if namespace.A == "" or namespace.B == "" or namespace.C == "" :
        params = params_input()
    else :
        params = str_to_num(namespace.A, namespace.B, namespace.C)
    return params

def params_input():
    print("Ведите коэффициенты биквадратного уравнения:")
    str = input().split()
    if len(str) > 2 :
        strA = str[0]
        strB = str[1]
        strC = str[2]
        if (strA != None) & (strB != None) & (strC != None) :
            params = str_to_num(strA, strB, strC)
            return params
    else :
        params = params_input()
        return params


# проверка параметров командной строки
def str_to_num(A, B, C):
    if '.' in A and A.replace('.', '').isdigit():
        str2 = A.replace('-', '')
        if '-' in A2 and A2.replace('-', '').isdigit():
            params = [float(A2)]
        params = [float(A)]
    elif '-' in A and A.replace('-', '').isdigit():
            params = [float(A)]
    elif A.isdigit():
        params = [int(A)]
    else :
        params = params_input()
        return params

    if '.' in B and B.replace('.', '').isdigit():
        str2 = B.replace('-', '')
        if '-' in B2 and B2.replace('-', '').isdigit():
            params.append(float(B2))
        params.append(float(B))
    elif '-' in B and B.replace('-', '').isdigit():
            params.append(float(B))
    elif B.isdigit():
        params.append(int(B))
    else :
        params = params_input()
        return params

    if '.' in C and C.replace('.', '').isdigit():
        str2 = C.replace('-', '')
        if '-' in C2 and C2.replace('-', '').isdigit():
            params.append(float(C2))
        params.append(float(C))
    elif '-' in C and C.replace('-', '').isdigit():
            params.append(float(C))
    elif C.isdigit():
        params.append(int(C))
    else :
        params = params_input()
        return params
    return params

# решение биквадратного уравнения
def biquadratic_equation(A, B, C):
    D = pow(B, 2) - 4*A*C
    if D > 0 :
        X1 = (-B + math.sqrt(D))/ 2*A
        X2 = (-B - math.sqrt(D))/ 2*A
        print("Действительные корни уравнения:")
        print("X1= " + str(X1) + " " + "X2= " + str(X2))
    elif D == 0 :
        X = (-B + math.sqrt(D))/ 2*A
        print("Действительный корень уравнения:")
        print("X = " + str(X))
    else :
         print("Нет действительных корней уравнения :( ")

# начало программы
params = check_params()
A = params[0]
B = params[1]
C = params[2]
print("Коэффициенты биквадратного уравнения: ", params[0]," ", params[1], " ", params[2])
biquadratic_equation(A, B, C)



