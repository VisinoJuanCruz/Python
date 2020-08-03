import PySimpleGUI as sg
import tablero as table
import mano
import random
import jugador
import string
import pattern.es as pt
import configuracion



def iniciar():
	ALTO=15
	ANCHO=15


	"""
	diccionario_maquina={"0":"","1":"","2":"","3":"","4":"","5":"","6":""}
	diccionario_jugador1= {"00":"","11":"","22":"","33":"","44":"","55":"","66":""}
	"""
	bolsa_fichas = mano.bolsa_letras

	
	import pattern.es as pt


	def busca_palabra(diccionario_maquina):
		#diccionario_maquina={"0":"P","1":"A","2":"E","3":"R","4":"O","5":"B","6":"S"}
		dict_values = []
		palabra_a_formar = []
		print("las fichas de la maquina cuando arranca: ", maquina.fichas)
		for x in diccionario_maquina.values():
			dict_values.append(x.lower())
		dict_values = set(dict_values)

		palabra_tamaño = -1
		palabra_a_formar = ""
		for palabra in pt.spelling:
			posible = True
			letras = []
			#palabra = set(palabra)
			
			coinciden = set(palabra) & dict_values
			#print(coinciden, len(coinciden))
			if len(coinciden) == len(palabra):
				if palabra_tamaño < len(palabra):
					palabra_a_formar = palabra
					palabra_tamaño = len(palabra_a_formar)

		for letra in palabra_a_formar:
			for coorde in diccionario_maquina.keys():
				if diccionario_maquina[coorde] == letra.upper():
					maquina.fichas[coorde] = ""
		maquina.cant_fichas -= len(palabra_a_formar)
		mano.repartir_fichas(maquina,mano_rival)
		print("las fichas de la maquina cuando termina: ", maquina.fichas)


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
				coordenadas_palabra[tupla[0][0]+x,tupla[0][1]] = palabra_a_formar[x].upper()
				
		else:
			for y in range(len(palabra_a_formar)):
				tablero.diccionario[tupla[0][0],tupla[0][1]+y] = palabra_a_formar[y].upper()
				coordenadas_palabra[tupla[0][0],tupla[0][1]+y] = palabra_a_formar[y].upper()
				print(tupla[0][0],tupla[0][1]+y)
	
	def turno_maquina():
		palabra = busca_palabra(maquina.fichas)
		#print("mano antes de repartir :", maquina.fichas)
		mano.repartir_fichas(maquina,mano_rival)
		#print("mano despues de repartir :", maquina.fichas)

		tupla = busca_lugar_en_tablero(palabra)
		escribo_palabra(tupla,palabra)
		tablero.actualizar(window)
		maquina.turno = False
		jugador1.turno = True

	#def calcular_puntaje_palabra(diccionario):
	#	for x in palabra:


	

	def actualizar_puntos():
		"""Actualiza el puntaje en la Listbox"""

		for x in list(coordenadas_palabra.keys()):
			letra = coordenadas_palabra[x].lower()
			for y in list(coordenadas_tablero.keys()):
				if coordenadas_tablero[y] is x:
					if tablero.matriz[int(y[0])][int(y[1])].ButtonColor ==('yellow','yellow'):
						jugador1.puntaje += (int(bolsa_fichas[letra.upper()]['valor'])) * 2
					else:
						if tablero.matriz[int(y[0])][int(y[1])].ButtonColor == ('black','black'):
							jugador1.puntaje += int(bolsa_fichas[letra.upper()]['valor']) * 0.5
						else:
							jugador1.puntaje += int(bolsa_fichas[letra.upper()]['valor'])
	
	def actualizar_puntajes():
		window["-PUNTAJERIVAL-"].Update(list(str(int(maquina.puntaje))))
		window["-PUNTAJEPROPIO-"].Update(list(str(int(jugador1.puntaje))))
	
	def recupero_datos():
		"""Si la palabra es erronea, se puede usar esta funcion para devolver el tablero y la mano a como estaba en el turno inicialmente. Se le pasa como parametro las coordenadas de tablero y de la mano utilizadas en este turno"""
		for x in list(coordenadas_palabra.keys()):
			window[x].update(text= coordenadas_palabra[x])
		for y in list(coordenadas_tablero.keys()):
			window[y].update(text = "")


	def palabra_existe(diccionario):
		"""Verifica si la palabra pasada existe, se le pasa como parametro un diccionario de tipo {coordenada:letra}, donde la coordenada es la ficha seleccionada de su mano."""
		palabra = ""
		for x in diccionario.values():
			palabra += x
		#print("LA PALABRA FORMADA ES : ",palabra)
		if (palabra.lower() in pt.verbs) or (palabra.lower() in pt.lexicon) or (palabra.lower() in pt.spelling):
			return True

		else:return False
	
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
			window[int(x)].Update(text = jugador.fichas[x])



	def selecciono_ficha_mano():
		try:
			return (str(event)in jugador1.fichas.keys())
		except:
			return False

	def selecciono_casillero():
		return event in tablero.diccionario

	def turno_jugador():
		
		window["_PASARTURNO_"].Update(disabled = False)
		window["_CAMBIARFICHAS_"].Update(disabled = False)
		

		event , values = window.read()
		
		while event != "_PASARTURNO_" or event != "_POSPONER_":

			window["_PASARTURNO_"].Update(disabled = True)
			window["_CAMBIARFICHAS_"].Update(disabled = True)
			print("ENTRO")

			if event is "_CAMBIARFICHAS_":
				mano.cambiar_mano(jugador1)
				mano.actualizar(window,jugador1)
			
			print("KEKEKE: ", (str(event) in jugador1.fichas.keys()))
			if str(event) in jugador1.fichas.keys():
				print("TOQUE FICHA")
				coordenadas_palabra[event] = jugador1.fichas[str(event)]
				#print("coordenadas de la palabra: ", coordenadas_palabra)
				jugador1.restar_ficha()
				jugador1.fichas[str(event)] = ""
				mano_propia.deshabilitar(window)
				tablero.habilitar_botones(window,coordenadas_tablero)
				tablero.actualizar(window)

			event, values = window.read()
			print(type(event))
			print(type(tablero.diccionario.keys()))
			print("LOLOLOLOL ? :", (event in tablero.diccionario))
			if event in tablero.diccionario:
				print("AHORA TOQUE TABLERO")
				coordenadas_tablero[event] = (list(coordenadas_palabra.values())[-1])
				tablero.diccionario[event] = (list(coordenadas_palabra.values())[-1])
				tablero.actualizar(window)
				tablero.estado_botones(window,True)
				mano_propia.habilitar(window,coordenadas_palabra)
				coordenadas_tablero[event] = (list(coordenadas_palabra)[-1])

			window["_PASARTURNO_"].Update(disabled = False)
			window["_CAMBIARFICHAS_"].Update(disabled = False)
			
			



	def preparo_tablero():
		"""Descuenta ficha, habilita tablero, deshabilita la mano."""
		
		var = str(event)
		coordenadas_palabra[event] = jugador1.fichas[var]
		
		jugador1.restar_ficha()
		#print("La letra en la posicion :", var, "es: ", jugador1.fichas[var])
		jugador1.fichas[var] = ""
		#print("La letra en la posicion :", var, "ahora es: ", jugador1.fichas[var])
		#window[list(coordenadas_palabra)[-1]].update(disabled = True)
		mano_propia.deshabilitar(window)
		tablero.habilitar_botones(window,coordenadas_tablero)
		tablero.actualizar(window)

	def preparo_mano():
		"""Asigna letra en el tablero, deshabilita tablero, habilita mano."""
		coordenadas_posibles.remove(event)
		#print("A VER QUE HAY ACA: ",list(coordenadas_palabra.values())[-1])

		tablero.diccionario[event] = (list(coordenadas_palabra.values())[-1])
		tablero.actualizar(window)
		#window[event].update(text = (list(coordenadas_palabra.values())[-1]))
		tablero.estado_botones(window,True)
		mano_propia.habilitar(window,coordenadas_palabra)
		coordenadas_tablero[event] = (list(coordenadas_palabra)[-1])
		print(tablero.diccionario)
		


	#def turno_maquina():


	mano_rival = mano.Mano(True)
	mano_propia = mano.Mano(False)
	tablero =  table.Tablero(ALTO,ANCHO)
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
	

	
	#print(mano_propia.fichas[0][0].Key)
	#print(mano_rival.fichas[0][0].Key)
	

	#DEFINO EL LAYUOT
	layout=mano_propia.fichas
	layout += [[sg.Text(""),sg.Text("PUNTAJE: "),sg.Listbox(values=[],key="-PUNTAJEPROPIO-", size=(25,0))]]
	layout+=tablero.matriz
	layout += [[sg.Text(""),sg.Text("PUNTAJE: "),sg.Listbox(values=[],key="-PUNTAJERIVAL-", size=(25,0))]]
	layout+=mano_rival.fichas
	layout+=[[sg.Button("COMENZAR",key="_COMENZAR_"),sg.Button("PASAR TURNO",key="_PASARTURNO_",disabled= True),sg.Button("CAMBIAR FICHAS",key="_CAMBIARFICHAS_",disabled = True),sg.Button("POSPONER", key = "_POSPONER_",disabled = True),sg.Button("VOLVER AL MENU",key="_VOLVER_")]]
	
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
	


	#jugador1.turno = True
	tablero.asignar_especiales()
	movimiento = 0
	program = True

	#
	

	while program:
		
		#busca_lugar_en_tablero()
		event,values = window.read()
		print("TOCÓ :", event)
		tablero.actualizar(window)
		
		if event is "_VOLVER_":
			program = False
			break

		if event == "_COMENZAR_":
			turno = random.choice((jugador1,maquina))
			comienza.turno = True
			#jugador1.turno = True
			mano.repartir_fichas(maquina,mano_rival)
			mano.repartir_fichas(jugador1,mano_propia)
			mano.actualizar(window,jugador1)
			#for x in jugador1.fichas.keys():
			#	window[int(x)].Update(text = jugador1.fichas[x])


		coordenadas_usadas=[]
		coordenadas_palabra={}
		coordenadas_tablero = {}
		sentido = ''
		
		print(maquina.turno)
		print(jugador1.turno)
		print("IA FICHAS: ",maquina.fichas)
		print("Jugador FICHAS: ", jugador1.fichas)
		if maquina.turno:
			turno_maquina()
			turno_jugador()
		else:
			turno_jugador()
			turno_maquina()
		
		"""
		if (comienza == maquina) or (comienza == jugador1):
			
			
			
			
			comienza.turno = False
			comienza = jugador1
			jugador1.turno = True
			
			
			for x in jugador1.fichas.keys():
				print(x)
		"""
		while(jugador1.turno):
			event,values = window.read()
			
			
			#POSPONER JUEGO
			if event is "_POSPONER_":
				#jugador1.turno = False
				sg.Popup("ERROR","Falta resolver funcionalidad")
				print ("Falta resolver funcionalidad")
				event,values = window.read()
				break
			
			
			#SALIR AL MENU PRINCIPAL
			if event is "_VOLVER_":
				program = False
				break
				


			#CAMBIAR FICHAS
			if event is "_CAMBIARFICHAS_":
				#jugador1.turno = False
				mano.cambiar_mano(jugador1)
				mano.actualizar(window,jugador1)
				event,values = window.read()
				
				
			

			#TERMINAR TURNO	
			if event is "_PASARTURNO_":
				puntaje = 0
				jugador1.turno = False
				if palabra_existe(coordenadas_palabra):
					actualizar_puntos()
					actualizar_puntajes()
					mano.actualizar(window,jugador1)

					print("Despues de repartir las fichas :", jugador1.fichas)
					mano.repartir_fichas(jugador1,mano_propia)
					
					mano.actualizar(window,jugador1)
					print("despues del turno: " , jugador1.fichas)



				else:
					sg.Popup("ERROR","La palabra ingresada no existe")
					recupero_datos()
				print("coordendadas_palabra: ", coordenadas_palabra)
				vacio_diccionario(coordenadas_palabra)
				vacio_diccionario(coordenadas_tablero)
				print("coordenadas_palabra",coordenadas_palabra)
				mano_propia.deshabilitar(window)
				jugador1.turno= False
				maquina.turno = True
				turno_maquina()
				vacio_diccionario(coordenadas_palabra)
				vacio_diccionario(coordenadas_tablero)
				mano_propia.habilitar(window,coordenadas_palabra)
				print(coordenadas_palabra)



			#turno_jugador()



			#EL JUGADOR ESTA EN SU TURNO.
			#if #selecciono_ficha_mano():
				#print("SELECCIONO FICHA MANO")
				#preparo_tablero()
				#print("PREPARÉ CASILLERO")
				#print("Ahora tengo que leer algo:")
				#event,values = window.read()
				#print(event)
				#print(type(event))

			#if selecciono_casillero():
				#print("SELECCIONO CASILLERO")
				#preparo_mano()
				#print("PREPARE LA MANO")
				#print("YA PUSE LA FICHA Y ESTOY ESPERANDO A QUE REALICE UNA ACCIONT")
				
					
	window.close()

		
		
		
		
		
		
		
		



		
		


