## P1
a_file = open("WEEK-06/Resource/avgTemp_state_season.51.5.csv", "r")

list_of_lists = []
for line in a_file:
    stripped_line = line.strip()
    line_list = stripped_line.split(",")
    list_of_lists.append(line_list)

print(list_of_lists)

temp_by_state = {}

for i in range(1,len(list_of_lists),1):
    temp_by_state[list_of_lists[i][0]] = [list_of_lists[i][1],list_of_lists[i][2],list_of_lists[i][3],list_of_lists[i][4]]

## P2
reading = temp_by_state.items()
reading = list(reading)

for i in range(0, len(reading),1):
    avg = round((float(reading[i][1][0])+float(reading[i][1][1])+float(reading[i][1][2])+float(reading[i][1][3]))/4,2)
    print(str(reading[i][0]) + ": " + str(avg) + "°F")

## P3
reading = temp_by_state.items()
reading = list(reading)

temp_by_season = {}

for i in range(0,4,1):
    seList = []
    for j in range(0,len(reading),1):
        temp = [reading[j][0],reading[j][1][i]]
        seList.append(tuple(temp))

    if(i == 0):
        temp_by_season["Spring"] = seList
    elif(i == 1):
        temp_by_season["Summer"] = seList
    elif(i == 2):
        temp_by_season["Fall"] = seList
    elif(i == 3):
        temp_by_season["Winter"] = seList
    
print(temp_by_season["Spring"])
