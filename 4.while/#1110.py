import sys
number = int(sys.stdin.readline())
origin = number
cycle = 0
while True:
    b = number // 10
    a = number % 10
    c = (a + b) % 10
    number = a * 10 + c
    cycle += 1
    if origin == number:
        break
print(cycle)