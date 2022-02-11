import sys
N = int(sys.stdin.readline())
for i in range(N):
    arr=list(sys.stdin.readline())
    arr.pop()
    score = 0
    point = 0
    for i in arr:
        if i == 'X':
            point = 0
        elif i == 'O':
            point += 1
            score += point
    print(score)