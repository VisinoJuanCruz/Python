import PySimpleGUI as sg
import tablero as table
import casillero
import mano
import random
import jugador
import string
import pattern.es as pt

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

letras_disponibles = ['a','a','a','a','a','a','a','a','a','a','a','b','b','b','c','c','c','c','d','d','d','d',
'e','e','e','e','e','e','e','e','e','e','e','f','f','g','g','h','h','i','i','i','i','i','i','i','i','j','j',
'k','l','l','l','l','m','m','m','n','n','n','n','n','o','o','o','o','o','o','o','o','p','p','q','r',
'r','r','r','rr','s','s','s','s','s','s','s','t','t','t','t','u','u','u','u','u','u','v','v','w','x','y','z']

def palabra_existe(diccionario):
	palabra = ""
	for x in diccionario.values():
		palabra += x
	if (palabra.lower() in pt.verbs) or (palabra.lower() in pt.lexicon) or (palabra.lower() in pt.spelling):
		print(palabra , " EXISTE")

	else:print(palabra ," NO EXISTE")

def selecciono_random(letras_disponibles):
	letra = random.choice(letras_disponibles)
	letras_disponibles.remove(letra)
	bolsa_fichas[letra]['cantidad'] -= 1
	return letra
	


def repartir_fichas(jugador):
	if jugador == maquina:
		while maquina.cant_fichas < len(mano_rival.fichas[0]):
			for x in range(len(mano_rival.fichas[0])):
				if mano_rival.fichas[0][x].ButtonText == "":
					mano_rival.fichas[0][x].ButtonText = selecciono_random(letras_disponibles).upper()
					maquina.sumar_ficha()
	if jugador == jugador1:
		while jugador1.cant_fichas < len(mano_propia.fichas[0]):
			for x in range(len(mano_propia.fichas[0])):
				if mano_propia.fichas[0][x].ButtonText == "":
					mano_propia.fichas[0][x].ButtonText = selecciono_random(letras_disponibles).upper()
					mano_propia.fichas[0][x].ImageSubSample = 2
					jugador1.sumar_ficha()

"""
def reponer_fichas(window,estructura):
	for x in estructura:
		window[x].update(text = selecciono_random(letras_disponibles).upper())
"""
mano_rival = mano.Mano(True)
mano_propia = mano.Mano(False)
tablero =  table.Tablero(ALTO,ANCHO)

#fichas_del_rival
#mano_rival =  mano_rival.fichas
#fichas_del_jugador
#mano_propia =  mano_propia.fichas	


jugador1 = jugador.Jugador()
maquina = jugador.Jugador()


repartir_fichas(maquina)
repartir_fichas(jugador1)


punto = 100

#layout = [[sg.Text('ScrabbleAR GAME',size=(15,0),justification='center', font=("Helvetica", 25))]]
#layout += [[sg.Text("")]]
layout=mano_rival.fichas
layout += [[sg.Text(""),sg.Text("PUNTAJE:")]]
layout+=tablero.matriz
layout += [[sg.Text(""),sg.Text("PUNTAJE")]]
layout+=mano_propia.fichas#+[[sg.Button("PASAR TURNO",key="_PASARTURNO_")]]
layout+=[[sg.Button("PASAR TURNO",key="_PASARTURNO_"),sg.Button("CAMBIAR FICHAS",key="_CAMBIARFICHAS_")]]
#layout +=[[sg.Button("PASAR TURNO")]]


layout+= [[sg.Button("POSPONER", key = "_POSPONER_")]]
window = sg.Window("ScrabbleAR",layout,size=(1000,1000))



comienza = random.choice((jugador1,maquina))
comienza.turno = True


coordenadas = []
#MOMENTANEO
jugador1.turno = True
#print(len(mano_propia.fichas))
tablero.asignar_especiales()
movimiento = 0
def iniciar():
	while True:
		event,values = window.read()
		print(event,values)
		coordenadas_mano={}
		coordenadas_tablero = {}
		sentido = ''
		#print(len(coordenadas_mano.values()))
		while(jugador1.turno):
			if event is "_POSPONER_":
				jugador1.turno = False
				print ("Falta resolver funcionalidad")
				break
			
			
			#Desactivo las fichas de la mano una vez que seleccioné una.
			mano_propia.deshabilitar(window)
			if event is "_PASARTURNO_":

				jugador1.turno = False
				palabra_existe(coordenadas_mano)
				print(list(coordenadas_mano.keys()))
				for x in list(coordenadas_mano.keys()):
					window[x].update(text = "")
				
				mano_propia.reponer(window,list(coordenadas_mano.keys()))

				jugador1.turno = True
				#event, values = window.read()
				for x in list(coordenadas_tablero.keys()):
					del coordenadas_tablero[x]
				for x in list(coordenadas_mano.keys()):
					del coordenadas_mano[x]
				
			else:
				print("ESTA JUGANDO EN SU TURNO")
				coordenadas_mano[event] = window[event].ButtonText
				jugador1.cant_fichas = jugador1.cant_fichas - 1
				window[list(coordenadas_mano)[-1]].update(text = "")
				#print("Le paso las coordenadas del tablero: ", coordenadas_tablero)
				tablero.habilitar_botones(window,coordenadas_tablero)
						
				event, values = window.read()
				
				window[event].update(text = (list(coordenadas_mano.values())[-1]))
				tablero.estado_botones(window,True)
				mano_propia.habilitar(window,coordenadas_mano)
				
				coordenadas_tablero[event] = (list(coordenadas_mano)[-1])
				#print(coordenadas_mano)
			
				
			print("Fin")
		window.close()
		
		
		event, values = window.read()
		
		
		
		
		



		
		
	window.close()