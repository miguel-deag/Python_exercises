def AVeryBigSum(ar):
    suma = 0
    for elemento in ar:
        suma += elemento
    return suma

ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

print(AVeryBigSum(ar))