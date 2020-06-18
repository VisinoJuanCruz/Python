import PySimpleGUI as sg
import ficha 

class Mano:
	def __init__(self,booleano):
		self.fichas = [[sg.Button(size=(3, 3), pad=(0,0), border_width=1, disabled = booleano,
			font='any 8') for col in range(7)] for row in range(1)]
		
		
		

	def agregar_ficha(self,ficha):
		self.cant_fichas += 1
		self.fichas[cant_fichas] = ficha


