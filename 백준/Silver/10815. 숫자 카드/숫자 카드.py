import sys
input = sys.stdin.readline

n = int(input())
card = set(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
for i in arr:
    sys.stdout.write(str(int(i in card)) + ' ')