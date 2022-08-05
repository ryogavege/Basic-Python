a,b,c = map(int, input().split())
if a < b:
    if b < c:
        print(a,b,c)
    elif c < b:
        if a < c:
            print(a,c,b)
        else:
            print(c,a,b)
else: #b<a
    if a < c:
        print(b,a,c)
    else:
        if b < c:
            print(b,c,a)
        else:
            print(c,b,a)
        