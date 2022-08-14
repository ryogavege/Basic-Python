for i in range(1, 3001):
    a, b = map(int, input().split())
    if a == b == 0:
        break
    elif a < b:
        print(a, b)
    else:
        print(b, a)
    i += 1
