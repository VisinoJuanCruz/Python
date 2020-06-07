import PySimpleGUI as sg

class Casillero:
	def __init__(self, modificador_de_valor,alto,ancho):
		self.button = [sg.Button(button_color=("white","black"),size=(alto, ancho),key=(row,col))]
		self.modificador_de_valor = modificador_de_valor
		self.ficha_en_casillero = False
		

	def agregar_ficha(una_ficha):
		self.ficha_en_casillero = una_ficha

	def esta_ocupado():
		return self.ficha_en_casillero




    	#Clase Casilla
class Casilla:
	#Atributos
	def __init__(self,valor):
		self.valor = valor
		self.ocupada = False
	#Métodos


