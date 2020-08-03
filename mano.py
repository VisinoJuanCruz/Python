import PySimpleGUI as sg
import random
import json

with open('configuration.json', 'r') as bolsa:
	bolsa_letras = json.load(bolsa)

	bolsa.close()	


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

	#print("Acá llega")
	while jugador.cant_fichas < len(jugador.fichas.keys()):
		for x in jugador.fichas:
			if jugador.fichas[x] == "":
				#print("KEKEKE : ",jugador.cant_fichas)
				letra = selecciono_random(letras_disponibles).upper()
				jugador.fichas[x] = letra
				#window[mano.fichas[0][x].Key].Update(text=letra)
				jugador.sumar_ficha()
	#print("El jugador ",jugador.nombre," queda con ",jugador.cant_fichas," fichas.")

def cambiar_mano(jugador):
	#print("La mano de ",jugador.nombre," estaba así: ",jugador.fichas)
	while jugador.cant_fichas != 0:
		for x in jugador.fichas:
			letras_disponibles.append(jugador.fichas[x])
			print("habia",jugador.fichas[x])
			jugador.fichas[x] = ""
			
			jugador.restar_ficha()
	
		#mano.letras_disponibles.append(mano_propia.fichas[0][x].ButtonText.lower())
		#window[mano_propia.fichas[0][x].Key].Update(text="")
	while jugador.cant_fichas != 7:
		for x in jugador.fichas:
			letra = selecciono_random(letras_disponibles)
			jugador.fichas[x] = letra
			print("En la coodenada : ",x,"de las fichas del jugador, hay",jugador.fichas[x])
			#window[mano_propia.fichas[0][x].Key].Update(text=letra.upper())
			jugador.sumar_ficha()
	#print("La mano de ",jugador.nombre," quedó así: ",jugador.fichas)
	print("SE CAMBIO LA MANO DEL JUGADOR : ", jugador)
def actualizar(window,jugador):
	for x in jugador.fichas.keys():
		window[int(x)].Update(text = jugador.fichas[x])

def habilitar(window,jugador1):
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

