M=[]
soma = 0
for i in range(0, 4):
    M.append([])
    for j in range(0,3):
        M[i].append(int(input("Digite um valor [{}][{}] -> ".format(i,j))))
        soma += M[i][j]
print(M)
print(soma)