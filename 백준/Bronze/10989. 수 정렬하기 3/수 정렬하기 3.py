import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(10001)]
for i in range(n):
    arr[int(input())] += 1
for j in range(len(arr)):
    if arr[j] != 0:
        for k in range(arr[j]):
            sys.stdout.write(str(j) + '\n')