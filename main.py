import Crypto
import Crypto.Random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

KEY_SIZE = 32  # Tamaño de la clave (256 bits)
BLOCK_SIZE = AES.block_size  # Tamaño del bloque AES (16 bytes)

def generate_key():
    #Genera una clave AES aleatoria.
    return get_random_bytes(KEY_SIZE)

def encrypt_file(file_path, key):
    """Encripta un archivo usando AES en modo CBC. Devuelve el archivo encriptado"""
    # Leer datos del archivo
    with open(file_path, 'rb') as file:
        data = file.read()

    # Crear IV y cifrador
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Rellenar datos al tamaño del bloque
    pad_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    padded_data = data + bytes([pad_len] * pad_len)

    # Encriptar
    encrypted_data = cipher.encrypt(padded_data)

    # Guardar datos encriptados junto con el IV
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(iv + encrypted_data)

    print(f"Archivo encriptado guardado en: {encrypted_file_path}")
    return encrypted_file_path

def decrypt_file(encrypted_file_path, key):
    """Desencripta un archivo encriptado con AES en modo CBC y lo devuelve."""
    # Leer datos encriptados
    with open(encrypted_file_path, 'rb') as encrypted_file:
        data = encrypted_file.read()

    # Separar IV y datos encriptados
    iv = data[:BLOCK_SIZE]
    encrypted_data = data[BLOCK_SIZE:]

    # Crear cifrador
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Desencriptar y remover relleno
    decrypted_data = cipher.decrypt(encrypted_data)
    pad_len = decrypted_data[-1]
    decrypted_data = decrypted_data[:-pad_len]

    # Guardar datos desencriptados
    decrypted_file_path = encrypted_file_path.replace('.enc', '.dec')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"Archivo desencriptado guardado en: {decrypted_file_path}")
    return decrypted_file_path


if __name__ == '__main__':
    # Generar clave
    key = generate_key()
    print(f"Clave generada: {key.hex()}")

    # Ruta del archivo a encriptar
    file_to_encrypt = 'target.txt'

    # Encriptar y desencriptar
    encrypted_path = encrypt_file(file_to_encrypt, key)
    decrypt_file(encrypted_path, key)