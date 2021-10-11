txtList = []
with open(".\\Resource\\average_number_of_words.txt" , encoding="utf-8") as f:
    lines = [line.rstrip() for line in f]
    txtList.extend(lines)

countList = []
for i in range(0,len(txtList),1):
    wordCount = 1
    for j in range(0,len(txtList[i]),1):
        if(txtList[i][j] == " "):
            wordCount += 1
    countList.append(wordCount)

sumList = 0
for i in range(0, len(countList),1):
    sumList += countList[i]

avg = sumList/len(countList)
print("Average number of words per line:", avg)