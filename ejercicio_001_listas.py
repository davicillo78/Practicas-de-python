"""
'''
Escriba una lista con nombres de personas. Haga algunos experimentos
imprimiendo los nombres de los mismos.
'''
amigos = ["Pedro", "Juan", "Vicky", "Javi"]
print(amigos[1])
print(amigos[2:3])
print(amigos[::-1])


'''
Con la lista inicial, escriba a cada uno de ellos un mensaje personalizado.
'''
print(f"Hola cómo estas {amigos[0]}?")
print(f"A {amigos[2]}, {amigos[0]} y a mi nos gustaría invitar a {amigos[1]} y a {amigos[3]} a comer")

'''
Haga algun ejercicio añadiendo o quitando elementos de una lista
'''
"""

motos = ["Honda", "Yamaha", "Ducati", "Bultaco", "Kawasaki"]
print(motos)
motos[0] = "Vespa"
print(motos)
motos.append("Piaggio")
print(motos)
del motos[4]
print(motos)
motos.insert(2, "Kawasaki")
print(motos)