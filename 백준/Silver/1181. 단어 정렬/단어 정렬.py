n = int(input())
w = set(input() for _ in range(n))
print(*sorted(w, key=lambda x: (len(x), x)), sep='\n')