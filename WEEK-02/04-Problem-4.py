monthsList = ["January","February","March","April","May","June","July","August","September","October","November","December"]
monthsRainfall = []
for i in range(0,len(monthsList),1):
    inputNum = float(input("Enter the rainfall for " + monthsList[i] + ":"))
    monthsRainfall.append(inputNum)

totalRainfall = sum(monthsRainfall)
avgRainfall = totalRainfall/len(monthsList)

highRainfall = monthsList[monthsRainfall.index(max(monthsRainfall))]
lowRainfall = monthsList[monthsRainfall.index(min(monthsRainfall))]

totalRainfall = ("%.2f" % round(totalRainfall,2))
avgRainfall = ("%.2f" % round(avgRainfall,2))

print(totalRainfall)
print(avgRainfall)
print(highRainfall)
print(lowRainfall)