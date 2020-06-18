import PySimpleGUI as sg
import tablero as table
import casillero
import mano
import random
import jugador
import string

ALTO=15
ANCHO=15

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


mano_rival = mano.Mano(True)
mano_propia = mano.Mano(False)
tablero =  table.Tablero(ALTO,ANCHO)

#fichas_del_rival
mano_rival =  mano_rival.fichas
#fichas_del_jugador
mano_propia =  mano_propia.fichas	

layout = [[sg.Text('ScrabbleAR GAME',size=(15,0),justification='center', font=("Helvetica", 25))]]
layout += [[sg.Text("")]]
layout+=mano_rival
layout += [[sg.Text("")]]		
layout+=tablero.matriz
layout += [[sg.Text("")]]
layout+=mano_propia



layout+= [[sg.Button("INICIAR")]]
window = sg.Window("ScrabbleAR",layout,size=(1000,1000))

jugador1 = jugador.Jugador()
maquina = jugador.Jugador()

comienza = random.choice((jugador1,maquina))
comienza.turno = True
print(jugador1.turno)
print(maquina.turno)
coordenadas = []
#print(len(mano_propia.fichas))
tablero.asignar_especiales()
while True:
	
	#while(jugador1.esTurno()):
	#tablero.desabilitar_botones(window)
	#window[(7,7)].update(disabled = False)
	sentido = ''
	event, values = window.read()
	print(event, values)
	coordenadas.append(event)
	window[event].update(text=selecciono_random().upper(), button_color=('red','black'))
	#tablero.desabilitar_botones(window)
	#tablero.habilitar_botones(window,sentido,coordenadas)
	#if inicio == True:
	#	tablero.asignar_especiales(window)
	#	inicio = False
	print(window[event].ButtonText)

	



	
	
window.close()