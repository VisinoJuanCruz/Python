import PySimpleGUI as sg

#background = '#000000'
#sg.SetOptions(background_color=background, element_background_color=background)
#sg.theme_previewer()
sg.theme('Light Brown 9')
layout = [[sg.Text("")],
		  [sg.Text("")],
		  [sg.Text(" "),sg.Button("",image_filename="./IconosFichas/configuracion.png",disabled=False),sg.Text(" "*10)],
		  [sg.Text("")],
		  [sg.Text("")],
		  [sg.Text("A:  "),sg.Input(key="A",size=(5,5)),sg.Text("     "),sg.Text("K: "),sg.Input(key="K",size=(5,5)),sg.Text("     "),sg.Text("RR: "),sg.Input(key="RR",size=(5,5)),sg.Text("SELECCIONE NIVEL: "),sg.Input(key="nivel")],
		  [sg.Text("B:  "),sg.Input(key="B",size=(5,5)),sg.Text("     "),sg.Text("L:  "),sg.Input(key="L",size=(5,5)),sg.Text("     "),sg.Text("S:    "),sg.Input(key="S",size=(5,5)),sg.Text("(Facil,Medio,Dificil)")],
		  [sg.Text("C:  "),sg.Input(key="C",size=(5,5)),sg.Text("     "),sg.Text("LL:"),sg.Input(key="LL",size=(5,5)),sg.Text("     "),sg.Text("T:   "),sg.Input(key="T",size=(5,5))],
		  [sg.Text("D:  "),sg.Input(key="D",size=(5,5)),sg.Text("     "),sg.Text("M: "),sg.Input(key="M",size=(5,5)),sg.Text("     "),sg.Text("U:   "),sg.Input(key="U",size=(5,5))],
		  [sg.Text("E:  "),sg.Input(key="E",size=(5,5)),sg.Text("     "),sg.Text("N: "),sg.Input(key="N",size=(5,5)),sg.Text("     "),sg.Text("V:    "),sg.Input(key="V",size=(5,5))],
		  [sg.Text("F:  "),sg.Input(key="F",size=(5,5)),sg.Text("     "),sg.Text("Ñ: "),sg.Input(key="Ñ",size=(5,5)),sg.Text("     "),sg.Text("W:   "),sg.Input(key="W",size=(5,5))],
		  [sg.Text("G:  "),sg.Input(key="G",size=(5,5)),sg.Text("     "),sg.Text("O: "),sg.Input(key="O",size=(5,5)),sg.Text("     "),sg.Text("X:    "),sg.Input(key="X",size=(5,5))],
		  [sg.Text("H:  "),sg.Input(key="H",size=(5,5)),sg.Text("     "),sg.Text("P: "),sg.Input(key="P",size=(5,5)),sg.Text("     "),sg.Text("Y:    "),sg.Input(key="Y",size=(5,5))],
		  [sg.Text(" I:   "),sg.Input(key="I",size=(5,5)),sg.Text("     "),sg.Text("Q: "),sg.Input(key="Q",size=(5,5)),sg.Text("     "),sg.Text("Z:   "),sg.Input(key="Z",size=(5,5))],
		  [sg.Text("J:  "),sg.Input(key="J",size=(5,5)),sg.Text("     "),sg.Text("R:  "),sg.Input(key="R",size=(5,5)),sg.Text("     ")],
		  [sg.Button("Guardar"),sg.Button("SALIR",key = "_EXIT_")]]


window = sg.Window("Scrable Python2020", layout,size =(800,600))


def iniciar():
	event,values = window.read()
	while True:
		print(event,values)
		if event is "_EXIT_":
			window.close()
		
	window.close()