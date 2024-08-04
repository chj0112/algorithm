while True:
    n = int(input())
    if n == -1:
        break
    d = [1]
    for i in range(2, n // 2 + 1):
        if i in d:
            break
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n // i)
    d.sort()
    sum = 0
    s = ''
    for j in d:
        sum += j
        s = s + str(j) + " + "
    if n == sum:
        print("{} = {}".format(n, s.rstrip(" + ")))
    else:
        print("{} is NOT perfect.".format(n))