line = list(input())
n = 0
while line:
    n += 1
    str_n = str(n)
    if line[0] in str_n:
        str_n = str_n[str_n.index(line.pop(0)) + 1:]
        for i in str_n:
            if line:
                if line[0] == i:
                    str_n = str_n[str_n.index(line.pop(0)) + 1:]
print(n)