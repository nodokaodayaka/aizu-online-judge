import math

x = 0
y = 1
p1 = (0, 0)
p2 = (100, 0)
sin60 = math.sin(math.radians(60))
cos60 = math.cos(math.radians(60))

n = int(input())

def kock(n, p1, p2):
    if n == 0:
        return

    # p1, p2 から s, t, u を計算
    s = (0, 0)
    t = (0, 0)
    u = (0, 0)
    s = ((2 * p1[x] + 1 * p2[x]) / 3, (2 * p1[y] + 1 * p2[y]) / 3)
    t = ((1 * p1[x] + 2 * p2[x]) / 3, (1 * p1[y] + 2 * p2[y]) / 3)
    u = ((t[x] - s[x])*cos60 - (t[y] - s[y])*sin60 + s[x], (t[x] - s[x])*sin60 + (t[y] - s[y])*cos60 + s[y])

    kock(n-1, p1, s)
    print ('{:.8f} {:.8f}'.format(s[x], s[y]))
    kock(n-1, s, u)
    print ('{:.8f} {:.8f}'.format(u[x], u[y]))
    kock(n-1, u, t)
    print ('{:.8f} {:.8f}'.format(t[x], t[y]))
    kock(n-1, t, p2)


print ('{:.8f} {:.8f}'.format(p1[x], p1[y]))
kock(n, p1, p2)
print ('{:.8f} {:.8f}'.format(p2[x], p2[y]))
