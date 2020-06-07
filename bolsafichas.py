class BolsaFichas:
	#Atributos
	def __init__(self):
		self.cant_fichas_restantes=0
		self.esVacia = False


	#Métodos
	def descontar_ficha(self):
		self.cant_fichas_restantes -=1

	def cant_fichas_restantes(self):
		return self.cant_fichas_restantes
	

	def esVacia(self):
		return self.esVacia

	def asignar_cant_fichas(self,cant):
		self.cant_fichas_restantes=cant