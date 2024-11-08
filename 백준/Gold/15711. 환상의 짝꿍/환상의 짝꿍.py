s = int(2 * (10 ** 6)) + 1
arr = [0, 0] + [1] * (s - 1)
prime = set()
for i in range(2, s + 1):
    if arr[i] == 1:
        prime.add(i)
        for j in range(i + i, s + 1, i):
            arr[j] = 0

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a + b == 2:
        print("NO")
    elif (a + b) % 2 == 0:
        print("YES")
    elif a + b - 2 <= s:
        if a + b - 2 in prime:
            print("YES")
        else:
            print("NO")
    else:
        flag = False
        for i in prime:
            if (a + b - 2) % i == 0:
                flag = True
                print("NO")
                break
        if flag == False:
            print("YES")