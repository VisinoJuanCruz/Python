import PySimpleGUI as sg
import ficha 
import random

letras_disponibles = ['a','a','a','a','a','a','a','a','a','a','a','b','b','b','c','c','c','c','d','d','d','d',
'e','e','e','e','e','e','e','e','e','e','e','f','f','g','g','h','h','i','i','i','i','i','i','i','i','j','j',
'k','l','l','l','l','m','m','m','n','n','n','n','n','o','o','o','o','o','o','o','o','p','p','q','r',
'r','r','r','rr','s','s','s','s','s','s','s','t','t','t','t','u','u','u','u','u','u','v','v','w','x','y','z']

def selecciono_random(letras_disponibles):
	letra = random.choice(letras_disponibles)
	letras_disponibles.remove(letra)
	return letra

def repartir_fichas(jugador,mano):
		
	while jugador.cant_fichas < len(mano.fichas[0]):
		for x in range(len(mano.fichas[0])):
			if mano.fichas[0][x].ButtonText == "":
				letra = selecciono_random(letras_disponibles).upper()
				mano.fichas[0][x].ButtonText = letra
				#window[mano.fichas[0][x].Key].Update(text=letra)
				jugador.sumar_ficha()
		

#window[list(coordenadas_mano)[-1]].update(text = "")
#for x in range(len(mano_propia.fichas[0])):
#			print(mano_propia.fichas[0][x].Key)

"""
def devolver_fichas(jugador,mano,window):
	
	while jugador.cant_fichas != len(mano.fichas[0]):
		for x in range(len(mano.fichas[0])):
			if mano.fichas[0][x].ButtonText != "":
				letras_disponibles.append(mano.fichas[0][x].ButtonText)
				window[mano_propia.fichas[0][x].Key].Update(text="")
				mano.fichas[0][x].ButtonText = ""
				jugador.restar_ficha()
"""


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

	def reponer(self,window,estructura):
		for x in estructura:
			window[x].update(text = selecciono_random(letras_disponibles).upper())
		estructura = {}

