courseList = [["CS101","3004","Haynes","8:00 a.m."],
              ["CS102","4501","Alvarado","9:00 a.m."],
              ["CS103","6755","Rich","10:00 a.m."],
              ["NT110","1244","Burke","11:00 a.m."],
              ["CM241","1411","Lee","1:00 p.m."]]

inp = str(input("Enter a course number: "))
find = False
for i in range(0,len(courseList),1):
    if(courseList[i][0] == inp):
        print("The details for course",courseList[i][0],"are:")
        print("Room:",courseList[i][1])
        print("Instructor:",courseList[i][2])
        print("Alvarado Time:",courseList[i][3])
        find = True
        break

if(find == False):
    print(inp, "is an invalid course number.")
