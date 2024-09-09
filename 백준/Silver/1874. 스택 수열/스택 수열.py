n = int(input())
seq = [int(input()) for _ in range(n)]
stack = []
num = 0
result = ""
for i in seq:
    while i > num:
        num += 1
        stack.append(num)
        result += '+\n'
    if stack.pop() == i:
        result += '-\n'
    else:
        print("NO")
        exit()
print(result)