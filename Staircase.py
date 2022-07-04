def Staircase(n):
    for row in range(n): # Por cada fila
        for s in range(n-row-1): # range --> 3; 2; 1; 0;
            '''
            s=0 --> En un rango de 3 imprime ' '
            s=1 --> En un rango de 2 imprime ' ' 
            s=2 --> En un rango de 1 imprime ' ' 
            s=3 --> En un rango de 0 imprime ' ' 
            '''
            print('1', end='')

        for colum in range(row+1): # Por cada columna
           print('#', end='')
        print()

Staircase(4)