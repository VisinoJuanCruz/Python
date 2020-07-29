import json


arc = open('configuration.py','r')
letras = arc.read()

print(type(dict(letras)))
print(letras)

	#with open('configuration.py', 'r') as arc:
	#	bolsa_letras = dict(arc.read())