import PySimpleGUI as sg



#Clase Tablero
class Tablero:
	#Atributos
	def __init__(self,alto,ancho):
		self.matriz = [[sg.Button(str(""),size=(3, 3),disabled=True,button_color= ('grey','grey') ,pad=(0,0), border_width=1,
			font='any 8',key=(row,col)) for col in range(alto)] for row in range(ancho)]
		self.alto = alto
		self.ancho = ancho
		
	

	
	def estado_botones(self,window,estado):
		"""Cambia el estado de los botones"""
		
		for x in range(self.alto):
			for y in range(self.ancho):
				window[x,y].update(disabled=estado)
	
	def sentido(self,lista_keys):
		"""Verifica en que sentido se va a escribir la palabra"""
		if len(lista_keys) == 0:
			return "cero"
		elif(len(lista_keys) == 1):
			return "uno"

		elif(lista_keys[-1][0] > lista_keys[-2][0]):
			return "vertical"
		else:
			return "horizontal"
	

	def habilitar_botones(self,window,estructura):
		"""Habilita los casilleros del teclado disponibles para jugar. Dependiendo el sentido en el que el jugador este formando la palabra"""

		lista_keys = list(estructura.keys())
		
		if self.sentido(lista_keys) == "cero":
			self.estado_botones(window,False)
		elif self.sentido(lista_keys) == "uno":
			if int(lista_keys[-1][0]+1)<self.alto:
				window[lista_keys[-1][0]+1,lista_keys[-1][1]].update(disabled = False)
			if int(lista_keys[-1][1]+1)<self.ancho:
				window[lista_keys[-1][0],lista_keys[-1][1]+1].update(disabled = False)
		elif (self.sentido(lista_keys) == "vertical") and (lista_keys[-1][0]+1 < self.alto):
			window[lista_keys[-1][0]+1,lista_keys[-1][1]].update(disabled = False)
		elif (self.sentido(lista_keys) == "horizontal") and (lista_keys[-1][1]+1 < self.ancho):
			window[lista_keys[-1][0],lista_keys[-1][1]+1].update(disabled = False)
			
	
		
		
	def asignar_especiales(self):
		"""Asigna casilleros con descuento y con premio"""
		for x in range(self.alto):
			for y in range(self.ancho):
				if ((x ==y) or ((x+y)== self.ancho-1)) :
					self.matriz[x][y].ButtonColor=('yellow','yellow')
				if ((x == 0) or (x==7) or (x==14)) and ((y == 0) or (y==7) or (y==14)):
					self.matriz[x][y].ButtonColor=('black','black')
				if ((x ==7) and (y==7)):
					self.matriz[x][y].ButtonColor=('red','red')

