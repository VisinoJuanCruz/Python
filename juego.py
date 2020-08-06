import PySimpleGUI as sg
import tablero as table

import random
import jugador
import string
import pattern.es as pt
import configuracion
import json










def iniciar():
	alto=15
	ancho=15
	import mano


	
	bolsa_fichas = mano.bolsa_letras
	



	def busca_palabra(diccionario_maquina):
		#diccionario_maquina = maquina.fichas
		palabras_validas = []
		for x in pt.spelling:
			palabras_validas.append(x.lower())
		for x in pt.verbs:
			palabras_validas.append(x.lower())
		for x in pt.lexicon:
			palabras_validas.append(x.lower())


		dict_values = []
		palabra_a_formar = []
		for x in diccionario_maquina.values():
			dict_values.append(x.lower())
		dict_values = set(dict_values)

		palabra_tamaño = -1
		palabra_a_formar = ""
		palabras_que_existen = pt
		for palabra in palabras_validas:
			posible = True
			letras = []
			
			coinciden = set(palabra) & dict_values
			if len(coinciden) == len(palabra):
				if palabra_tamaño < len(palabra):
					palabra_a_formar = palabra
					palabra_tamaño = len(palabra_a_formar)

		
		for letra in palabra_a_formar:
			for coorde in diccionario_maquina.keys():
				if diccionario_maquina[coorde] == letra.upper():
					maquina.fichas[coorde] = ""
					break
		maquina.cant_fichas -= len(palabra_a_formar)
		return palabra_a_formar

	def busca_lugar_en_tablero(palabra_a_formar):
		
		
		se_puede = False
		while not se_puede:
			se_puede = True

			casillero = random.choice(list(tablero.diccionario.keys()))	

			for x in range(len(palabra_a_formar)):
				try:
					tablero.diccionario[(casillero[0]+x,casillero[1])]
					if  not ((tablero.diccionario[(casillero[0]+x,casillero[1])] == "") and se_puede):
						se_puede = False
					
				except:
					se_puede = False
			if se_puede:
				direccion = "vertical"
				retorno = (casillero,"vertical")
				break
			if not se_puede:
				se_puede = True	
				
				for y in range(len(palabra_a_formar)):
					try:
						tablero.diccionario[(casillero[0],casillero[1]+y)]
						if  not ((tablero.diccionario[(casillero[0],casillero[1]+y)] == "") and se_puede):
							se_puede = False
						
					except:
						se_puede = False
			if se_puede:
				retorno = (casillero,"horizontal")
				break

		return retorno

	def escribo_palabra(tupla,palabra_a_formar):
		if tupla[1] == "vertical":
			for x in range(len(palabra_a_formar)):
				tablero.diccionario[tupla[0][0]+x,tupla[0][1]] = palabra_a_formar[x].upper()
				coordenadas_tablero[tupla[0][0]+x,tupla[0][1]] = palabra_a_formar[x].upper()
				
				
		else:
			for y in range(len(palabra_a_formar)):
				tablero.diccionario[tupla[0][0],tupla[0][1]+y] = palabra_a_formar[y].upper()
				coordenadas_tablero[tupla[0][0],tupla[0][1]+y] = palabra_a_formar[y].upper()
		#actualizar_puntos(maquina)
		#

	def turno_maquina(maquina):
		palabra = busca_palabra(maquina.fichas)
		mano.repartir_fichas(maquina,mano_rival)
		tupla = busca_lugar_en_tablero(palabra)
		escribo_palabra(tupla,palabra)
		actualizar_puntos(maquina)
		actualizar_puntajes()
		tablero.actualizar(window)
		maquina.turno = False
		jugador1.turno = True
		vacio_diccionario(coordenadas_palabra)
		vacio_diccionario(coordenadas_tablero)



	def guardo_info_de_tablero(tablero,info_guardada):
		
		tabla_diccionario = {}
		for x in tablero.diccionario:
			tabla_diccionario[str(x)] = tablero.diccionario[x]


		diccionario_tablero = {'coordenadas':tabla_diccionario,
								'alto':tablero.alto,
								'ancho':tablero.ancho}

		
		name_tabla= "tablero"
		info_guardada[name_tabla] = diccionario_tablero
	
	def guardo_info_de_jugador(jugador,info_guardada):
		diccionario_jugador = {'nombre':"",
								'fichas':"",
								'cant_fichas':"",
								'cant_puntos':"",
								'turno':"",
								'puntaje':""}

		diccionario_jugador['nombre'] = jugador.nombre
		diccionario_jugador['fichas'] = jugador.fichas
		diccionario_jugador['cant_fichas'] = jugador.cant_fichas
		diccionario_jugador['cant_puntos'] = jugador.cant_puntos
		diccionario_jugador['turno'] = jugador.turno
		diccionario_jugador['puntaje'] = jugador.puntaje

		info_guardada[jugador.nombre] = diccionario_jugador

	"""
	def guardo_mano_rival(mano_rival,info_guardada):
		info_guardada['mano rival'] = mano_rival

	def guardo_mano_propia(mano_propia,info_guardada):
		info_guardada['mano propia'] = mano_propia
	"""
	def guardo_json(diccionario_top10):
		with open('top10.json', 'w') as f:
			json.dump(diccionario_top10, f, indent=4)


	def actualizo_top10(nuevo_puntaje):
		with open('top10.json', 'r') as archivo:
			top10 = json.load(archivo)
			
			top10_valores = list(top10.values())
			top10_valores.append(nuevo_puntaje)
			top10_valores = sorted(top10_valores,reverse=True)
			
			print(top10_valores)

			for x in top10:
				top10[x] = top10_valores[int(x)-1]

			guardo_json(top10)


	def mostrar_top10():
		with open('top10.json', 'r') as archivo:
			top10 = json.load(archivo)
		print("TOP 10 PLAYERS")
		for x in top10:
			print("Top",x," es de ", top10[x], " puntos.")

	def cargar_datos(contenido):
		jugador1.nombre = contenido['jugador1']['nombre']
		jugador1.fichas =	contenido['jugador1']['fichas']
		jugador1.cant_fichas =contenido['jugador1']['cant_fichas']
		jugador1.cant_puntos =contenido['jugador1']['cant_puntos']
		jugador1.turno =contenido['jugador1']['turno']
		jugador1.puntaje = contenido['jugador1']['puntaje']

		maquina.nombre = contenido['maquina']['nombre']
		maquina.fichas =	contenido['maquina']['fichas']
		maquina.cant_fichas =contenido['maquina']['cant_fichas']
		maquina.cant_puntos =contenido['maquina']['cant_puntos']
		maquina.turno =contenido['maquina']['turno']
		maquina.puntaje = contenido['maquina']['puntaje']

		coorde_tabla = {}
		for x in contenido['tablero']['coordenadas']:
			coorde = tuple(int(num) for num in x.replace('(', '').replace(')', '').replace('...', '').split(', '))

			coorde_tabla[coorde] = contenido['tablero']['coordenadas'][x]

		tablero.diccionario = coorde_tabla


	def actualizar_top10():
		top10 = {}

		try:
			with open('configuration.json', 'w') as f:
				json.dump(contenido, f, indent=4)

		except:
			print("NO EXISTE")

	def mostrar_top10():
		pass

	def actualizar_puntos(jugador):
		"""Actualiza el puntaje en la Listbox"""

		for x in list(coordenadas_tablero.keys()):
			letra = coordenadas_tablero[x]
			
			if window[x].ButtonColor ==('yellow','yellow'):
				jugador.puntaje += (int(bolsa_fichas[letra.upper()]['valor'])) * 2
				
			else:
				if window[x].ButtonColor == ('black','black'):
					jugador.puntaje += int(bolsa_fichas[letra.upper()]['valor']) * 0.5
					
				else:
					jugador.puntaje += int(bolsa_fichas[letra.upper()]['valor'])
			
	def actualizar_puntajes():
		window["-PUNTAJERIVAL-"].Update(list(str(int(maquina.puntaje))))
		window["-PUNTAJEPROPIO-"].Update(list(str(int(jugador1.puntaje))))
	
	def recupero_datos():
		"""Si la palabra es erronea, se puede usar esta funcion para devolver el tablero y la mano a como estaba en el turno inicialmente. Se le pasa como parametro las coordenadas de tablero y de la mano utilizadas en este turno"""
		
		for x in list(coordenadas_palabra.keys()):
			jugador1.fichas[str(x)] = coordenadas_palabra[x]
			jugador1.cant_fichas +=  1
		for y in list(coordenadas_tablero.keys()):
			tablero.diccionario[y]= ""
		

	def palabra_existe(diccionario):
		"""Verifica si la palabra pasada existe, se le pasa como parametro un diccionario de tipo {coordenada:letra}, donde la coordenada es la ficha seleccionada de su mano."""
		nivel = 1
		palabra = ""
		for x in diccionario.values():
			palabra += x

		if nivel == 1:
			if (palabra.lower() in pt.verbs) or (palabra.lower() in pt.lexicon) or (palabra.lower() in pt.spelling):
				return True

			else:return False
		else:
			if nivel == 2:
				if (palabra.lower() in pt.verbs) or (palabra.lower() in pt.lexicon):
					return True
				else:
					return False
			else:
				if (palabra.lower() in pt.verbs):
					return True
				else:
					return False
	
	def vacio_diccionario(diccionario):
		"""Vacia el diccionario que se le pase por parametro"""
		for x in list(diccionario.keys()):
			del diccionario[x]
	
	def cambiar_mano(window,jugador):
		for x in range(len(mano_propia.fichas[0])):
			if jugador1.cant_fichas != 0:
				mano.letras_disponibles.append(mano_propia.fichas[0][x].ButtonText.lower())
				window[mano_propia.fichas[0][x].Key].Update(text="")
				jugador1.restar_ficha()
		for x in range(len(mano_propia.fichas[0])):
			if jugador1.cant_fichas < len(mano_propia.fichas[0]):
				if mano_propia.fichas[0][x].ButtonText == "":
					letra = mano.selecciono_random(mano.letras_disponibles).lower()
					window[mano_propia.fichas[0][x].Key].Update(text=letra.upper())
					jugador1.sumar_ficha()

	def actualizar_window(window,jugador):
		for x in jugador.fichas.keys():
			#window[int(x)].UpdateImageFileName = None
			window[int(x)].Update(text = jugador.fichas[x])



	def selecciono_ficha_mano():
		try:
			return (str(event)in jugador1.fichas.keys())
		except:
			return False

	def selecciono_casillero():
		return event in tablero.diccionario

	def turno_jugador():
		
		while jugador1.turno:
			window["_PASARTURNO_"].Update(disabled = False)
			window["_CAMBIARFICHAS_"].Update(disabled = False)
			window["_POSPONER_"].Update(disabled = False)
			

			event , values = window.read()
			
			while (event != "_PASARTURNO_") and (event != "_POSPONER_"):
				
				window["_CAMBIARFICHAS_"].Update(disabled = True)
				
				if event is "_TERMINAR_":
					programa = False
					actualizo_top10(jugador1.puntaje)
					window.close()
					break

				if event is "_CAMBIARFICHAS_":
					mano.cambiar_mano(jugador1)
					mano.actualizar(window,jugador1)
					event,values=window.read()
				
				


				
				if str(event) in jugador1.fichas.keys():

					coordenadas_palabra[event] = jugador1.fichas[str(event)]
					jugador1.restar_ficha()
					jugador1.fichas[str(event)] = ""
					mano_propia.deshabilitar(window)
					tablero.estado_botones(window,True)
					tablero.habilitar_botones(window,coordenadas_tablero)

					tablero.actualizar(window)

					
				
				if event in tablero.diccionario:
					
					coordenadas_tablero[event] = (list(coordenadas_palabra.values())[-1])
					tablero.diccionario[event] = (list(coordenadas_palabra.values())[-1])
					tablero.actualizar(window)
					
					tablero.estado_botones(window,True)
					mano_propia.habilitar(window,coordenadas_palabra)
					
				event, values = window.read()

			if event is "_POSPONER_":
				info_guardada = {}
				guardo_info_de_jugador(maquina,info_guardada)
				guardo_info_de_jugador(jugador1,info_guardada)
				guardo_info_de_tablero(tablero,info_guardada)
				#guardo_mano_propia(mano_propia,info_guardada)
				#guardo_mano_rival(mano_rival,info_guardada)
				
				
				
				with open('juegoguardado.json', 'w') as f:
					json.dump(info_guardada, f, indent=4)
				
			



			if event is "_PASARTURNO_":
				jugador1.turno = False
				maquina.turno = True
				if palabra_existe(coordenadas_palabra):
					actualizar_puntos(jugador1)
					actualizar_puntajes()
					mano.actualizar(window,jugador1)
					mano.repartir_fichas(jugador1,mano_propia)
					mano.actualizar(window,jugador1)
					vacio_diccionario(coordenadas_palabra)
					vacio_diccionario(coordenadas_tablero)
					window["_PASARTURNO_"].Update(disabled = True)
				else:
					sg.Popup("ERROR","La palabra ingresada no existe")
					recupero_datos()
					mano.actualizar(window,jugador1)
					vacio_diccionario(coordenadas_palabra)
					vacio_diccionario(coordenadas_tablero)
					mano_propia.deshabilitar(window)
					turno_maquina(maquina)
					vacio_diccionario(coordenadas_palabra)
					vacio_diccionario(coordenadas_tablero)
					mano_propia.habilitar(window,coordenadas_palabra)
			window["_PASARTURNO_"].Update(disabled = True)
			window["_CAMBIARFICHAS_"].Update(disabled = True)
			



	def preparo_tablero():
		"""Descuenta ficha, habilita tablero, deshabilita la mano."""
		
		var = str(event)
		coordenadas_palabra[event] = jugador1.fichas[var]
		
		jugador1.restar_ficha()
		jugador1.fichas[var] = ""
		mano_propia.deshabilitar(window)
		tablero.habilitar_botones(window,coordenadas_tablero)
		tablero.actualizar(window)

	def preparo_mano():
		"""Asigna letra en el tablero, deshabilita tablero, habilita mano."""
		coordenadas_posibles.remove(event)
		
		tablero.diccionario[event] = (list(coordenadas_palabra.values())[-1])
		
		tablero.actualizar(window)
		tablero.estado_botones(window,True)
		mano_propia.habilitar(window,coordenadas_palabra)
		coordenadas_tablero[event] = (list(coordenadas_palabra)[-1])
	
	def creo_mano(booleano):
		return [[sg.Button(str(""),size=(3, 3), pad=(0,0), border_width=1, disabled = booleano,
			font='any 8', key=(col)) for col in range(7)] for row in range(1)]

	matriz =  [[sg.Button(str(""),size=(3, 3),disabled=True,button_color= ('grey','grey') ,pad=(0,0), border_width=1,
				font='any 8',key=(row,col)) for col in range(alto)] for row in range(ancho)]
	

	mano_rival = mano.Mano(creo_mano(True))
	mano_propia = mano.Mano(creo_mano(False))
	
	
	diccionario_matriz = {}
	tablero =  table.Tablero(matriz,diccionario_matriz,alto,ancho)
	tablero.crear_diccionario()
	
	jugador1 = jugador.Jugador('jugador1')
	maquina = jugador.Jugador('maquina')

	diccionario_jugador1 = {}
	diccionario_maquina = {}

	
	for x in range(len(mano_rival.fichas[0])):
		diccionario_maquina[str(mano_rival.fichas[0][x].Key)] = ""

	for x in range(len(mano_propia.fichas[0])):
		diccionario_jugador1[str(mano_propia.fichas[0][x].Key)] = ""

	jugador1.crear_fichas(diccionario_jugador1)
	maquina.crear_fichas(diccionario_maquina)
	

	
	

	#DEFINO EL LAYUOT
	layout=mano_propia.fichas
	layout += [[sg.Text(""),sg.Text("PUNTAJE: "),sg.Listbox(values=[],key="-PUNTAJEPROPIO-", size=(25,1))]]
	layout+=tablero.matriz
	layout += [[sg.Text(""),sg.Text("PUNTAJE: "),sg.Listbox(values=[],key="-PUNTAJERIVAL-", size=(25,1))]]
	layout+=mano_rival.fichas
	layout+=[[sg.Button("COMENZAR",key="_COMENZAR_"),sg.Button("PASAR TURNO",key="_PASARTURNO_",disabled= True),sg.Button("CAMBIAR FICHAS",key="_CAMBIARFICHAS_",disabled = True),sg.Button("POSPONER", key = "_POSPONER_",disabled = True),sg.Button("TERMINAR",key="_TERMINAR_")]]
	
	window = sg.Window("ScrabbleAR",layout,size=(1000,1000))

	#Define quien comienza el turno. Por el  momento no se utiliza.
	comienza = random.choice((jugador1,maquina))
	comienza.turno = True
	
	#En lista_mano, guardo las keys de las fichas.
	lista_mano=[]
	for x in range(len(mano_propia.fichas[0])):
			lista_mano.append(mano_propia.fichas[0][x].Key)
	

	#En coordenadas_posibles, guardo las coordenadas del tablero que estan disponibles.
	coordenadas_posibles = []
	for x in range(len(tablero.matriz)):
				for y in range(len(tablero.matriz[x])):
					coordenadas_posibles.append(tablero.matriz[x][y].Key)
	


	tablero.asignar_especiales()
	movimiento = 0
	programa = True

	#
	

	while programa:
		
		try:
			with open('juegoguardado.json', 'r') as juegoguardado:
				contenido = json.load(juegoguardado)
				
			respuesta = sg.popup_yes_no(title="CONTINUAR?")
			if respuesta == "Yes":
				cargar_datos(contenido)
			else:
				pass

		except:
			sg.Popup("Pulse COMENZAR para iniciar el juego.")


		event,values = window.read()
		tablero.actualizar(window)
		
		if event is "_TERMINAR_":
			programa = False
			break

		if event == "_COMENZAR_":
			turno = random.choice((jugador1,maquina))
			comienza.turno = True
			mano.repartir_fichas(maquina,mano_rival)
			mano.repartir_fichas(jugador1,mano_propia)
			mano.actualizar(window,jugador1)
			window["_COMENZAR_"].Update(disabled = True)
			coordenadas_usadas=[]
			coordenadas_palabra={}
			coordenadas_tablero = {}
			sentido = ''
			

		while event != "_TERMINAR_" and event != "_POSPONER_":
			if maquina.turno:
				turno_maquina(maquina)
				mano.habilitar(window,jugador1)
				turno_jugador()
			
			else:
				mano.habilitar(window,jugador1)
				turno_jugador()
				turno_maquina(maquina)
				mano.habilitar(window,jugador1)

		
	window.close()

