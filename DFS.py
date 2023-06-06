#lendo o arquivo do grafo
arquivo = input("insira o nome do arquivo:")

arqGrafo = open(arquivo, 'r')
conteudoArq = []
dados_importantes =[]

dados_importantes = arqGrafo.readline().split()

#colocando valores importantes no seu lugar
numVertices = int(dados_importantes[0])
quantArestas = int(dados_importantes[1])

if len(dados_importantes) > 2:
    direcionamento = "direcionado"
else: 
    direcionamento = "não direcionado"

# print("\nvertices:",numVertices,"\nArestas:", quantArestas,'\nDirecionamento:',direcionamento,'\n')

# lendo o arquivo
lista = arqGrafo.readlines()

# criando lista provisoria
listadj = [[] for _ in range(numVertices)] 

# colocando os valores na lista por linha lida de acordo com a ordem alfabetica
for i in range(len(lista)):
    linha = lista[i].split()
    #ordem alfabetica é abstrata pois ele so esta no suposto lugar  que ele deveria
    listadj[ord(linha[0])-97].append(linha[1])     

#colocando em ordem 
lista_adj = [sorted(li) for li in listadj]
arqGrafo.close()

#fazendo uma lista de ondem para execução com a maior grau de saida 
maior_lista = None
tam_maior = 0
for lista in lista_adj:
    tam_lista = len(lista)
    if tam_lista>tam_maior:
        tam_maior = tam_lista
        maior_lista = lista
x = 0
for i in lista_adj:
    if maior_lista == i:
        break
    x = x + 1

lista_V = [numVertices]
for i in range(numVertices):
    if lista_V[0] != x:
        lista_V.append(x)
    else:
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
        i = ord(j)-97
        if cor[i] == 'BRANCO':
            DFS_VISIT(lista_adj[i],i)
            print(f"{chr(u+97)} {chr(i+97)}: árvore")
        elif cor[i] == 'CINZA':
            print(f"{chr(u+97)} {chr(i+97)}: retorno")
        elif cor[i] == 'PRETO': 
            if d[u] < d[i]:
                print(f"{chr(u+97)} {chr(i+97)}: avanço")
            else:
                print(f"{chr(u+97)} {chr(i+97)}: cruzamento")
    cor[u] = 'PRETO'
    mark += 1
    f[u] = mark
    
def DFS():
    for i in lista_V:
        v = lista_V[i]
        if cor[v] == 'BRANCO':
            DFS_VISIT(lista_adj[v], v)
           
DFS()
# print('\nLista Adjacente:\n', lista_adj)
print("\nvetor d:",d)
print("vetor f:",f)