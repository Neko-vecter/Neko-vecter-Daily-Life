import math
x = [3.23, 2.11, 5.36, 8.21, 1.34]
y = [12.45, -1.2, 2.23, 9.8, 0.23]

XYi = 0 ; Xi = 0 ; Yi = 0
Xi2 = 0 ; Yi2 = 0
## cal xyi
for i in range(0, len(x), 1):
    temp = x[i]*y[i]
    XYi += temp
## cal Xi
for i in range(0, len(x), 1):
    Xi = Xi+(x[i])
## cal Yi
for i in range(0, len(x), 1):
    Yi = Yi+(y[i])
n = len(x)

## cal Xi2
for i in range(0, len(x), 1):
    Xi2 = Xi2+(x[i]**2)
## cal Yi2
for i in range(0, len(x), 1):
    Yi2 = Yi2+(y[i]**2)
n = len(x)

finalS = (n*(XYi)-(Xi*Yi))/math.sqrt(((n*Xi2)-Xi**2)*((n*Yi2)-Yi**2))

finalS = round(finalS,2)
print("r =",finalS)