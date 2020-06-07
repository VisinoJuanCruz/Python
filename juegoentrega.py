import PySimpleGUI as sg
#import time
#import objetos
import tablero
#import casillero

ALTO = 15
ANCHO = 15


tablero = tablero.Tablero(ALTO,ANCHO)
layout = [sg.Text("ScrabbleAR")]
matriz =  [[sg.Button(str("Vacio"), image_filename="./IconosFichas/casilla.png",size=(0, 0), pad=(0,0), border_width=1,
			font='any 8',key=(row,col)) for col in range(ALTO)] for row in range(ANCHO)]
layout+=matriz
window = sg.Window("ScrabbleAR UNLP Python2020", layout)

#casillero_comun = objetos.CasillaComun()


while True:
	#window = sg.Window("ScrabbleAR UNLP Python2020", layout)
	event, values = window.read()
	print(event, values)
	#if event == (0,0):
	#print(casillero_comun.esta_ocupada())
	#tabla = list(tablero.dibujar_tablero())
	#print(tabla[0,1])
	#print(list(event))
	#print(matriz[event[0]][event[1]])
	#matriz[event[0]][event[1]] = sg.Button(str("OCUPADO"), image_filename="./IconosFichas/casilla.png",size=(0, 0), pad=(0,0), border_width=1,
	#		font='any 8')
	#print(matriz[event[0]][event[1]])
	#window.clean()
	
	
window.close()