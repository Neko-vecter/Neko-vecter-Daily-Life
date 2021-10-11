from csv import reader
# read csv file as a list of lists
with open(".\\Resource\\oscar_age_female.csv", "r") as read_obj:
    csv_reader = reader(read_obj)
    listO = list(csv_reader)

# The years and names of Oscars Best Actress Winners after the year 2000 (including 2000)
indexOfActressWinners = []
for i in range(1,len(listO),1):
    if(int(listO[i][1]) <= 2000):
        indexOfActressWinners.append(i)

print("years and names of Oscars Best Actress Winners after the year 2000")
for i in range(0,len(indexOfActressWinners),1):
    print(listO[int(indexOfActressWinners[i])][1] , "," , listO[int(indexOfActressWinners[i])][3])

print()

# The years, names, ages, and movies of those who were younger than 30 (including 30) when they won Oscar.
indexOfYounger = []
for i in range(1,len(listO),1):
    if(int(listO[i][2]) <= 30):
        indexOfYounger.append(i)

print("years, names, ages, and movies of those who were younger than 30")
for i in range(0,len(indexOfYounger),1):
    print(listO[int(indexOfYounger[i])][1] , "," , listO[int(indexOfYounger[i])][3] , "," , 
    listO[int(indexOfYounger[i])][2] ,"," , listO[int(indexOfYounger[i])][4])

print()

# The year, name, age, and movie of the winner who was the oldest age when she won Oscar.
oldest = 1
for i in range(1,len(listO),1):
    if(listO[i][2] > listO[oldest][2]):
        oldest = i
print("year, name, age, and movie of the winner who was the oldest age when she won")

print(listO[oldest][1] , "," , listO[oldest][3] , "," , 
listO[oldest][2] ,"," , listO[oldest][4])

