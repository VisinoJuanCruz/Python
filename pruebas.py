import random
"""
letras_disponibles = ['a','a','a','a','a','a','a','a','a','a','a','b','b','b','c','c','c','c','d','d','d','d',
'e','e','e','e','e','e','e','e','e','e','e','f','f','g','g','h','h','i','i','i','i','i','i','i','i','j','j',
'k','l','l','l','l','m','m','m','n','n','n','n','n','o','o','o','o','o','o','o','o','p','p','q','r',
'r','r','r','rr','s','s','s','s','s','s','s','t','t','t','t','u','u','u','u','u','u','v','v','w','x','y','z']
print(letras_disponibles)
letra = random.choice(letras_disponibles)
letras_disponibles.remove(letra)
print("x"* 50)
print(letra)
print(letras_disponibles)

"""
diccionario = {(11, 3): '00', (11, 4): '22', (11, 5): '33', (11, 6): '44'}

lista_keys = list(diccionario.keys())


if len(lista_keys) == 0:
	print("vacia")
elif(len(lista_keys) == 1):
	print("habilito derecha y abajo")
else:
	if(lista_keys[-1][0] > lista_keys[-2][0]):
		print("Vertical")
	else:
		print("Horizontal")

sentido = 1

print(sentido)
def cambio_sentido(sentido):
	sentido = "hola"
	print(sentido)
cambio_sentido(sentido)
print(sentido)