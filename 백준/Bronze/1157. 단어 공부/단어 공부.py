word = input()
alphabet = [0 for i in range(26)]
for i in word:
    if ord(i) - 97 < 0:
        alphabet[ord(i) - 65] += 1
    else:
        alphabet[ord(i) - 97] += 1
s_alp = sorted(alphabet)
if s_alp[25] == s_alp[24]:
    print('?')
else:
    print(chr(alphabet.index(max(alphabet)) + 65))