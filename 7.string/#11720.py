import sys
N = int(sys.stdin.readline())
arr = list(str(sys.stdin.readline()))
arr.pop()
sum = 0
for i in arr:
    sum += int(i)
print(sum)