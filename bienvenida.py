import PySimpleGUI as sg
import configuracion as config
import juego as game

#background = '#000000'
#sg.SetOptions(background_color=background, element_background_color=background)
#sg.theme_previewer()
sg.theme('Light Brown 9')
layout = [[sg.Text("")],
		  [sg.Text("")],
		  [sg.Text(" "*15),sg.Button("",image_filename="./IconosFichas/bienvenida.png",disabled=False),sg.Text(" "*10)],
		  [sg.Text("")],
		  [sg.Text("")],
		  [sg.Text("")],
		  [sg.Text("")],
		  [sg.Text("")],
		  [sg.Text(" "*35),sg.Button("",image_filename="./IconosFichas/comenzar.png",disabled=False,key="_COMENZAR_"),sg.Text(" "*10)],
		  [sg.Text("")],
		  [sg.Text(""),sg.Button("",image_filename="./IconosFichas/configuracion.png",disabled=False,key="_CONFIG_"),sg.Text(" "*20)],
		  [sg.Text("")],
		  [sg.Text(" "*55),sg.Button("",image_filename="./IconosFichas/salir.png",disabled=False,key="_EXIT_"),sg.Text(" "*25)]]

window = sg.Window("Scrable Python2020", layout,size =(800,600))

program = True
event,values = window.read()
while program:
	
	
	if event is "_COMENZAR_":
		
		game.iniciar()
	if event is "_CONFIG_":
		
		config.iniciar()
	if event is "_EXIT_":
		program= False
		break
	event,values = window.read()

window.close()