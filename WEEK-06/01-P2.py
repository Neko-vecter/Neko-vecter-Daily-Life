a_file = open("WEEK-06/Resource/WorldSeriesWinners.txt", "r")

list_of_lists = []
for line in a_file:
    stripped_line = line.strip()
    list_of_lists.append(stripped_line)

con = 0
inp = int(input("Enter a year in the range 1903-2009: "))
inpn = inp - 1903

print(list_of_lists[inpn])
if(list_of_lists[inpn] == "No Winner"):
    print("The world series wasn't played in the year", inp)

else:
    
    for i in range(0,len(list_of_lists),1):
        if(list_of_lists[i]==list_of_lists[inpn]):
            con += 1

print("The team that won the world series in",inp,"is the "+ str(list_of_lists[inpn]) +". They won the world series",con,"times.")