nn = int(input("How much number you want to in arr x:"))
mm = int(input("How much number you want to in arr y:"))
x = []
y = []
Findit = False

## X arr append
for i in  range(0,nn,1):
    inputTimes = str(i+1)
    inputNum = float(input('Enter number of x '+ inputTimes + " of "+ str(nn) + ": "))
    x.append(inputNum)

## Y arr append
for i in  range(0,mm,1):
    inputTimes = str(i+1)
    inputNum = float(input('Enter number of y '+ inputTimes + " of "+ str(mm) + ": "))
    y.append(inputNum)

for i in range(0,nn,1):
    for j in range(0,mm,1):
        if(x[i] == y[j]):
            Findit = True
            break

if(Findit == True):
    print("True")
else:
    print("False")