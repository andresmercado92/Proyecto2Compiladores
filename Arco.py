class Arco:
	"""docstring for Arco"""
	
	def __init__(self,estado_actual,estado_siguiente,caracter_transicion,nombre_arco,caracter_apilar):
		self.estado_actual=estado_actual
		self.estado_siguiente=estado_siguiente
		self.caracter_transicion=caracter_transicion
		self.nombre_arco=nombre_arco
		self.caracter_apilar=caracter_apilar

	def estadoActual(self):
		return self.estado_actual

	def estadoSiguiente(self):
		return self.estado_siguiente

	def caracterTransicion(self):
		return self.caracter_transicion

	def nombreArco(self):
		return self.nombre_arco

	def caracterApilar(self):
		return self.caracter_apilar		