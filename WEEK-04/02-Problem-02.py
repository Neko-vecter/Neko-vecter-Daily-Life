testSList = []
def get_valid_score():
    getScore = False
    while(getScore == False):
        inputS = float(input("Please enter a test score:"))
        if(inputS > 100):
            print("That is not a valid score")
            getScore = False
        elif(inputS < 0):
            print("That is not a valid score")
            getScore = False
        else:
            testSList.append(inputS)
            print("This student recieved a(n)" , determine_grade(inputS) , "on the test")
            getScore = True



def determine_grade(inputgrade):
    inputgrade = float(inputgrade)
    if(inputgrade>=90 and inputgrade<=100):
        return "A"

    elif(inputgrade>=80 and inputgrade<=89):
        return "B"

    elif(inputgrade>=70 and inputgrade<=79):
        return "C"

    elif(inputgrade>60 and inputgrade<=69):
        return "D"

    elif(inputgrade>=0 and inputgrade<=59):
        return "F"

def calc_average(testSList):
    sumOfList = 0
    for i in range(0,len(testSList),1):
        sumOfList += testSList[i]
    
    ## find avg
    Avg = sumOfList/len(testSList)
    return Avg
    

for i in range(0,3,1):
    get_valid_score()

print("The average of the" , len(testSList) , "test scores was" , round(calc_average(testSList),2))