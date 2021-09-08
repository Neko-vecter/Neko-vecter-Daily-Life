# Powered By Neko.vecter
# This Program is licensed under a CC BY-NC-SA 4.0 License

startNum = int(input("Starting number of organisms:"))
dailyIncrease = float(input("daily increase: "))/100
numberOfDays = int(input("number of days: "))

finalPopulation = startNum

for i in range(1 , numberOfDays , 1):
    finalPopulation = finalPopulation + (finalPopulation * dailyIncrease)

finalPopulation = round(finalPopulation)
print("on day " + str(numberOfDays) + ", the population is" , str(finalPopulation) +".")