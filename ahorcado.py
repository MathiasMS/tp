# ------------------------------------GENERAR DICCIONARIO A PARTIR DE TEXTO ------------------------------------------ 
def esEspacio(palabra):
	return palabra.strip() == ""

def esNumero(palabra):
	return palabra.isdigit()

def esPalabra(palabra):
	return not esNumero(palabra) and not esEspacio(palabra)

def limpiarTexto(texto):
	palabrasEntexto = texto.split()
	textoLimpio = filter(esPalabra, palabrasEntexto)
	return list(textoLimpio)

def generarPalabra(diccionario,palabra):
	if palabra.lower() in diccionario:
		diccionario[palabra.lower()] = diccionario[palabra.lower()] + 1
	else:
		diccionario[palabra.lower()] = 1
	return diccionario

def generarDiccionario(palabrasLimpiasEnTexto):
	diccionario = {}
	for palabra in palabrasLimpiasEnTexto:
		generarPalabra(diccionario, palabra)
	return diccionario
# ------------------------------------GENERAR DICCIONARIO A PARTIR DE TEXTO ------------------------------------------

def validarJugadores(numeroJugadores):
	return int(numeroJugadores) <= 10

def validarNombreJugador(jugadores, nombre):
	return not nombre in jugadores and not esEspacio(nombre)

def elegirJugadores():
	cantidadJugadores = input("Coloque la cantidad de jugadores que quieren jugar: ")
	if not esNumero(cantidadJugadores) or esEspacio(cantidadJugadores):
		print("Formato invalido. Coloque un numero!")
		return elegirJugadores()
	elif not validarJugadores(cantidadJugadores):
		print("El maximo de jugadores permitido es 10")
		return elegirJugadores()
	return cantidadJugadores	

def nombrarJugadores(cantidadJugadores):
	jugadores = {}
	contador = 0
	while contador < cantidadJugadores:
		nombre = input("Coloque el nombre del jugador (%d)\n" % contador)
		if validarNombreJugador(jugadores, nombre):
			jugadores[nombre] = 0
			contador += 1 
		else:
			print("Nombre invalido, intente con otro\n")
	return jugadores

def menor5caracteres(largoDeLaPalabra):
	return int(largoDeLaPalabra) < 5

def elegirPalabraParaJugar(diccionarioParaJugar):	
	largoDeLaPalabra = input("Elijan el largo de la palabra que quieren utilizar para jugar\n")
	if not esNumero(largoDeLaPalabra) or menor5caracteres(largoDeLaPalabra):
		print("No se ha ingresado un formato valido. Utilizar unicamente numeros positivos y mayor a 5")
		return elegirPalabraParaJugar(diccionarioParaJugar)
	else:
		num = largoDeLaPalabra
		numerito = int(num)
		for palabraEndiccionario in diccionarioParaJugar.keys():
			if len(palabraEndiccionario) == numerito:
				return palabraEndiccionario
	print("No hay ninguna palabra en el diccionario con ese tamaño.Vuelve a elegir\n")
	return elegirPalabraParaJugar(diccionarioParaJugar)

def inicio():
	print("Bienvenidos al ahorcado!!!!!\n")
	diccionarioParaJugar = generarDiccionario(limpiarTexto("Hola nosotros somos el ahorcado  2 3 "))
	cantidadJugadores = elegirJugadores()
	print("Excelente!!!!\n")
	print("Coloque el nombre de cada jugador\n")
	jugadores = nombrarJugadores(int(cantidadJugadores))
	print(jugadores)
	print("Perfecto!! ya estan todos los " + cantidadJugadores + " jugadores preparados!\n")
	palabraParaJugar = elegirPalabraParaJugar(diccionarioParaJugar)
	print("La palabra tiene %d letras" % len(palabraParaJugar))
	

inicio()