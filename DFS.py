#lendo o arquivo do grafo
arquivo = input("insira o nome do arquivo:")

arqGrafo = open(arquivo, 'r')

conteudoArq = []
dados_importantes =[]

dados_importantes = arqGrafo.readline().split()

#colocando valores importantes no seu lugar
numVertices = int(dados_importantes[0])
quantArestas = int(dados_importantes[1])

# lendo o arquivo
lista = arqGrafo.readlines()

# criando lista provisoria
conteudoArq = [[] for _ in range(numVertices)] 

# colocando os valores na lista por linha lida de acordo com a ordem numerica
for i in range(len(lista)):
    linha = lista[i].split()
    #ordem numerica é abstrata pois ele so esta no suposto lugar  que ele deveria
    conteudoArq[int(linha[0])-1].append(linha[1])     

#colocando em ordem 
lista_adj = [sorted(li) for li in conteudoArq]
arqGrafo.close()

#fazendo uma lista de ondem para execução com a maior grau de saida 
maior_lista = 0
tam_maior = 0
for i in lista_adj:
    tam_lista = len(i)
    if tam_lista>tam_maior:
        tam_maior = tam_lista
        maior_lista = i

x = 0
for i in lista_adj:
   if maior_lista == i:
       break
   x = x + 1

lista_V = [x]
for i in range(numVertices-1):
    if i == x:
        continue
    lista_V.append(i)

#variaveis e listas utilizadas no dfs
cor = ['BRANCO']*numVertices
mark = 0
d = [0]*numVertices
f = [0]*numVertices

#algoritmo de busca em profundidade
def DFS_VISIT(vert_vizinhos, u):
    global mark
    cor[u] = 'CINZA'
    mark += 1
    d[u] = mark
    for j in vert_vizinhos:
        i = int(j)-1
        if cor[i] == 'BRANCO':
            DFS_VISIT(lista_adj[i],i)
            print(f"{u+1} {i+1}: árvore")
        elif cor[i] == 'CINZA':
            print(f"{u+1} {i+1}: retorno")
        elif cor[i] == 'PRETO': 
            if d[u] < d[i]:
                print(f"{u+1} {i+1}: avanço")
            else:
                print(f"{u+1} {i+1}: cruzamento")
    cor[u] = 'PRETO'
    mark += 1
    f[u] = mark
    
def DFS():
    if quantArestas != 0:
        for v in lista_V:
            if cor[v] == 'BRANCO':
                DFS_VISIT(lista_adj[v], v)
           
DFS()

print("vetor d:",d)
print("vetor f:",f)