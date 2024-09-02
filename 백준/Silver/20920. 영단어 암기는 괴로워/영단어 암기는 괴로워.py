import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}
for i in range(n):
    word = input()
    if len(word) > m:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
for k, v in sorted(dict.items(), key= lambda x: (-x[1], -len(x[0]), x[0])):
    sys.stdout.write(k)