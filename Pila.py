class Pila:
	
	def __init__(self):
		self.elementos=['#']

	def apilar(self,palabra):
		for caracteres in palabra:
			if(caracteres!='e'):
				self.elementos.append(caracteres)

	def desapilar(self):
			return self.elementos.pop()

