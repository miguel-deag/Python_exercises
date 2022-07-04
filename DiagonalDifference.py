def DiagonalDifference(arr):
    sumaizq, sumader = 0, 0

    # Diagonal Izquierda
    i, j = 0, 0
    while (i < len(arr)):
        sumaizq += arr[i][j]
        #print(arr[i][j])
        i += 1
        j += 1
    print(sumaizq)

    #Diagonal Derecha
    i = 0
    j = len(arr) - 1
    while ((i < len(arr))):
        sumader += arr[i][j]
        #print(arr[i][j])
        i += 1
        j -= 1
    print(sumader)

    return abs(sumader-sumaizq)


    #     0 1 2
lista = [[1,2,3], # 0
         [4,5,6], # 1
         [7,8,9]] # 2

'''
print(lista[0][0])
print(lista[1][1])
print(lista[2][2])
'''

print(DiagonalDifference(lista))






