import configuracion as config
import jugador
import random
import PySimpleGUI as sg
import string

ALTO=15
ANCHO=15

def letraRandom():
	result = random.choice(string.ascii_uppercase)
	return result


bolsa_fichas = {
	
	'a': {'cantidad':11 , 'valor': 1},
	'b': {'cantidad': 3, 'valor': 3},
	'c': {'cantidad': 4, 'valor': 2},
	'd': {'cantidad': 4, 'valor': 2},
	'e': {'cantidad': 11, 'valor': 1},
	'f': {'cantidad': 2, 'valor': 4},
	'g': {'cantidad': 2, 'valor': 2},
	'h': {'cantidad': 2, 'valor': 4},
	'i': {'cantidad': 6, 'valor': 1},
	'j': {'cantidad': 2, 'valor': 6},
	'k': {'cantidad': 1, 'valor': 8},
	'l': {'cantidad': 4, 'valor': 1},
	'll':{'cantidad': 1, 'valor': 8},
	'm': {'cantidad': 3, 'valor': 3},
	'n': {'cantidad': 5, 'valor': 1},
	'ñ': {'cantidad': 1, 'valor': 8},
	'o': {'cantidad': 8, 'valor': 1},
	'p': {'cantidad': 2, 'valor': 3},
	'q': {'cantidad': 1, 'valor': 8},
	'r': {'cantidad': 4, 'valor': 1},
	'rr':{'cantidad': 1, 'valor': 8},
	's': {'cantidad': 7, 'valor': 1},
	't': {'cantidad': 4, 'valor': 1},
	'u': {'cantidad': 6, 'valor': 1},
	'v': {'cantidad': 2, 'valor': 4},
	'w': {'cantidad': 1, 'valor': 8},
	'x': {'cantidad': 1, 'valor': 8},
	'y': {'cantidad': 1, 'valor': 4},
	'z': {'cantidad': 1, 'valor': 10},
}

def selecciono_random():
	return random.choice(list(bolsa_fichas.keys()))





randomcito = selecciono_random()
print(randomcito)
print(bolsa_fichas[randomcito]['valor'])
#___________________________________________#
#___________________________________________#
#___________________________________________#
jugador1 = jugador.Jugador()
maquina = jugador.Jugador()

comienza = random.choice((jugador1,maquina))
comienza.turno = True
print(comienza.turno)
if(comienza == maquina):
	comienza = jugador1

