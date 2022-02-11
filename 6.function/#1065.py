import sys
N = int(sys.stdin.readline())
cnt = 0
for i in range(1, N+1):
    arr = []
    gap = []
    while i > 0:
        arr.append(i % 10)
        i = i // 10
    for j in range(len(arr)-1):
        gap.append(arr[j] - arr[j+1])
    if(len(arr) > 1):
        gap = set(gap)
    else:
        cnt += 1
    if len(gap) == 1:
        cnt += 1
print(cnt)