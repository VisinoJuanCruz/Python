import PySimpleGUI as sg
import random
import json

with open('configuration.json', 'r') as bolsa:
	contenido = json.load(bolsa)

		

bolsa_letras = contenido['bolsa_letras']
#Creo la bolsa con las letras disponibles
letras_disponibles = []
for letra in bolsa_letras:
	for cantidad in range(bolsa_letras[letra]['cantidad']):
		letras_disponibles.append(letra)



def selecciono_random(letras_disponibles):
	"""Retorna una letra sacada al azar de 'letras_disponibles'"""
	
	letra = random.choice(letras_disponibles)
	letras_disponibles.remove(letra)	
	return letra
	
		

	
	



def repartir_fichas(jugador,mano):
	"""Reparte fichas al jugador y la mano pasada como parametro"""
	salir = False
	while (jugador.cant_fichas < len(jugador.fichas.keys())) and not salir:
		for x in jugador.fichas:
			if jugador.fichas[x] == "":
				if len(letras_disponibles) == 0:
					sg.Popup("No hay mas letras. Fin del juego.")
					salir = True
					break
				else:
					letra = selecciono_random(letras_disponibles).upper()
					jugador.fichas[x] = letra
					jugador.sumar_ficha()

def cambiar_mano(jugador):
	"""Cambio las fichas de la mano de un jugador pasado como parametro"""
	while jugador.cant_fichas != 0:
		for x in jugador.fichas:
			letras_disponibles.append(jugador.fichas[x])
			
			jugador.fichas[x] = ""
			
			jugador.restar_ficha()
	
	while jugador.cant_fichas != 7:
		for x in jugador.fichas:
			letra = selecciono_random(letras_disponibles)
			jugador.fichas[x] = letra
			
			jugador.sumar_ficha()
def actualizar(window,jugador):
	"""Actualiza el layout"""
	for x in jugador.fichas.keys():
		if jugador.fichas[x] != "":
			letra = jugador.fichas[x]
			ruta = "./IconosFichas/"+letra+".png"
			window[int(x)].Update(text = jugador.fichas[x],image_filename=ruta,image_subsample = 4,image_size = (43,45))

def habilitar(window,jugador1):
	"""habilita la mano"""
	for x in jugador1.fichas.keys():
		window[int(x)].Update(disabled = False)


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

	def nueva_mano(self,window):
		for x in range(len(self.fichas[0])):
			if self.fichas[0][x].ButtonText != "":
				letras_disponibles.append(self.fichas[0][x].ButtonText)
				window[self.fichas[0][x]].update(text=selecciono_random(letras_disponibles).upper())

	def reponer(self,window,estructura):
		for x in estructura:
			window[x].update(text = selecciono_random(letras_disponibles).upper())
		estructura = {}

