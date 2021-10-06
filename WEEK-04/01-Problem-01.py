def filter_list(num,list):
    filterNum = []
    for i in range(0, len(list), 1):
        if(list[i]>num):
            filterNum.append(list[i])
    return filterNum

listOfNum = [19, 2940, 10, 24, 29, 1, 85, 201, -15, -122, 799]
num = 13

print("Number :", num)
print("List of numbers :", listOfNum)
print("List of numbers that are larger than" , num , ":" ,filter_list(num,listOfNum))