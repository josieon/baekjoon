def d(n):
    sum = n
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

arr = [0 for i in range(10001)]
for i in range(10001):
    res = d(i)
    if res < 10000:
        arr[res] = 1
for i in range(10000):
    if arr[i] == 0:
        print(i, end = ' ')