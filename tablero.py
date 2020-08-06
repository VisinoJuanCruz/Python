import PySimpleGUI as sg



#Clase Tablero
class Tablero:
	#Atributos
	def __init__(self,matriz,diccionario,alto,ancho):
		self.matriz = matriz
		
		self.diccionario = diccionario

		self.alto = alto
		self.ancho = ancho
		
		
	def crear_diccionario(self):
		for x in range(self.ancho):
			for y in range(self.alto):
				self.diccionario[x,y] = ""
	
	def estado_botones(self,window,estado):
		"""Cambia el estado de los botones"""
		for x in self.diccionario:
			if self.diccionario[x] == "":
				window[x].Update(disabled = estado)
			else:
				window[x].Update(disabled = True )
	
	def sentido(self,lista_keys):
		"""Verifica en que sentido se va a escribir la palabra"""
		if len(lista_keys) == 0:
			return "cero"
		elif(len(lista_keys) == 1):
			return "uno"


		elif(lista_keys[-1][0] > lista_keys[-2][0]):
			return "vertical"
		else:
			return "horizontal"
	

	def habilitar_botones(self,window,estructura):
		"""Habilita los casilleros del teclado disponibles para jugar. Dependiendo el sentido en el que el jugador este formando la palabra"""

		lista_keys = list(estructura.keys())
		
		
		if self.sentido(lista_keys) == "cero":
			self.estado_botones(window,False)
		elif self.sentido(lista_keys) == "uno":
			coorde = lista_keys[-1]
			if (int(coorde[0]+1)<self.alto) and self.diccionario[tuple((int(coorde[0]+1),int(coorde[1])))]  == "":
				window[lista_keys[-1][0]+1,lista_keys[-1][1]].update(disabled = False)
			if int(coorde[1]+1)<self.ancho and self.diccionario[tuple((int(coorde[0]),int(coorde[1]+1)))]  == "":
				window[lista_keys[-1][0],lista_keys[-1][1]+1].update(disabled = False)
		elif (self.sentido(lista_keys) == "vertical") and (lista_keys[-1][0]+1 < self.alto):
			
			window[lista_keys[-1][0]+1,lista_keys[-1][1]].update(disabled = False)
		elif (self.sentido(lista_keys) == "horizontal") and (lista_keys[-1][1]+1 < self.ancho):
			
			window[lista_keys[-1][0],lista_keys[-1][1]+1].update(disabled = False)
			
	
		
		
	def asignar_especiales(self):
		"""Asigna casilleros con descuento y con premio"""
		for x in range(self.alto):
			for y in range(self.ancho):
				if ((x ==y) or ((x+y)== self.ancho-1)) :
					self.matriz[x][y].ButtonColor=('yellow','yellow')
				if ((x == 0) or (x==(self.alto-1)/2) or (x==self.alto-1)) and ((y == 0) or (y==(self.ancho-1)/2) or (y==self.ancho-1)):
					self.matriz[x][y].ButtonColor=('black','black')
					#self.matriz[x][y].ImageFilename = "./IconosFichas/descuento.png"
					#self.matriz[x][y].ImageSubSample = 4
					#self.matriz[x][y].ImageSize = (43,45)
					#self.matriz[x][y].border_width = 0
				if ((x ==(self.alto-1)/2) and (y==(self.ancho-1)/2)):
					self.matriz[x][y].ButtonColor=('red','red')
					#self.matriz[x][y].ImageFilename = "./IconosFichas/descuento.png"
					#self.matriz[x][y].ImageSubSample = 4
					self.matriz[x][y].ImageSize = (43,45)

	def actualizar(self,window):
		for x in self.diccionario:
			print(x)
			print(self.diccionario[x])
			if self.diccionario[x] == "":
				
				window[x].Update(text = self.diccionario[x]) #,image_filename= None)
			else:
				ruta = "./IconosFichas/"+self.diccionario[x]+".png"
				window[x].Update(text = self.diccionario[x],image_filename=ruta,image_subsample = 4,image_size = (43,45))