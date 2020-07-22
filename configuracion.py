import PySimpleGUI as sg
import juego

#background = '#000000'
#sg.SetOptions(background_color=background, element_background_color=background)
#sg.theme_previewer()
def iniciar():
	sg.theme('Light Brown 9')
	layout = [[sg.Text("")],
			  [sg.Text("")],
			  [sg.Text(" "),sg.Button("",image_filename="./IconosFichas/configuracion.png",disabled=False),sg.Text(" "*10)],
			  [sg.Text("")],
			  [sg.Text("CANTIDAD DE LETRAS :")],
			  [sg.Text("A:  "),sg.Input(key="CANT-A",size=(5,5)),sg.Text("     "),sg.Text("B: "),sg.Input(key="CANT-B",size=(5,5)),sg.Text("     "),sg.Text("C: "),sg.Input(key="CANT-C",size=(5,5)),sg.Text("     "),sg.Text("D:  "),sg.Input(key="CANT-D",size=(5,5)),sg.Text("     "),sg.Text("E:  "),sg.Input(key="CANT-E",size=(5,5)),sg.Text("     "),sg.Text("F:    "),sg.Input(key="CANT-F",size=(5,5))],#sg.Text("(Facil,Medio,Dificil)")],
			  [sg.Text("G:  "),sg.Input(key="CANT-G",size=(5,5)),sg.Text("     "),sg.Text("H: "),sg.Input(key="CANT-H",size=(5,5)),sg.Text("     "),sg.Text("I:  "),sg.Input(key="CANT-I",size=(5,5)),sg.Text("     "),sg.Text("J:   "),sg.Input(key="CANT-J",size=(5,5)),sg.Text("     "),sg.Text("K: "),sg.Input(key="CANT-K",size=(5,5)),sg.Text("      "),sg.Text("L:   "),sg.Input(key="CANT-L",size=(5,5))],
			  [sg.Text("LL: "),sg.Input(key="CANT-LL",size=(5,5)),sg.Text("     "),sg.Text("M:"),sg.Input(key="CANT-M",size=(5,5)),sg.Text("     "),sg.Text("N:  "),sg.Input(key="CANT-N",size=(5,5)),sg.Text("     "),sg.Text("Ñ:  "),sg.Input(key="CANT-Ñ",size=(5,5)),sg.Text("     "),sg.Text("O: "),sg.Input(key="CANT-O",size=(5,5)),sg.Text("     "),sg.Text("P:   "),sg.Input(key="CANT-P",size=(5,5))],#sg.Text("   (En minutos)")],
			  [sg.Text("Q:  "),sg.Input(key="CANT-Q",size=(5,5)),sg.Text("     "),sg.Text("R: "),sg.Input(key="CANT-R",size=(5,5)),sg.Text("    "),sg.Text("RR:"),sg.Input(key="CANT-RR",size=(5,5)),sg.Text("     "),sg.Text("S:  "),sg.Input(key="CANT-S",size=(5,5)),sg.Text("     "),sg.Text("T: "),sg.Input(key="CANT-T",size=(5,5)),sg.Text("     "),sg.Text("U:    "),sg.Input(key="CANT-U",size=(5,5))],
			  [sg.Text(" V: "),sg.Input(key="CANT-V",size=(5,5)),sg.Text("     "),sg.Text("W:"),sg.Input(key="CANT-W",size=(5,5)),sg.Text("     "),sg.Text("X:  "),sg.Input(key="CANT-X",size=(5,5)),sg.Text("     "),sg.Text("Y:  "),sg.Input(key="CANT-Y",size=(5,5)),sg.Text("     "),sg.Text("Z:  "),sg.Input(key="CANT-Z",size=(5,5)),sg.Text("     ")],
			  [sg.Text("")],
			  [sg.Text("PUNTAJE DE LETRAS :")],
			  [sg.Text("A:  "),sg.Input(key="VALOR-A",size=(5,5)),sg.Text("     "),sg.Text("B: "),sg.Input(key="VALOR-B",size=(5,5)),sg.Text("     "),sg.Text("C: "),sg.Input(key="VALOR-C",size=(5,5)),sg.Text("     "),sg.Text("D:  "),sg.Input(key="VALOR-D",size=(5,5)),sg.Text("     "),sg.Text("E:  "),sg.Input(key="VALOR-E",size=(5,5)),sg.Text("     "),sg.Text("F:    "),sg.Input(key="VALOR-F",size=(5,5))],#sg.Text("(Facil,Medio,Dificil)")],
			  [sg.Text("G:  "),sg.Input(key="VALOR-G",size=(5,5)),sg.Text("     "),sg.Text("H: "),sg.Input(key="VALOR-H",size=(5,5)),sg.Text("     "),sg.Text("I:  "),sg.Input(key="VALOR-I",size=(5,5)),sg.Text("     "),sg.Text("J:   "),sg.Input(key="VALOR-J",size=(5,5)),sg.Text("     "),sg.Text("K: "),sg.Input(key="VALOR-K",size=(5,5)),sg.Text("      "),sg.Text("L:   "),sg.Input(key="VALOR-L",size=(5,5))],
			  [sg.Text("LL: "),sg.Input(key="VALOR-LL",size=(5,5)),sg.Text("     "),sg.Text("M:"),sg.Input(key="VALOR-M",size=(5,5)),sg.Text("     "),sg.Text("N:  "),sg.Input(key="VALOR-N",size=(5,5)),sg.Text("     "),sg.Text("Ñ:  "),sg.Input(key="VALOR-Ñ",size=(5,5)),sg.Text("     "),sg.Text("O: "),sg.Input(key="VALOR-O",size=(5,5)),sg.Text("     "),sg.Text("P:   "),sg.Input(key="VALOR-P",size=(5,5))],#sg.Text("   (En minutos)")],
			  [sg.Text("Q:  "),sg.Input(key="VALOR-Q",size=(5,5)),sg.Text("     "),sg.Text("R: "),sg.Input(key="VALOR-R",size=(5,5)),sg.Text("    "),sg.Text("RR:"),sg.Input(key="VALOR-RR",size=(5,5)),sg.Text("     "),sg.Text("S:  "),sg.Input(key="VALOR-S",size=(5,5)),sg.Text("     "),sg.Text("T: "),sg.Input(key="VALOR-T",size=(5,5)),sg.Text("     "),sg.Text("U:    "),sg.Input(key="VALOR-U",size=(5,5))],
			  [sg.Text(" V: "),sg.Input(key="VALOR-V",size=(5,5)),sg.Text("     "),sg.Text("W:"),sg.Input(key="VALOR-W",size=(5,5)),sg.Text("     "),sg.Text("X:  "),sg.Input(key="VALOR-X",size=(5,5)),sg.Text("     "),sg.Text("Y:  "),sg.Input(key="VALOR-Y",size=(5,5)),sg.Text("     "),sg.Text("Z:  "),sg.Input(key="VALOR-Z",size=(5,5)),sg.Text("     ")],
			  [sg.Text(" "*70),sg.Button("Guardar",key="_GUARDAR_"),sg.Button("SALIR",key = "_EXIT_")]]



	window = sg.Window("Scrable Python2020", layout,size =(800,600))
	program = True
	
	while program:
		event,values = window.read()
		
		if event is "_GUARDAR_":
			#print(values)
			#print(values)
			bolsa_letras={}
			info_letra = {'cantidad':"",'valor':""}
			letras_existentes = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','RR','S','T','U','V','W','X','Y','Z')
			for letra in letras_existentes:
				bolsa_letras[letra] = info_letra
			
			for x in values:
				if (x[0:4] == 'CANT'):
					try:
						bolsa_letras[x[5:]]['cantidad']= int(values[x])
					except:
						pass
				else:
					try:
						bolsa_letras[x[6:]]['valor'] = int(values[x])
					except:
						pass
				
			print(bolsa_letras)
			
			sg.Popup("Aun sin configurar.")
			print("Sin funcionalidad todavia.")
		if event is "_EXIT_":
			program = False
	
	window.close()
	