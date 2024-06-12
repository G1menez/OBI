a = int(input())
b = int(input())
c = int(input())
ab = a - b
ac = a - c
bc = b - c
if ab == 0:
    print(c)
elif ac == 0:
    print(b)
elif bc == 0:
    print(a)