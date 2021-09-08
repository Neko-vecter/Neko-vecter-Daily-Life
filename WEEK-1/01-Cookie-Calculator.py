# Powered By Neko.vecter
# This Program is licensed under a CC BY-NC-SA 4.0 License

cookies = int(input("How much cookies you want: "))

# One cookie need and times the cookies you need 
# to calculate total amount of material
cupsOfSugar = 0.125 * cookies
cupOfButter = 0.243 * cookies
cupsOfFlour = 0.157 * cookies

# use round to keep two decimals
cupsOfSugar = ("%.2f" % round(cupsOfSugar,2))
cupOfButter = ("%.2f" % round(cupOfButter,2))
cupsOfFlour = ("%.2f" % round(cupsOfFlour,2))

# Print out the result
print(cupsOfSugar,"cups of sugar")
print(cupOfButter,"cup of butter")
print(cupsOfFlour,"cups of flour")
