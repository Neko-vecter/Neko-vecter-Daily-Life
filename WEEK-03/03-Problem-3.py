l = ["apple", "banana", "strawberry", "orange", "cherry", "melon"]
input = str(input(""))

find = False

for i in range(0,len(l),1):
    if(l[i].find(input) != -1):
        find = True
        break

if(find == True):
    print("Success")
else:
    print("Failure")