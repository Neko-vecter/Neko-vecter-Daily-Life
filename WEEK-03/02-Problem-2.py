x = [3, 5, 6, 10, 12, 14, 20, 22, 23]
y = [1, 2, 4, 8, 9, 11, 15, 16]

z = x+y

for i in range(1, len(z)):
        for j in range(0, len(z)-i):
            if z[j] > z[j+1]:
                z[j], z[j + 1] = z[j + 1], z[j]

print("z =", z)