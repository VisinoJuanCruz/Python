import PySimpleGUI as sg
import numpy as np
import casillero

#Clase Tablero
class Tablero:
	#Atributos
	def __init__(self,alto,ancho):
		self.matriz = casillero.Casillero(1,2,4) for col in range(alto)] for row in range(ancho)]
		self.alto = alto
		self.ancho = ancho
		self.cant_casilla_con_premio=0
		self.cant_casilla_normal = 0
		self.cant_casilla_descuento = 0

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


	def ocupar_casilla(self,ficha):
		if self.
"""
tabla = Tablero(15,15)
print ("Tablero 1 = ",tabla.alto)
matriz = tabla.dibujar_tablero()
print(matriz[0][0])
matriz[0][0] = sg.Button(str("Vacio"))
print(matriz[0][0])
#print("MATRIZ = ", tabla.hacer_tablero())

"""