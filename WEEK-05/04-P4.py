daySteps = []
with open(".\\Resource\\steps.txt") as f:
    lines = [line.rstrip() for line in f]
    daySteps.extend(lines)


def sumM(listN,numS,days):
    finalSum = 0

    for i in range(numS,days+numS,1):
        finalSum += int(listN[i])
    return finalSum

def calAvg(num,days):
    return round(num/days,1)

# 1
January = calAvg(sumM(daySteps,0,31),31)
print("The average steps taken in January was" , January)
# 2
February = calAvg(sumM(daySteps,31,28),28)
print("The average steps taken in February was" , February)
# 3
March = calAvg(sumM(daySteps,59,31),31)
print("The average steps taken in March was" , March)
# 4
April = calAvg(sumM(daySteps,90,30),30)
print("The average steps taken in April was" , April)
# 5
May = calAvg(sumM(daySteps,120,31),31)
print("The average steps taken in May was" , May)
# 6  
June = calAvg(sumM(daySteps,151,30),30)
print("The average steps taken in June was" , June)
# 7
July = calAvg(sumM(daySteps,181,31),31)
print("The average steps taken in July was" , July)
# 8
August = calAvg(sumM(daySteps,212,31),31)
print("The average steps taken in August was" , August)
# 9
September = calAvg(sumM(daySteps,243,30),30)
print("The average steps taken in September was" , September)
# 10
October = calAvg(sumM(daySteps,273,31),31)
print("The average steps taken in October was" , October)
# 11
November = calAvg(sumM(daySteps,304,30),30)
print("The average steps taken in November was" , November)
# 12
December = calAvg(sumM(daySteps,334,31),31)
print("The average steps taken in December was" , December)