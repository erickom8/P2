''' 
while = comando que verifica se uma condição for verdadeira e se for atendida, executa os comandos dessa estrutura até que a condição mude e seja falsa

for = comando que repete uma sequência de instrucções qenquanto uma condição for verdadeira. Percorre um objeto iterado (elementos dentro de um objeto, que pode ser precorrido individualmente)
    'for <variavel> in <objeto iteravel>:
        bloco de instruções'

vetores = variaveis com características especiais, onde podemos salvar/alterar/acessar valores individualmente podendo mudar o conteúdo dentro dela ja que ela esta salva dentro da memoria RAM do PC local. 

var = {valor}
vet = [| |, | |, | |]

em linguagem c, o vetor ele é fixo e não pode ser alterado, ja em pýthon você consegue formatar cada vetor

primeira posição de um vetor = 0

vetores x listas: 
lista permite o armazenamento de diversos tipos de valores, podendo conter 0 elementos ou n elementos inclusive vetores dentro da lista.

L=[] (vetor vazio)
Z=[4,5,2] (vetor com 3 elementos sendo separados por vírgulas)

nomedalista[indice] 

len = tamanho da lista 
L = [1,2,3,4,5]
print(len(L)) //5

'=' vai funcionar apenas se ja existe determinado espaço no vetor para ele ser alterado
'.append' ira adicionar apenas no final da lista, pode ser adicionado em um vetor vazio : v =[]
'.insert' cria um espaço na posição que você indicou


matrizes = conjunto de vetores

'''

M = []
for i in range (5):
    M.append(int(input('insira um numero: ')))

print(M)     