import PySimpleGUI as sg
import ficha 

class Mano:
	def __init__(self,booleano):
		self.fichas = [[sg.Button(str(""),size=(3, 3), pad=(0,0), border_width=1, disabled = booleano,
			font='any 8', key=(col)) for col in range(7)] for row in range(1)]
		
		
		

	def agregar_ficha(self,ficha):
		self.cant_fichas += 1
		self.fichas[cant_fichas] = ficha

	def habilitar(self,window,estructura):
		lista_keys = list(estructura.keys())
		for x in self.fichas[0]:
			if (x.Key) not in lista_keys: 
				window[x.Key].Update(disabled = False)

	def deshabilitar(self,window):
		for x in self.fichas[0]:
			window[x.Key].Update(disabled = True)

	def cambiar_estado_botones(self,window,estado):
		for x in self.fichas[0]:
			window[x.Key].Update(disabled = estado)


