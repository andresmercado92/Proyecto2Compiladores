from Pila import *
from Arco import *

class Automata_par:
	transicion_p=None
	transicion_q=None
	transicion_r=None
	arcos=[]

	def __init__(self,cadena):
		self.pila=Pila()
		self.bandera=False
		self.i=-1
		self.transicion_p=True
		self.transicion_q=False
		self.transicion_r=False
		self.palabra=cadena
		self.verificar()
		self.definir()

	def verificar(self):
		mitad=int(len(self.palabra)/2)
		if(len(self.palabra) % 2 == 0):
			cad1=self.palabra[:mitad]
			cad2=self.palabra[mitad:]
			if(cad1==cad2[::-1]):
				self.bandera=True

	def definir(self):
		arco=Arco('p','p','#','a','#a')
		self.arcos.append(arco)
		arco=Arco('p','p','#','b','#b')
		self.arcos.append(arco)
		#arco=Arco('p','p','a','a','aa')
		#self.arcos.append(arco)
		arco=Arco('p','q','a','a','e')
		self.arcos.append(arco)
		arco=Arco('p','p','a','b','ab')
		self.arcos.append(arco)
		arco=Arco('p','p','b','a','ba')
		self.arcos.append(arco)
		#arco=Arco('p','p','b','b','bb')
		#self.arcos.append(arco)
		arco=Arco('p','q','b','b','e')
		self.arcos.append(arco)
		arco=Arco('q','r','#','e','#')
		self.arcos.append(arco)
		arco=Arco('q','q','a','a','e')
		self.arcos.append(arco)
		arco=Arco('q','q','b','b','e')
		self.arcos.append(arco)

	def ejecucion(self,caracter_palabra,verifica):
		if(self.transicion_p==True and verifica==0):
			print("estoy en p")
			verifica=1
			for arco in self.arcos:
				if(arco.estadoActual()=='p' and arco.caracterTransicion()==self.pila.elementos[-1] and caracter_palabra==arco.nombreArco()):
					print(caracter_palabra+"\n")
					print(self.pila.elementos)
					self.pila.desapilar()
					print(self.pila.elementos)
					self.pila.apilar(arco.caracterApilar())
					print(self.pila.elementos)
					if(arco.estadoSiguiente()=='q'):
						self.transicion_p=False
						self.transicion_q=True
						self.transicion_r=False
					break


		if(self.transicion_q==True and verifica==0):
			print("estoy en q")
			verifica=1
			for arco in self.arcos:
				if(arco.estadoActual()=='q' and arco.caracterTransicion()==self.pila.elementos[-1] and caracter_palabra==arco.nombreArco()):
					print(self.pila.elementos)
					self.pila.desapilar()
					print(self.pila.elementos)
					self.pila.apilar(arco.caracterApilar())
					print(self.pila.elementos)
					if(arco.estadoSiguiente()=='r'):
						self.transicion_p=False
						self.transicion_q=False
						self.transicion_r=True
					break

		if(self.transicion_r==True):
			print("estoy en r")
			verifica=1

	def programa(self):
		for letras in self.palabra:
			if(self.transicion_r==False):
				print("lee "+letras+"\n")
				self.ejecucion(letras,0)
				print(self.transicion_p)
				print(self.transicion_q)
				print(self.transicion_r)
				if(self.transicion_r==True):
					break
			else:
				break

		if(self.pila.elementos[-1] == '#' and self.transicion_r==False and len(self.pila.elementos)==1):
			print("toma e")
			self.ejecucion('e',0)

		self.conclusion()

	def conclusion(self):
		if(self.transicion_r==True and self.bandera==True):
			print("es Palindromo")
		else:
			print("no es Palindromo")