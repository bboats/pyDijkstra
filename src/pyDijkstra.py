#!python3
from collections import namedtuple,deque


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
	     arestas: lista de arestas (tuplas nomeadas definidas acima, Aresta(inicio,fim,peso))
	     vertices: lista de vertices (tuplas nomeadas definidas acima, Vertice(nome,peso))'''
	def __init__(self, arestas, vertices):
		self.arestas = [gera_aresta(*aresta) for aresta in arestas]
		self.vertices = [gera_vertice(*vertice) for vertice in vertices]


numVertices = 5
destinoVertices = [2,4,5]
pesosVertices = [1,1,100,2,2]
matrizArestas = [[-1, 2, 1, 3, -1], [2, -1, 3, -1, -1], [1, 3, -1, 1, 2], [3, -1, 1, -1, 4], [-1, -1, 2, 4, -1]]

print(matrizArestas)


###USER INPUT###
'''
numVertices = int(input('quantas vertices?: '))
destinoVertices = input('quais os destinos? (separados por espaco)\n ').split(' ')
pesosVertices = list(map(int, input('quais os pesos das vertices? (separados por espaco e ordenados)\n').split(' ')))
matrizArestas = [] #define futura lista de listas que sera inserida pelo usuario para informar pesos das arestas que saem de cada vertice
for i in range(numVertices):
	matrizArestas.append(list(map(int, input('Peso das arestas que saem do vertice {}? (-1 indica a ausencia da aresta)\n'.format(i+1)).split(' '))))
'''


