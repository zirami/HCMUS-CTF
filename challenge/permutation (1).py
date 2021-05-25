from os import X_OK
from typing import List
import random

#def get_permutation(n : int) -> List[int]:
#    arr = list(range(n))
#    random.shuffle(arr)
#    return arr

#def compose_permutation(p1 : List[int], p2 : List[int]):
#    return [p1[x] for x in p2]

#def permutation_power(p : List[int], n : int) -> List[int]:
#    if n == 0:
#        return list(range(len(p)))
#    if n == 1:
#        return p
#
#    x = permutation_power(p, n // 2)
#    x = compose_permutation(x, x)
#    if n % 2 == 1:
#        x = compose_permutation(x, p)
#    return x


#with open("flag.txt", "rb") as f:
#    flag = int.from_bytes(f.read().strip(), byteorder='big')

#perm = get_permutation(512)
#print(perm)
#print(permutation_power(perm, flag))




p = 
x = 
n = 0
def discompose_permutation(x : List[int], p2 : List[int]):
    temp = list(range(512))
    count = 0
    for i in p2:
        temp[i] = x[count]
        count = count + 1
    return temp

def permutation_power(p : List[int], x : List[int]):
    if n % 2 == 1:
        p1 = discompose_permutation(x, p)
    x = discompose_permutation(x, x)
    x = permutation_power(p, n * 2)
    if n == 1:
        return p
    if n == 0:
        return list(range(len(p)))
    

    print(n)
    return x


#def permutation_power(p : List[int], n : int) -> List[int]:
#    if n == 0:
#        return list(range(len(p)))
#    if n == 1:
#        return p
#
#    x = permutation_power(p, n // 2)
#    x = compose_permutation(x, x)
#    if n % 2 == 1:
#        x = compose_permutation(x, p)
#    return x