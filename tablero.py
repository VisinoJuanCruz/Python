import PySimpleGUI as sg
import numpy as np
import casillero

#Clase Tablero
class Tablero:
	#Atributos
	def __init__(self,alto,ancho):
		self.arreglo = np.full((ancho,alto),casillero.Casillero(5,5,5))
		self.alto = alto
		self.ancho = ancho
		self.cant_casilla_con_premio=0
		self.cant_casilla_normal = 0
		self.cant_casilla_descuento = 0

	#Metodos

	def dibujar_tablero(self):
		tablero = [[sg.Button(str("Vacio"),button_color=("white","black"),size=(0, 0), pad=(0,0), border_width=1,
			font='any 8',key=(row,col)) for col in range(self.alto)] for row in range(self.ancho)]
		return tablero
	
	def hacer_tablero(self):
		lattice = np.empty( (self.ancho,self.alto), dtype=object)
		lattice[:,:] = Tablero(15,15)
		#for i in range(3):
   		#	for j in range(3):
        #		lattice[i,j] = sg.Button(str("Vacio"), image_filename="./IconosFichas/casilla.png",size=(0, 0), pad=(0,0), border_width=1,font='any 8')
		return lattice
	


	def asignar_casilla_normal(self,cant):
		self.cant_casilla_normal = cant

	def asignar_casilla_descuento(self,cant):
		self.cant_casilla_descuento = cant

	def asignar_casilla_con_premio(self,cant):
		self.cant_casilla_con_premio = cant

	def cant_casilla_normal(self):
		return self.cant_casilla_normal

	def cant_casilla_con_descuento(self):
		return self.cant_casilla_con_descuento

	def cant_casilla_con_premio(self):
		return self.cant_casilla_con_premio
"""
tabla = Tablero(15,15)
print ("Tablero 1 = ",tabla.alto)
matriz = tabla.dibujar_tablero()
print(matriz[0][0])
matriz[0][0] = sg.Button(str("Vacio"))
print(matriz[0][0])
#print("MATRIZ = ", tabla.hacer_tablero())

"""