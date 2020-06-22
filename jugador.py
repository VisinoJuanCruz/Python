class Jugador:
	#Atributos
	def __init__(self):
		self.fichas = []
		self.cant_fichas= 0
		self.cant_puntos = 0
		self.turno = False

	#Métodos
	def selecciona_ficha(mano,event):
		return mano[event[0][event[1]]]

	def selecciona_casillero(tablero,event):
		return casillero[event[0][event[1]]]


	def cant_fichas(self):
		return self.cant_fichas

	def cant_puntos(self):
		return self.cant_puntos

	def esTurno(self):
		return self.turno

	def tomar_fichas(self):
		self.cant_fichas+=1

	def sumar_puntos(self,cant):
		self.cant_puntos +=cant

	def dar_turno(self):
		self.turno = True

	def pasar_turno(self):
		self.turno = False