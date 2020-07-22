class Jugador:
	#Atributos
	def __init__(self,nombre):
		self.nombre = nombre
		self.fichas = []
		self.cant_fichas= 0
		self.cant_puntos = 0
		self.turno = False

	#Métodos
	
	def cant_fichas(self):
		"""Retorna la cantidad de fichas."""
		return self.cant_fichas

	def cant_puntos(self):
		"""Retorna la cantidad de puntos"""
		return self.cant_puntos

	def esTurno(self):
		"""Retorna True si es su turno"""
		return self.turno

	def sumar_ficha(self):
		"""Suma una ficha"""
		self.cant_fichas += 1

	def restar_ficha(self):
		"""Resta una ficha"""
		self.cant_fichas -= 1

	def sumar_puntos(self,cant):
		"""Suma puntos"""
		self.cant_puntos +=cant

	def dar_turno(self):
		"""Asigna turno"""
		self.turno = True

	def pasar_turno(self):
		"""Le quita el turno"""
		self.turno = False