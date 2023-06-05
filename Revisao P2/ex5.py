
from random import randint

M=[]
diagonal_principal = []
pares = []
for i in range(0, 6):
    M.append([])
    for j in range(0, 6):
        M[i].append(randint(1,50))
print(M)

for i in range (0, 6):
    for j in range (0, 6):
        if i == j: 
            diagonal_principal.append(M[i][j])
for i in diagonal_principal:
    if i % 2 == 0:
        pares.append(i)
# print('Diagonal principal: {}'.format(diagonal_principal))
print('Pares da diagonal Principal: {}'.format(pares))