import PySimpleGUI as sg
import tablero as table
import casillero
import mano

ALTO=15
ANCHO=15

mano_rival = mano.Mano()
mano_propia = mano.Mano()
tablero =  table.Tablero(ALTO,ANCHO)

#fichas_del_rival
mano_rival =  mano_rival.fichas
#fichas_del_jugador
mano_propia =  mano_propia.fichas	

layout = [[sg.Text('ScrabbleAR GAME',size=(15,0),justification='center', font=("Helvetica", 25))]]
layout += [[sg.Text("")]]
layout+=mano_rival
layout += [[sg.Text("")]]		
layout+=tablero.matriz
layout += [[sg.Text("")]]
layout+=mano_propia



layout+= [[sg.Button("INICIAR")]]
window = sg.Window("ScrabbleAR",layout,size=(1000,1000))

while True:
	
	event, values = window.read()
	print(event, values)
	window[event].update(text="H", button_color=('blue','yellow'))



	
	
window.close()