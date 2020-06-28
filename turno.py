jugador1.turno = True
coordenadas = []
coordenadas_mano={}
coordenadas_tablero = {}
sentido = ''
#print(len(coordenadas_mano.values()))
while(jugador1.turno):

	
	event, values = window.read()
	print(event,values)
	if event is "_POSPONER_":
		jugador1.turno = False
		print ("Falta resolver funcionalidad")
		window.close()
	
	
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
		