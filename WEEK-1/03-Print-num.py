# Powered By Neko.vecter
# This Program is licensed under a CC BY-NC-SA 4.0 License

X = int(input("X="))
Y = int(input("Y="))

if(X<Y):
    for i in range(X,Y+1,1):
        print(i)
else:
    for i in range(Y,X+1,1):
        print(i)