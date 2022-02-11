import sys
number = int(sys.stdin.readline())
for i in range(1, number+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(i, a, b, a+b))