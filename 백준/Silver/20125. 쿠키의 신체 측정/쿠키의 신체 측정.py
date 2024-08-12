import sys

n = int(input())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]
for i in range(n):
    if '*' in arr[i]:
        x = i + 2
        y = arr[i].index('*') + 1
        break
arm = arr[x - 1].count('*')
left_arm = y - arr[x - 1].find('*') - 1
right_arm = arm - left_arm - 1
for j in range(x, n):
    if arr[j][y - 1] == '_':
        leg_start = j
        break
body = leg_start - x
left_leg, right_leg = 0, 0
for k in range(leg_start, n):
    if '*' not in arr[k]:
        break
    if arr[k][y - 2] == '*':
        left_leg += 1
    if arr[k][y] == '*':
        right_leg += 1
print(x, y)
print(left_arm, right_arm, body, left_leg, right_leg)