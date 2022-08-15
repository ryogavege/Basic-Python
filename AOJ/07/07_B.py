while True:
    n, x = map(int, input().split())
    if n == 0:
        break
    count = 0
    for i in range(1, n - 1):
        for k in range(i + 1, n):
            for m in range(k + 1, n + 1):
                if i + k + m == x:
                    count += 1
    print(count)
