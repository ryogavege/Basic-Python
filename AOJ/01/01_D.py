S = int(input())
h = S // 3600
m = (S // 60) % 60
s = S % 60
print("{}:{}:{}".format(h, m, s))