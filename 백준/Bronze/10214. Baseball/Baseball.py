t = int(input())
for i in range(t):
    yonsei, korea = 0, 0
    for i in range(9):
        y, k = map(int, input().split())
        yonsei += y
        korea += k
    if yonsei > korea:
        print("Yonsei")
    elif yonsei < korea:
        print("Korea")
    else:
        print("Draw")