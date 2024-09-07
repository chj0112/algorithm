import sys
input = sys.stdin.readline

n = int(input())
w = set(input().rstrip() for _ in range(n))
print(*sorted(w, key=lambda x: (len(x), x)), sep='\n')