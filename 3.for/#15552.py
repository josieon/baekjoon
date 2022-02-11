import sys
num = int(sys.stdin.readline())
for i in range(num):
    print(sum(map(int,sys.stdin.readline().split())))