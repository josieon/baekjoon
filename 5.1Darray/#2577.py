import sys
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
res = list(str(A * B * C))
arr = [0 for i in range(10)]
for i in res:
    arr[int(i)] += 1
for i in arr:
    print(i)