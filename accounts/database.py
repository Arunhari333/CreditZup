n = [0] * 90
for i in range(1, 3):
    n[10 * i + 8] = 60
    n[10 * i + 1] = 80
    for j in range(2, 5):
        n[10 * i + j] = 70
    for k in range(5, 8):
        n[10 * i + k] = 80

s = [0] * 30
for i in range(1, 3):
    s[10 * i + 1] = 8
    s[10 * i + 2] = 15
    s[10 * i + 3] = 25
    s[10 * i + 4] = 40
    s[10 * i + 5] = 60

c = [0] * 40
for i in range(1, 4):
    c[10 * i + 1] = 8
    c[10 * i + 2] = 12
    c[10 * i + 3] = 20
    c[10 * i + 4] = 40
    c[10 * i + 5] = 60

p = [0] * 100
p[20] = 50
p[40] = 20
p[50] = 30
p[60] = 20
p[70] = 20
p[80] = 5
p[90] = 60
for i in range(1, 4, 2):
    z = 10
    for j in range(1, 6):
        if i == 3 and j == 3:
            z -= 10
        p[i * 10 + j] += z
        z += 10
p[32] -= 5

e = [0] * 12
e[1] = 60
e[2] = 30
e[3] = 35
e[4] = 50
e[5] = 80
e[6] = 60
e[7] = 60
e[8] = 60
e[9] = 80
e[10] = 80
e[11] = 50

l = [0] * 65
for i in range(1, 5):
    l[10 * i + 1] = 15
    l[10 * i + 2] = 10
    l[10 * i + 3] = 5

l[51] = 30
l[52] = 25
l[53] = 15
