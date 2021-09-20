A = [1, 4, 11, 5, 2, 9]
B = [8, 1, 4, 3, 9, 13, 14]

C = []
D = []
E = []
## C
for i in A:
    if i in B:
        C.append(i)
## D
D.extend(A)
for i in range(0,len(A),1):
    for j in range(i+1,len(B),1):
        if(D[i] != B[j]):
            if B[j] not in D:
                D.append(B[j])
                break

for i in range(len(D)):
        for j in range(0, len(D)-i-1):
            if D[j] > D[j+1] :
                D[j], D[j+1] = D[j+1], D[j]
## E
for i in A:
    if i not in B:
        E.append(i)


print("C",C)
print("D",D)
print("E",E)

