import sys
C = int(sys.stdin.readline())
for i in range(C):
    arr = list(map(int, sys.stdin.readline().split()))
    N = arr[0]
    arr = arr[1:]
    avg = sum(arr) / N
    cnt = 0
    for stu in arr:
        if stu > avg:
            cnt += 1
    print("{0:0.3f}%".format(float(cnt / N * 100)))