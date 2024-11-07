import math

n = int(input())
arr = [0, 0] + [1] * (n - 1)
prime = []
for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == 1:
        for j in range(i * 2, n + 1, i):
            arr[j] = 0
for i in range(len(arr)):
    if arr[i] == 1:
        prime.append(i)
start = 0
end = 1
result = 0
while end <= len(prime):
    num = sum(prime[start:end])
    if num == n:
        result += 1
        start += 1
        end += 1
    elif num > n:
        start += 1
    elif num < n:
        end += 1
print(result)