import json

with open('configuration.json', 'r') as bolsa_letras:
	bolsa = json.load(bolsa_letras)

bolsa_letras.close()

print("imprimo bolsa: ",bolsa)