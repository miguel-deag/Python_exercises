def PlusMinus(arr):
    pos, neg, zero = 0, 0, 0
    for i in range(len(arr)):
        if arr[i] > 0: # número positivo
            pos += 1
        elif arr[i] < 0: # numero negativo
            neg += 1
        else:
            zero += 1
    #print(pos,neg,zero)
    pos /= len(arr)
    neg /= len(arr)
    zero /= len(arr)
    print(f'{pos:.6f}\n{round(neg, 6)}\n{round(zero, 6)}')


arr = [-4, 3, -9, 0, 4, 1]

PlusMinus(arr)