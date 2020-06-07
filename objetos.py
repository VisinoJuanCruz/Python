#Clase Ficha
class Ficha:
	#Atributos
	def __init__(self):
		self.letra=""
		self.punto=0
		self.alto=ALTOFICHA
		self.ancho=ANCHOFICHA
	
	#Métodos
	def asignar_letra(self,letra):
		self.letra=letra

	def asignar_punto(self,punto):
		self.punto=punto 



#Clase Tablero
class Tablero:
	#Atributos
	def __init__(self):
		self.alto = ALTOTABLERO
		self.ancho = ANCHOTABLERO
		self.cant_casilla_con_premio=0
		self.cant_casilla_normal = 0
		self.cant_casilla_descuento = 0

	#Metodos
	def asignar_casilla_normal(self,cant):
		self.cant_casilla_normal = cant

	def asignar_casilla_descuento(self,cant):
		self.cant_casilla_descuento = cant

	def asignar_casilla_con_premio(self,cant):
		self.cant_casilla_con_premio = cant

	def cant_casilla_normal(self):
		return self.cant_casilla_normal

	def cant_casilla_con_descuento(self):
		return self.cant_casilla_con_descuento

	def cant_casilla_con_premio(self):
		return self.cant_casilla_con_premio

#Clase Jugador




#Clase Casilla
class Casilla:
	#Atributos
	def __init__(self,valor):
		self.valor = valor
		self.ocupada = False
	#Métodos
	def ocupar_casilla(self):
		self.ocupada = True

	def esta_ocupada(self):
		return self.ocupada