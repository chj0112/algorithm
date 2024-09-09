def is_vps(string):
    stack = []
    for i in string:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return "NO"
    return "NO" if stack else "YES"

t = int(input())
for i in range(t):
    string = input()
    print(is_vps(string))