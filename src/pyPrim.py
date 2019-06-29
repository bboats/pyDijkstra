#!python3
###########TO DO##############
#encontrar vizinhos (como usamos dicionário é possivel fazer isso com uma função de if a in b) [X]
#métodos para adicionar e remover arestas/vertices (dentro da clase Grafo) -- [...X?]  
#fazer o tal do algoritmo pipipipopopo [ ]
#############################



#valor infinito para utilizarmos posteriormente no algoritmo
infinito = float('inf')

if 1 < infinito:
	print('oi')

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
		'''determina qual o vertice que possui o menor custo para adicionar no grafo final'''
		dist_total_escolhido = infinito #valor que grava qual a menor distancia ateh o momento
		vert_escolhido = -1 #numero do vertice escolhido

		for vertice_atual in self.grafoInclui:
			for destino,peso in self.arestas[vertice_atual].items():
				dist_total_atual = peso + self.pesosMinimos[vertice_atual-1] + self.vertices[destino]
				if (dist_total_atual  < dist_total_escolhido) and (destino not in self.grafoInclui):
					dist_total_escolhido = dist_total_atual
					vert_escolhido = destino

		self.pesosMinimos[vert_escolhido-1] = dist_total_escolhido
		self.grafoInclui.append(vert_escolhido)


numVertices = 5 ##iteração ao gerar a matriz
destinoVertices = [1,2,3,4,5] ##utilizado para output
##utilizados na geração do grafo
pesosVertices = [1,1,100,2,2] 
matrizArestas = [[-1, 2, 1, 3, -1], 
				[2, -1, 3, -1, -1], 
				[1, 3, -1, 1, 2], 
				[3, -1, 1, -1, 4], 
				[-1, -1, 2, 4, -1]]





teste = Grafo(matrizArestas,pesosVertices)

while -1 in teste.pesosMinimos:
	teste.menor_distancia()
	#print(teste.pesosMinimos)

print("Dijkstra grafos em python")
for vert in destinoVertices:
	print ("Custo de 1 para {}: {}".format(vert,teste.pesosMinimos[vert-1]))

###USER INPUT###
#will be part of the code but sublime text is a pain to work with user input so for now we will use already defined variables instead#
'''
numVertices = int(input('quantas vertices?: '))
destinoVertices = input('quais os destinos? (separados por espaco)\n ').split(' ')
pesosVertices = list(map(int, input('quais os pesos das vertices? (separados por espaco e ordenados)\n').split(' ')))
matrizArestas = [] #define futura lista de listas que sera inserida pelo usuario para informar pesos das arestas que saem de cada vertice
for i in range(numVertices):
	matrizArestas.append(list(map(int, input('Peso das arestas que saem do vertice {}? (-1 indica a ausencia da aresta)\n'.format(i+1)).split(' '))))
'''


