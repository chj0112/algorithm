t = int(input())
for i in range(t):
    n = int(input())
    max = 0
    school = ''
    for j in range(n):
        s, l = input().split()
        l = int(l)
        if max < l:
            max = l
            school = s
    print(school)