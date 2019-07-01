#!python3
#Trabalho final da cadeira de grafos
#Implementacao do algoritmo de prim modificado para levar em conta as vertices possuirem peso proprio
#Marcos Vinicius de Oliveira Pinto - 00288560

#valor infinito para utilizarmos posteriormente no algoritmo
infinito = float('inf')

#classe de grafo, inicialmente no arquivo principal para facilitar testes
####!!!! transferir para classes.py ao concluir o dev do programa !!!!####
class Grafo:
	'''Grafo(arestas,nodos)
	     arestas: matriz de arestas informadas pelo usuario no input será transformada em uma lista de tuplas nomeadas
	     vertices: lista de pesos das vertices ordenadas, serão transformadas em um dicionario contendo nomeDoVertice:peso '''
	def __init__(self, arestas, vertices):
		self.arestas = self.matrizArestas_to_dictArestas(arestas)
		self.vertices = {vertice+1:peso for vertice,peso in enumerate(vertices)} #gera o dicionario de peso dos vertices
		self.grafo = [[-1 for column in range(len(vertices))] for row in range(len(vertices))] #matriz de adj do grafo final
		self.grafoInclui = [1] #lista de vertices já inclusos no grafo final
		self.pesosMinimos = [-1 for i in vertices]
		self.pesosMinimos[0] = self.vertices[1]


	def matrizArestas_to_dictArestas(self, arestas):
		'''recebe uma matriz de arestas e transforma ela em um dicionário de dicionários no formato {origem: {destino: peso}}'''
		dictArestas = {}
		for origem,listaDeAdj in enumerate(arestas):
			for destino,peso in enumerate(listaDeAdj):
				if peso != -1:
					if origem+1 in dictArestas:
						dictArestas[origem+1][destino+1] = peso
					else:
						dictArestas[origem+1] = {destino+1 : peso}
		return dictArestas


	def menor_distancia(self):
		'''determina qual o vertice que possui o menor custo para adicionar no grafo final e adiciona'''
		dist_total_escolhido = infinito #valor que grava qual a menor distancia ateh o momento
		vert_escolhido = -1 #numero do vertice escolhido

		#testa todos os vertices ja inclusos na arvore geradora minima
		for vertice_atual in self.grafoInclui:
			#checa todos possiveis vertices alcancaveis a partir do vertice ja incluso escolhido
			for destino,peso in self.arestas[vertice_atual].items():
				#calcula a distancia total para atingir o vertice nao incluido na arvore
				dist_total_atual = peso + self.pesosMinimos[vertice_atual-1] + self.vertices[destino]
				#testa todas para descobrir qual eh o nodo de menor custo para adicionar na arvore
				if (dist_total_atual  < dist_total_escolhido) and (destino not in self.grafoInclui):
					dist_total_escolhido = dist_total_atual #atualiza dist_total caso encontre uma opcao de menor custo
					vert_escolhido = destino # atualiza qual o numero do novo vertice de menor custo 

		#adiciona o custo para atingir o vertice que acaba de ser escolhido a arvore minima
		self.pesosMinimos[vert_escolhido-1] = dist_total_escolhido
		#inclui ele na lista de vertices ja inclusos na arvore
		self.grafoInclui.append(vert_escolhido)




#############################
#############################
###      DRIVER CODE      ###
#############################
#############################


#recebe inputs do usuario
numVertices = int(input('quantas vertices?: '))
destinoVertices = list(map(int, input('quais os destinos? (separados por espaco)\n').split(' ')))
pesosVertices = list(map(int, input('quais os pesos das vertices? (separados por espaco e ordenados)\n').split(' ')))
matrizArestas = [] #define futura lista de listas que sera inserida pelo usuario para informar pesos das arestas que saem de cada vertice

#recebe iterativamente a matriz de adjacencia dos vertices
for i in range(numVertices):
	matrizArestas.append(list(map(int, input('Peso das arestas que saem do vertice {}? (-1 indica a ausencia da aresta)\n'.format(i+1)).split(' '))))



#cria um objeto da classe grafo com os dados obtidos
teste = Grafo(matrizArestas,pesosVertices)

#enquanto a lista de pesos da arvore geradora minima nao for completa (ainda restam vertices nao incluidos)
while -1 in teste.pesosMinimos:
	teste.menor_distancia() #chama o metodo menor distancia, que insere o vertice de menor distancia ainda nao incluido na arvore


#output
resultado = ""

#gera iterativamente a string de output consultando a arvore geradora minima	
for vert in destinoVertices:
	#print ("Custo de 1 para {}: {}".format(vert,teste.pesosMinimos[vert-1])) #print verbose
	resultado += str(teste.pesosMinimos[vert-1]) + ' '

resultado = resultado[0:-1] #remove espaco final desnecessario

print(resultado)
input('encerra')

