import PySimpleGUI as sg
import tablero as table
import casillero

ALTO=15
ANCHO=15


matriz =  table.Tablero(ALTO,ANCHO)
#fichas_del_rival
mano_rival =  [[sg.Button("", image_filename="./IconosFichas/casilla.png",size=(0, 0), pad=(0,0), border_width=1,
			font='any 8',key=(col)) for col in range(7)] for row in range(1)]
#fichas_del_jugador
mano_propia =  [[sg.Button("A", image_filename="./IconosFichas/casilla.png",size=(0, 0), pad=(0,0), border_width=1,
			font='any 8',key=(col)) for col in range(7)] for row in range(1)]	

layout = [[sg.Text('ScrabbleAR GAME',size=(15,0),justification='center', font=("Helvetica", 25))]]
layout += [[sg.Text("")]]
layout+=mano_rival
layout += [[sg.Text("")]]		
layout+=matriz.arreglo
layout += [[sg.Text("")]]
layout+=mano_propia



layout+= [[sg.Button("INICIAR")]]
window = sg.Window("ScrabbleAR",layout,size=(600,600))

while True:
	
	event, values = window.read()
	print(event, values)
	#if event == (0,0):
	#print(casillero_comun.esta_ocupada())
	#tabla = list(tablero.dibujar_tablero())
	#print(tabla[0,1])
	matriz.arreglo[event[0]][event[1]].ImageFilename = None
	matriz.arreglo[event[0]][event[1]].ButtonColor = ('blue','white')
	print(matriz.arreglo[event[0]][event[1]].ImageFilename)
	#print(dir(matriz.arreglo[event[0]][event[1]]))

	print (type(mano_propia))



	
	
window.close()