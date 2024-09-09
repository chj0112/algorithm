import sys
input = sys.stdin.readline

n = int(input())
seq = [int(input()) for _ in range(n)]
stack = []
num = 0
result = []
for i in seq:
    while i > num:
        num += 1
        stack.append(num)
        result.append('+')
    if stack.pop() == i:
        result.append('-')
    else:
        print("NO")
        exit()
print('\n'.join(result))