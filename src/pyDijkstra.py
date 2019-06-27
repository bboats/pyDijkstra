#!python3
from collections import namedtuple,deque

###########TO DO##############
#encontrar vizinhos (como usamos dicionário é possivel fazer isso com uma função de if a in b) [X]
#métodos para adicionar e remover arestas/vertices (dentro da clase Grafo) -- [...X?]  
#fazer o tal do algoritmo pipipipopopo [ ]
#############################



#valor infinito para utilizarmos posteriormente no algoritmo
infinito = float('inf')

#gera uma tupla nomeada para as arestas com a intencao de facilitar a compreensao do programa
Aresta = namedtuple('Aresta','inicio, fim, peso')
def gera_aresta(inicio,fim,peso):
	return Aresta(inicio,fim,peso)

#gera uma tupla nomeada para os nodos com a intencao de facilitar a compreensao do programa
Vertice = namedtuple('Vertice','nome, peso')
def gera_vertice(nome,peso):
	return Vertice(nome,peso)

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
		self.grafoInclui = [] #lista de vertices já inclusos no grafo final
		self.pesosMinimos = [-1 for i in vertices]


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

	def adiciona_aresta(self, inicio, fim, peso):
		#insere em arestas[inicio][destino] (e garante que não ocorrerão key errors)
		if inicio in self.arestas:
			self.arestas[inicio][destino] = peso
		else:
			self.arestas[inicio] = {destino:peso}

		#idem porém em arestas[destino][inicio] (as arestas são bidirecionais)
		if destino in self.arestas:
			self.arestas[destino][inicio] = peso
		else:
			self.arestas[destino] = {inicio:peso}



	def remove_aresta(self, inicio, destino):
		'''remove uma aresta de um dicionario dando seu inicio e destino, esta aresta precisa estar presente'''
		self.arestas[inicio].pop(destino)
		self.arestas[destino].pop(inicio)

	def menor_distancia(self):
		'''determina qual o nodo que possui o menor custo para adicionar no grafo final'''
		decisao = "trocar pelo numero do vertice de menor distancia"
		print (self.arestas) # isso diz os pesos das arestas conectadas a cada vertice do grafo original
		print (self.grafoInclui) #isso vai dizer quais estao e n estao no grafo
		print (decisao)
		#DO THIS#


numVertices = 5 ##iteração ao gerar a matriz
destinoVertices = [2,4,5] ##utilizado para output
##utilizados na geração do grafo
pesosVertices = [1,1,100,2,2] 
matrizArestas = [[-1, 2, 1, 3, -1], 
				[2, -1, 3, -1, -1], 
				[1, 3, -1, 1, 2], 
				[3, -1, 1, -1, 4], 
				[-1, -1, 2, 4, -1]]





teste = Grafo(matrizArestas,pesosVertices)
teste.menor_distancia()
print(teste.pesosMinimos)

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


