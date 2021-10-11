sentence = input("Enter a string:").lower()
words = sentence.split()
print(words)

for i in range(0,len(words),1):
    for j in range(0,len(words[i]),1):
        words[i] = words[i][1:] + words[i][:1] + "ay"
        break
pig_latin = ' '.join(words)
print(pig_latin.upper())