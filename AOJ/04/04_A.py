def d(m, n):
    d = m // n
    return d


def r(x, y):
    r = x % y
    return r


def f(k, l):
    f = round(k / l, 5)
    return f


a, b = map(int, input().split())

d = d(a, b)
r = r(a, b)
f = f(a, b)

print(d, r, f)
