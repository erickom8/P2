from random import randint
M =[]
for i in range(0,5):
    M.append([])
    for j in range(0, 5):
        M[i].append(randint(1,25))

for i in range (0, 5):
    menor = 25
    for j in range (0, 5):
        if M[i][j] < menor:
            menor = M[i][j]
    print(M[i],'Menor numero da linha {}: {}'.format(i+1, menor))