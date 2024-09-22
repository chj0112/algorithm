def prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, int(x ** (1 / 2)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
num = list(map(int, input().split()))
result = 0
for i in num:
    if prime(i):
        result += 1
print(result)