num = int(input("Enter pocket number:"))
if(num == 0):
    print("The color is: Green")
elif(num>=1 and num<=10):
    if(num % 2 != 0):
        print("The color is: Red")
    else:
        print("The color is: Black")
elif(num>=11 and num<=18):
    if(num % 2 == 0):
        print("The color is: Red")
    else:
        print("The color is: Black")
elif(num>=19 and num<=28):
    if(num % 2 != 0):
        print("The color is: Red")
    else:
        print("The color is: Black")
elif(num>=29 and num<=36):
    if(num % 2 == 0):
        print("The color is: Red")
    else:
        print("The color is: Black")
else:
    print("Error: The pocket number is invalid")