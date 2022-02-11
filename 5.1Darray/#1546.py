import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
newarr = []
for i in range(N):
    newarr.append(arr[i] / max(arr) * 100)
print(sum(newarr) / len(newarr))