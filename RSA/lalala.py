import random

def generar_claves(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(1, phi)
    mcd = obtener_mcd(e, phi)
    
    while mcd != 1:
        e = random.randrange(1, phi)
        mcd = obtener_mcd(e, phi)
    
    d = obtener_inverso_multiplicativo(e, phi)
    
    return (n, e, d)

def obtener_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def obtener_inverso_multiplicativo(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('El inverso multiplicativo no existe')
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def cifrar(mensaje, clave_publica):
    n, e = clave_publica
    return pow(mensaje, e, n)

def descifrar(cifrado, clave_privada):
    n, d = clave_privada
    return pow(cifrado, d, n)

p = 61
q = 53
claves = generar_claves(p, q)

mensaje = 12345
cifrado = cifrar(mensaje, claves[:2])
descifrado = descifrar(cifrado, claves)

print("Mensaje original:", mensaje)
print("Mensaje cifrado:", cifrado)
print("Mensaje descifrado:", descifrado)