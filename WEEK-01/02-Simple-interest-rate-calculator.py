# Powered By Neko.vecter
# This Program is licensed under a CC BY-NC-SA 4.0 License

P = float(input("P="))
r = (float(input("r'=")))/100
n = float(input("n="))
t = float(input("t="))

A = (P*((1+(r/n)))**(n*t))

A = round(A,2)
A = '{:,}'.format(A)

print("At the end of", t ,"years you will have $" + A)