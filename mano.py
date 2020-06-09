import PySimpleGUI as sg
import ficha 

class Mano:
	def __init__(self):
		self.fichas = [[sg.Button(size=(3, 3), pad=(0,0), border_width=1,
			font='any 8',key=(col)) for col in range(7)] for row in range(1)]
		
		self.cant_fichas = 0
		

	def agregar_ficha(self,ficha):
		self.cant_fichas += 1
		self.fichas[cant_fichas] = ficha


