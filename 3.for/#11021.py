import sys
number = int(sys.stdin.readline())
for i in range(1, number+1):
    print("Case #{}: {}".format(i, sum(map(int, sys.stdin.readline().split()))))