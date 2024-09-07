import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
dict = {}
for i in arr1:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
for i in arr2:
    print(dict[i] if i in dict else 0, end=' ')