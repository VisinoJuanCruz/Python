import PySimpleGUI as sg
import juego
import json

#background = '#000000'
#sg.SetOptions(background_color=background, element_background_color=background)
#sg.theme_previewer()
def iniciar():
	
	with open('configuration.json', 'r') as archivo:
		contenido = json.load(archivo)

		
	
	dificultad = contenido['dificultad']#['DIFICULTAD']
	tiempo = contenido['tiempo']#['TIEMPO']
	bolsa_letras = contenido['bolsa_letras']
	diametro = contenido['diametro']
	print(diametro)
	
	sg.theme('Light Brown 9')
	layout = [[sg.Text("")],
			  [sg.Text("")],
			  [sg.Text(" "),sg.Button("",image_filename="./IconosFichas/configuracion.png",disabled=False),sg.Text(" "*10)],
			  [sg.Text("")],
			  [sg.Text("CANTIDAD DE LETRAS :")],
			  [sg.Text("A:  "),sg.Input(bolsa_letras['A']['cantidad'],key="CANT-A",size=(5,5)),sg.Text("    "),sg.Text("B: "),sg.Input(bolsa_letras['B']['cantidad'],key="CANT-B",size=(5,5)),sg.Text("     "),sg.Text("C: "),sg.Input(bolsa_letras['C']['cantidad'],key="CANT-C",size=(5,5)),sg.Text("     "),sg.Text("D:  "),sg.Input(bolsa_letras['D']['cantidad'],key="CANT-D",size=(5,5)),sg.Text("     "),sg.Text("E:  "),sg.Input(bolsa_letras['E']['cantidad'],key="CANT-E",size=(5,5)),sg.Text("     "),sg.Text("F:    "),sg.Input(bolsa_letras['F']['cantidad'],key="CANT-F",size=(5,5))],#sg.Text("(Facil,Medio,Dificil)")],
			  [sg.Text("G:  "),sg.Input(bolsa_letras['G']['cantidad'],key="CANT-G",size=(5,5)),sg.Text("     "),sg.Text("H: "),sg.Input(bolsa_letras['H']['cantidad'],key="CANT-H",size=(5,5)),sg.Text("     "),sg.Text("I:  "),sg.Input(bolsa_letras['I']['cantidad'],key="CANT-I",size=(5,5)),sg.Text("     "),sg.Text("J:   "),sg.Input(bolsa_letras['J']['cantidad'],key="CANT-J",size=(5,5)),sg.Text("     "),sg.Text("K: "),sg.Input(bolsa_letras['K']['cantidad'],key="CANT-K",size=(5,5)),sg.Text("      "),sg.Text("L:   "),sg.Input(bolsa_letras['L']['cantidad'],key="CANT-L",size=(5,5))],
			  [sg.Text("LL: "),sg.Input(bolsa_letras['LL']['cantidad'],key="CANT-LL",size=(5,5)),sg.Text("     "),sg.Text("M:"),sg.Input(bolsa_letras['M']['cantidad'],key="CANT-M",size=(5,5)),sg.Text("     "),sg.Text("N:  "),sg.Input(bolsa_letras['N']['cantidad'],key="CANT-N",size=(5,5)),sg.Text("     "),sg.Text("Ñ:  "),sg.Input(bolsa_letras['Ñ']['cantidad'],key="CANT-Ñ",size=(5,5)),sg.Text("     "),sg.Text("O: "),sg.Input(bolsa_letras['O']['cantidad'],key="CANT-O",size=(5,5)),sg.Text("     "),sg.Text("P:   "),sg.Input(bolsa_letras['P']['cantidad'],key="CANT-P",size=(5,5))],#sg.Text("   (En minutos)")],
			  [sg.Text("Q:  "),sg.Input(bolsa_letras['Q']['cantidad'],key="CANT-Q",size=(5,5)),sg.Text("     "),sg.Text("R: "),sg.Input(bolsa_letras['R']['cantidad'],key="CANT-R",size=(5,5)),sg.Text("    "),sg.Text("RR:"),sg.Input(bolsa_letras['RR']['cantidad'],key="CANT-RR",size=(5,5)),sg.Text("     "),sg.Text("S:  "),sg.Input(bolsa_letras['S']['cantidad'],key="CANT-S",size=(5,5)),sg.Text("     "),sg.Text("T: "),sg.Input(bolsa_letras['T']['cantidad'],key="CANT-T",size=(5,5)),sg.Text("     "),sg.Text("U:    "),sg.Input(bolsa_letras['U']['cantidad'],key="CANT-U",size=(5,5))],
			  [sg.Text(" V: "),sg.Input(bolsa_letras['V']['cantidad'],key="CANT-V",size=(5,5)),sg.Text("     "),sg.Text("W:"),sg.Input(bolsa_letras['W']['cantidad'],key="CANT-W",size=(5,5)),sg.Text("     "),sg.Text("X:  "),sg.Input(bolsa_letras['X']['cantidad'],key="CANT-X",size=(5,5)),sg.Text("     "),sg.Text("Y:  "),sg.Input(bolsa_letras['Y']['cantidad'],key="CANT-Y",size=(5,5)),sg.Text("     "),sg.Text("Z:  "),sg.Input(bolsa_letras['Z']['cantidad'],key="CANT-Z",size=(5,5)),sg.Text("     ")],
			  [sg.Text("")],
			  [sg.Text("PUNTAJE DE LETRAS :")],
			  [sg.Text("A:  "),sg.Input(bolsa_letras['A']['valor'],key="VALOR-A",size=(5,5)),sg.Text("     "),sg.Text("B: "),sg.Input(bolsa_letras['B']['valor'],key="VALOR-B",size=(5,5)),sg.Text("     "),sg.Text("C: "),sg.Input(bolsa_letras['C']['valor'],key="VALOR-C",size=(5,5)),sg.Text("     "),sg.Text("D:  "),sg.Input(bolsa_letras['D']['valor'],key="VALOR-D",size=(5,5)),sg.Text("     "),sg.Text("E:  "),sg.Input(bolsa_letras['E']['valor'],key="VALOR-E",size=(5,5)),sg.Text("     "),sg.Text("F:    "),sg.Input(bolsa_letras['F']['valor'],key="VALOR-F",size=(5,5))],#sg.Text("(Facil,Medio,Dificil)")],
			  [sg.Text("G:  "),sg.Input(bolsa_letras['G']['valor'],key="VALOR-G",size=(5,5)),sg.Text("     "),sg.Text("H: "),sg.Input(bolsa_letras['H']['valor'],key="VALOR-H",size=(5,5)),sg.Text("     "),sg.Text("I:  "),sg.Input(bolsa_letras['I']['valor'],key="VALOR-I",size=(5,5)),sg.Text("     "),sg.Text("J:   "),sg.Input(bolsa_letras['J']['valor'],key="VALOR-J",size=(5,5)),sg.Text("     "),sg.Text("K: "),sg.Input(bolsa_letras['K']['valor'],key="VALOR-K",size=(5,5)),sg.Text("      "),sg.Text("L:   "),sg.Input(bolsa_letras['L']['valor'],key="VALOR-L",size=(5,5))],
			  [sg.Text("LL: "),sg.Input(bolsa_letras['LL']['valor'],key="VALOR-LL",size=(5,5)),sg.Text("     "),sg.Text("M:"),sg.Input(bolsa_letras['M']['valor'],key="VALOR-M",size=(5,5)),sg.Text("     "),sg.Text("N:  "),sg.Input(bolsa_letras['N']['valor'],key="VALOR-N",size=(5,5)),sg.Text("     "),sg.Text("Ñ:  "),sg.Input(bolsa_letras['Ñ']['valor'],key="VALOR-Ñ",size=(5,5)),sg.Text("     "),sg.Text("O: "),sg.Input(bolsa_letras['O']['valor'],key="VALOR-O",size=(5,5)),sg.Text("     "),sg.Text("P:   "),sg.Input(bolsa_letras['P']['valor'],key="VALOR-P",size=(5,5))],#sg.Text("   (En minutos)")],
			  [sg.Text("Q:  "),sg.Input(bolsa_letras['Q']['valor'],key="VALOR-Q",size=(5,5)),sg.Text("     "),sg.Text("R: "),sg.Input(bolsa_letras['R']['valor'],key="VALOR-R",size=(5,5)),sg.Text("    "),sg.Text("RR:"),sg.Input(bolsa_letras['RR']['valor'],key="VALOR-RR",size=(5,5)),sg.Text("     "),sg.Text("S:  "),sg.Input(bolsa_letras['S']['valor'],key="VALOR-S",size=(5,5)),sg.Text("     "),sg.Text("T: "),sg.Input(bolsa_letras['T']['valor'],key="VALOR-T",size=(5,5)),sg.Text("     "),sg.Text("U:    "),sg.Input(bolsa_letras['U']['valor'],key="VALOR-U",size=(5,5))],
			  [sg.Text(" V: "),sg.Input(bolsa_letras['V']['valor'],key="VALOR-V",size=(5,5)),sg.Text("     "),sg.Text("W:"),sg.Input(bolsa_letras['W']['valor'],key="VALOR-W",size=(5,5)),sg.Text("     "),sg.Text("X:  "),sg.Input(bolsa_letras['X']['valor'],key="VALOR-X",size=(5,5)),sg.Text("     "),sg.Text("Y:  "),sg.Input(bolsa_letras['Y']['valor'],key="VALOR-Y",size=(5,5)),sg.Text("     "),sg.Text("Z:  "),sg.Input(bolsa_letras['Z']['valor'],key="VALOR-Z",size=(5,5)),sg.Text("     ")],
			  [sg.Text("Selecione dificultad( 1 - 3 ) :"),sg.Input(dificultad,key="DIFICULTAD",size = (3,3)),sg.Text("Tiempo de duracion : "), sg.Input(tiempo,key="TIEMPO",size=(3,3)),sg.Text("      "),sg.Text("DIAMETRO DEL TABLERO: "),sg.Input(diametro,key="DIAMETRO",size=(3,3))],
			  [sg.Text(" "*70),sg.Button("Guardar",key="_GUARDAR_"),sg.Button("SALIR",key = "_EXIT_")]]



	window = sg.Window("Scrable Python2020", layout,size =(800,600))
	program = True
	
	while program:
		event,values = window.read()
		
		if event is "_GUARDAR_":
				
			errores = {}
			for x in values:
				
				if x[0:4] == "CANT":
					try:
						bolsa_letras[x[5:]]['cantidad'] = int(values[x])
					except:
						errores['CANTIDAD-'+str(x[5:])] = "La cantidad de fichas debe ser un numero entero"
						
						
				if x[0:5] == "VALOR":
					try:
						bolsa_letras[x[6:]]['valor'] = int(values[x])
					except:

						errores['VALOR-'+str(x[6:])] = "El valor de las fichas debe ser un numero entero"
						
						
				if x == "DIFICULTAD":
					try:
						if (int(values['DIFICULTAD'])>0 and int(values['DIFICULTAD'])<4):
							dificultad =  int(values['DIFICULTAD'])
						else:
							errores['dificultad'] = "La dificultad tiene puede variar unicamente entre los valores: 1,2 y 3"
					except:
						
						errores["dificultad"] = "La dificultad tiene puede variar unicamente entre los valores: 1,2 y 3"
						

				if x == "TIEMPO":
					try:
						tiempo = int(values['TIEMPO'])
					except:
						errores['tiempo'] = "El tiempo debe ser un numero entero que represente los minutos"
						print("No hay tiempo")
				if x == "DIAMETRO":
					try:
						if (int(values['DIAMETRO']))== 15 or (int(values['DIAMETRO'])) == 17 or (int(values['DIAMETRO'])) == 19 :
							diametro = int(values['DIAMETRO'])
						else:
							errores['diametro'] = "El diametro debe ser 15,17 o 19"
					except:
						errores['diametro'] = "El diametro debe ser 15,17 o 19"


			
			if len(errores) > 0:
				sg.popup_scrolled("ERROR",errores)
			contenido = {}
			contenido['bolsa_letras'] = bolsa_letras
			contenido['dificultad'] = dificultad
			contenido['tiempo'] = tiempo
			contenido['diametro'] = diametro
			


			
			

			with open('configuration.json', 'w') as f:
				json.dump(contenido, f, indent=4)
			sg.Popup("AVISO","Los cambios correctos fueron guardados con éxito.")
			
		if event is "_EXIT_":
			program = False
	
	window.close()
	