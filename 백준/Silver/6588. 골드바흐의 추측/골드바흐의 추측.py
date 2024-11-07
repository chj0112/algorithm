import math, sys

num = []
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    num.append(n)
arr = [0, 0] + [1] * (max(num) - 1)
prime = []
for i in range(2, int(math.sqrt(max(num))) + 1):
    if arr[i] == 1:
        for j in range(i * 2, max(num) + 1, i):
            arr[j] = 0
for i in range(3, len(arr)):
    if arr[i] == 1:
        prime.append(i)
sprime = set(prime)
for i in num:
    for j in prime:
        if j > i / 2:
            print("Goldbach's conjecture is wrong.")
            break
        if i - j in sprime:
            print(f"{i} = {j} + {i - j}")
            break