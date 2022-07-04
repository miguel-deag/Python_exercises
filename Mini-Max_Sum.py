# functio without methods
def Mini_Max_Sum(arr):
    min = arr[0]
    max = arr[0]
    for elemento in arr:
        if min >= elemento:
          min = elemento
        elif max <= elemento:
            max = elemento
    print(f'Minimo: {min}\nMáximo: {max}')
    suma_min, suma_max = 0, 0
    for i in arr:
        suma_min += i
        suma_max += i
    suma_min -= max
    suma_max -= min
    print(f'Suma minimos: {suma_min}\nSuma maximos: {suma_max}')

# function with methods
def Min_max(arr):
    suma = sum(arr)
    print(f'{suma - max(arr)}, {suma - min(arr)}') # Min, Max


arr = [1, 2, 3, 4, 5]
#arr = [5,4,9,3,4,7,20]
Mini_Max_Sum(arr)
Min_max(arr)