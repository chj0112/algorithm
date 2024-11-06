def func(k, seq):
    for i in range(1, len(seq) // 2 + 1):
        if seq[-i :] == seq[-i * 2 : -i]:
            return
    if k == n:
        print(int(seq))
        exit()
    for i in range(1, 4):
        seq += str(i)
        func(k + 1, seq)
        seq = seq[:-1]

n = int(input())
func(0, '')