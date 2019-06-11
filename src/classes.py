class Grafo:
	def __init__(self, arestas):
		self.edges = [make_edge(*edge) for edge in arestas]
