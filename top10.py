import PySimpleGUI as sg
import json


with open('top10.json', 'r') as archivo:
	top10 = json.load(archivo)


sg.theme('Light Brown 9')
layouttop10 = []
for x in top10:
	
	frase = "Top"+ str(x)+" es de "+ str(top10[x])+ " puntos."
	layouttop10.append([sg.Text(frase)])

layouttop10 += [[sg.Button("Ok", key= ("-OK-")),sg.Button("Reset", key=("-RESET-"))]]

window = sg.Window("TOP10 Puntuaciones", layouttop10,size =(200,300))



def iniciar():	
	program = True
	while program:
		
		
		event,values = window.read()
		
		if event == "-OK-":
			program = False
			break
			

		if event == "-RESET-":
			with open('top10.json','w') as archivo:
				for x in top10:
					top10[x] = 0
				json.dump(top10,archivo, indent=4)
				sg.Popup("Ya se reseteo el top10.")
			
	window.close()
	
