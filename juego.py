import PySimpleGUI as sg
import tablero as table
import casillero
import mano
import random
import jugador
import string
import pattern.es as pt


def iniciar():
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

	def actualizar_puntos(listbox,puntos):
		for x in list(puntos):
			listbox.Update(x)
	"""
	letras_disponibles = ['a','a','a','a','a','a','a','a','a','a','a','b','b','b','c','c','c','c','d','d','d','d',
	'e','e','e','e','e','e','e','e','e','e','e','f','f','g','g','h','h','i','i','i','i','i','i','i','i','j','j',
	'k','l','l','l','l','m','m','m','n','n','n','n','n','o','o','o','o','o','o','o','o','p','p','q','r',
	'r','r','r','rr','s','s','s','s','s','s','s','t','t','t','t','u','u','u','u','u','u','v','v','w','x','y','z']
	"""
	def palabra_existe(diccionario):
		palabra = ""
		for x in diccionario.values():
			palabra += x
		if (palabra.lower() in pt.verbs) or (palabra.lower() in pt.lexicon) or (palabra.lower() in pt.spelling):
			return True

		else:return False
	

	mano_rival = mano.Mano(True)
	mano_propia = mano.Mano(False)
	tablero =  table.Tablero(ALTO,ANCHO)

	


	jugador1 = jugador.Jugador('jugador1')
	maquina = jugador.Jugador('maquina')


	mano.repartir_fichas(maquina,mano_rival)
	mano.repartir_fichas(jugador1,mano_propia)



	punto = 100

	
	layout=mano_rival.fichas
	layout += [[sg.Text(""),sg.Text("PUNTAJE: "),sg.Listbox(values=[],key="-PUNTAJERIVAL-", size=(25,0))]]
	layout+=tablero.matriz
	layout += [[sg.Text(""),sg.Text("PUNTAJE: "),sg.Listbox(values=[],key="-PUNTAJEPROPIO-", size=(25,0))]]
	layout+=mano_propia.fichas
	layout+=[[sg.Button("PASAR TURNO",key="_PASARTURNO_"),sg.Button("CAMBIAR FICHAS",key="_CAMBIARFICHAS_"),sg.Button("POSPONER", key = "_POSPONER_"),sg.Button("VOLVER AL MENU",key="_VOLVER_")]]
	


	
	window = sg.Window("ScrabbleAR",layout,size=(1000,1000))
	


	comienza = random.choice((jugador1,maquina))
	comienza.turno = True
	lista_mano=[]
	for x in range(len(mano_propia.fichas[0])):
			lista_mano.append(mano_propia.fichas[0][x].Key)
	


	coordenadas_posibles = []
	for x in range(len(tablero.matriz)):
				for y in range(len(tablero.matriz[x])):
					coordenadas_posibles.append(tablero.matriz[x][y].Key)
	
	jugador1.turno = True
	
	tablero.asignar_especiales()
	movimiento = 0
	program = True

	while program:
		
		
		coordenadas_usadas=[]
		coordenadas_mano={}
		coordenadas_tablero = {}
		sentido = ''
		
		while(jugador1.turno):
			event,values = window.read()
			

			if event is "_POSPONER_":
				jugador1.turno = False
				sg.Popup("ERROR","Falta resolver funcionalidad")
				print ("Falta resolver funcionalidad")
				break
			
			
			
			if event is "_VOLVER_":	
				program = False
				window.close()

			if event is "_CAMBIARFICHAS_":
				
				for x in range(len(mano_propia.fichas[0])):
						if jugador1.cant_fichas != 0:
							mano.letras_disponibles.append(mano_propia.fichas[0][x].ButtonText)
							window[mano_propia.fichas[0][x].Key].Update(text="")
							jugador1.restar_ficha()
						
				
				for x in range(len(mano_propia.fichas[0])):
					if jugador1.cant_fichas < len(mano_propia.fichas[0]):
						if mano_propia.fichas[0][x].ButtonText == "":
							letra = mano.selecciono_random(mano.letras_disponibles).lower()
							window[mano_propia.fichas[0][x].Key].Update(text=letra.upper())
							jugador1.sumar_ficha()
				

				
			if event is "_PASARTURNO_":
				puntaje = 0
				jugador1.turno = False
				if palabra_existe(coordenadas_mano):
					for x in list(coordenadas_mano.keys()):
						letra = coordenadas_mano[x].lower()
						for y in list(coordenadas_tablero.keys()):
							if coordenadas_tablero[y] is x:
								if tablero.matriz[int(y[0])][int(y[1])].ButtonColor ==('yellow','yellow'):
									puntaje += int(bolsa_fichas[letra]['valor']) * 2
								else:
									if tablero.matriz[int(y[0])][int(y[1])].ButtonColor == ('black','black'):
										puntaje += int(bolsa_fichas[letra]['valor']) * 0.5
									else:
										puntaje += int(bolsa_fichas[letra]['valor'])
							
					window["-PUNTAJEPROPIO-"].Update(list(str(puntaje)))
				else:
					print(" NO EXISTE")	
					print(coordenadas_mano)
					print(coordenadas_tablero)
					for x in list(coordenadas_mano.keys()):
						window[x].update(text= coordenadas_mano[x])
					for y in list(coordenadas_tablero.keys()):
						window[y].update(text = "")
					print("YA  ACOMODE TODO")

				for x in list(coordenadas_tablero.keys()):
					del coordenadas_tablero[x]
				for x in list(coordenadas_mano.keys()):
					del coordenadas_mano[x]
				mano_propia.deshabilitar(window)
				jugador1.turno= True
			if str(event) in lista_mano:
				print("SELECCIONO FICHA DE MANO")
				coordenadas_mano[event] = window[event].ButtonText
				jugador1.restar_ficha()
				window[list(coordenadas_mano)[-1]].update(text = "")
				mano_propia.deshabilitar(window)
				tablero.habilitar_botones(window,coordenadas_tablero)
				print(coordenadas_mano)
				
				
				
			if event in coordenadas_posibles:
				coordenadas_posibles.remove(event)
				print("PUSO FICHA SELECCIONADA EN TABLERO")
				window[event].update(text = (list(coordenadas_mano.values())[-1]))
				tablero.estado_botones(window,True)
				mano_propia.habilitar(window,coordenadas_mano)
				
				coordenadas_tablero[event] = (list(coordenadas_mano)[-1])
					
	window.close()

		
		
		
		
		
		
		
		



		
		


