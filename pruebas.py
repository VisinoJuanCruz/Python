import pattern.es as pt

def palabra_existe(diccionario):
	palabra = ""
	for x in diccionario.values():
		palabra += x
    if (palabra.lower() in pt.verbs) or (palabra.lower() in pt.lexicon) or (palabra.lower() in pt.spelling):
        print(palabra , "EXISTE")



diccionario = {'22': 'G', '00': 'A', '44': 'L', '33': 'A'}
palabra = ""
for x in diccionario.values():
	palabra += x

str(palabra)
print (type(palabra))
palabra_existe(palabra)