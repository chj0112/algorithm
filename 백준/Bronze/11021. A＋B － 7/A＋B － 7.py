T = int(input())
A, B = [0] * T, [0] * T
for i in range(T):
    A[i], B[i] = map(int, input().split())
    print("Case #" + str(i + 1) + ": " + str(A[i] + B[i]))