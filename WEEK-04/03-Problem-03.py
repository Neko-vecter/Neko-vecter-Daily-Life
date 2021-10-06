def prime_or_composite(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return str(num) + " is composite."

        else:
            return str(num) + " is prime."

    else:
        return str(num) + " is composite."

i = False
while(i == False):
    inputNum = int(input("Enter an integer greater than 1: "))
    if(inputNum > 0):
        i = True
    else:
        print("Invalid input.")

for i in range(0,inputNum-1,1):
    print(prime_or_composite(i+2))