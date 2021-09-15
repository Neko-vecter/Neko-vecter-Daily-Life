num = []
posNum = [] ; negNum = []
posSum = 0 ; negSum = 0
# input nums
for i in range (0,10,1):
    inputTimes = str(i+1)
    inputNum = int(input('Enter number '+ inputTimes + ' of 10: '))
    num.append(inputNum)

for i in range(0 , len(num),1):
    if(num[i]>0):
        posNum.append(num[i])
    else:
        negNum.append(num[i])
# Add pos and neg nums
for i in range(0,len(posNum),1):
    posSum += posNum[i]
for i in range(0,len(negNum),1):
    negSum += negNum[i]
# Print sum
print("Positive sum:",posSum)
print("Negative sum:",negSum)