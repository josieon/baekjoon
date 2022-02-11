import sys
arr = list(str(sys.stdin.readline()))
res = [-1 for i in range(26)]
for i in range(len(arr) - 1):
    if(res[ord(arr[i]) - 97] == -1):
        res[ord(arr[i]) - 97] = i
for i in res:
    print(res[i], end = ' ')