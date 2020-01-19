def add():
    sum=0
    for i in range(0,n):
        sum+=arr[i]
    return sum
from random import randint as rd

arr=[rd(1,10) for i in range(100)]
n=10
print(add())