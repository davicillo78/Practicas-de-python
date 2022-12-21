'''
Escribir un programa que pregunte al usuario una cantidad 
a invertir, el interés anual y el número de años, y muestre
por pantalla el capital obtenido en la inversión.
'''
capital = float(input("¿Cuánto quiere invertir?: "))
interes = float(input("¿Qué interes anual desea?: "))
resultado = int(input("¿Cuantos años desea tener invertido su capital?: "))
final = round(capital * (interes/100 +1) ** resultado, 2)
print(f"Si invierte {capital}€ a un interes del {interes}% anual durante {resultado} años, obtendrá un total de {final}€ al final del plazo.")

'''12000
720 12720
763,2   13483,2
808,992 14292,192
857,53152   15149,72352
908,9834112 16058,7069312'''

