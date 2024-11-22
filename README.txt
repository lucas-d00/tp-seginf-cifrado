Funcionamiento del Script:

1. Se genera la clave con la funcion "generate_key" que crea una clave AES aleatoria de 256 bits.

2. Proceso de encriptacion:
	* Se lee el archivo.
	* Se genera un IV.
	* Se utiliza AES en modo CBC.
	* Los datos se rellenan para ajustarse al tamaño del bloque.
	* Se escribe el IV y los datos encriptados en un nuevo archivo.

3. Proceso de desencriptacion:
	* Se lee el archivo encriptado.
	* Se separan el IV y los datos encriptados.
	* Se utiliza la misma clave e IV para desencriptar.
	* Se elimina el relleno y se guarda el archivo desepcriptado.

