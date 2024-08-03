bowl = input()
prev = ''
height = 0
for i in bowl:
    if prev != i:
        height += 10
    else:
        height += 5
    prev = i
print(height)