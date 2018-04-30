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

def validarNombreJugador(jugadores,nombre):
	if jugadores:	
		for jugador in jugadores:
			if jugador[0] == nombre:
				return False
		return True
	else:
		return True

# def validarNombreJugador(jugadores, nombre):
# 	return not nombre in jugadores and not esEspacio(nombre)

def elegirJugadores():
	cantidadJugadores = input("Coloque la cantidad de jugadores que quieren jugar: \n")
	if not esNumero(cantidadJugadores) or esEspacio(cantidadJugadores):
		print("Formato invalido. Coloque un numero!\n")
		return elegirJugadores()
	elif not validarJugadores(cantidadJugadores):
		print("El maximo de jugadores permitido es 10\n")
		return elegirJugadores()
	return cantidadJugadores	

# def nombrarJugadores(cantidadJugadores):
# 	jugadores = {}
#  	contador = 0
# 	while contador < cantidadJugadores:
# 		nombre = input("Coloque el nombre del jugador (%d)\n" % contador)
# 		if validarNombreJugador(jugadores, nombre):
# 			jugadores[nombre] = 0
# 			contador += 1 
# 		else:
# 			print("Nombre invalido, intente con otro\n")
# 	return jugadores

def nombrarJugadores(cantidadJugadores):
	# jugadores = {}
	jugadores = []
	contador = 0
	while contador < cantidadJugadores:
		nombre = input("Coloque el nombre del jugador (%d)\n" % contador)
		if validarNombreJugador(jugadores, nombre):
			# tupla (nombre, desaciertos, puntos)
			jugador = (nombre, 0, 0)
			jugadores.append(jugador)
			contador += 1 
		else:
			print("Nombre invalido, intente con otro\n")
	return jugadores

def menor5caracteres(largoDeLaPalabra):
	return int(largoDeLaPalabra) < 5

def esCaracter(palabra):
	return len(palabra) == 1

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

def jugadorTurno(jugadores, jugador=0):
	return jugadores[jugador]

def elegirLetra():
	letra = input("Elegi una letra\n")
	if not esNumero(letra) or esCaracter(letra):
		return letra
	else:
		return elegirLetra()

def verificarLetraEnPalabra(letraParaBuscar, palabraParaJugar,palabraFormadaPorIntentos):
	puntos = -2
	if len(palabraFormadaPorIntentos) != 0:
		for x in range(0,len(palabraParaJugar)):
			if palabraParaJugar[x] == letraParaBuscar:
				palabraFormadaPorIntentos[x] = palabraParaJugar[x]
				puntos = 1			
	else:
		for x in range(0,len(palabraParaJugar)):
			if palabraParaJugar[x] == letraParaBuscar:
				palabraFormadaPorIntentos.insert(x,palabraParaJugar[x])
				puntos = 1
			else:
				palabraFormadaPorIntentos.insert(x,"")
	return palabraFormadaPorIntentos, puntos

def modificarPuntajeJugador(jugador, puntos):
	if puntos == 1:
		jugadorModificado = (jugador[0], jugador[1], jugador[2] + puntos)
	else:
		jugadorModificado = (jugador[0], jugador[1] + 1, jugador[2] + puntos)
	return jugadorModificado

def modificarContador(jugadores, contador, puntos):
	if puntos != 1:
		if contador == len(jugadores) - 1:
			contador = 0
		else:
			contador += 1
	return contador

def verificarGanador(palabraFormadaPorIntentos):
		for letra in palabraFormadaPorIntentos:
			if letra == "":
				return False
		return True

def verificarSiJugadorPerdio(jugadores, contador):
	if jugadores[contador][1] == 7:
		jugadores.remove(contador)
	return jugadores

def verificarJugadores(jugadores):
	return len(jugadores) == 0

def jugar(jugadores,palabraParaJugar):
	palabraParaJugar = list(palabraParaJugar)
	contador = 0
	adivinar = False
	palabraFormadaPorIntentos = []
	while adivinar == False:
		jugador = jugadorTurno(jugadores,contador)
		print("Turno del jugador " + jugador[0] + "\n")
		letraParaBuscar = elegirLetra()
		palabraFormadaPorIntentos,puntos = verificarLetraEnPalabra(letraParaBuscar, palabraParaJugar, palabraFormadaPorIntentos,contador)
		adivinar = verificarGanador(palabraFormadaPorIntentos)
		jugador = modificarPuntajeJugador(jugador,puntos)
		jugadores = verificarSiJugadorPerdio(jugadores,contador)
		contador = modificarContador(jugadores,contador,puntos)
		adivinar = verificarJugadores(jugadores)

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
	print("La palabra tiene %d letras\n" % len(palabraParaJugar))
	a = jugar(jugadores, "hola")

inicio()