import random
arr = []
sum = 8
while sum != 0:
    sum = 0
    arr = []
    for i in range(4):
        a = random.randint(-5, 5)
        sum = sum + a
        arr.append(a)
print(arr)