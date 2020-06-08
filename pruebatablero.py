import tablero
import PySimpleGUI as sg

tablero = tablero.Tablero(15,15)

layout = [[sg.Button("INICIAR")]]
matriz = tablero.matriz
layout+=matriz
window = sg.Window("ScrabbleAR",layout,size=(600,600))

jugador = Jugador()	

while True:
	

	event, values = window.read()
	print(event, values)
	#if event == (0,0):
	#print(casillero_comun.esta_ocupada())
	#tabla = list(tablero.dibujar_tablero())
	#print(tabla[0,1])

	
	
	
window.close()