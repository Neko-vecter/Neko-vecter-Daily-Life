num = []
Sum = 0
# input nums
for i in range (0,10,1):
    inputTimes = str(i+1)
    inputNum = float(input('Enter number '+ inputTimes + ' of 10: '))
    num.append(inputNum)

for i in range(0,len(num),1):
    Sum += num[i]

lowNum = min(num)
highNum = max(num)
Sum = round(Sum,2)
avg = round(Sum/len(num),2)

print("Lowest number:",lowNum)
print("Highest number:",highNum)
print("Total:",Sum)
print("Average:",avg)