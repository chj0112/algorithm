w = input()
for i in range(len(w) // 2):
    if w[i] != w[len(w) - i - 1]:
        print(0)
        exit()
print(1)