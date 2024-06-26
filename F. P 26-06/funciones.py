import random


def validar_rut (rut):
    if rut == "":
        print("El rut es oblitario")
        return False
    else:
        return True


def validar_correo(correo):
    if correo != "":
        return True
    else:
        print("El correo es obligatorio")
        return False
    
def menu():
    print("1. VIP\n2. Galería\n3. Cancha")
    opciones = input("Opción: ")
    return opciones

def azar():
    valor_random = random.randint(1000, 9999)
    return valor_random

#Se retorna para poder capturar el valor de la variable y poder usarlo

def generar_boleta(cantidad_vip, cantidad_gal, cantidad_can):
    #write -> w
    #read -> r
    with open("boleta.txt", "w") as archivo:
        if cantidad_vip != 0:
            codigo = azar()
            archivo.write("-------------------------")
            archivo.write(f"Código: {codigo}")
            archivo.write("Tipo VIP")
            archivo.write("Marcianeke sinfónico")
            archivo.write(f"Cantidad: {cantidad_vip}")
            archivo.write(f"Valor: {cantidad_vip * 100000}")
#En python (y otros) se puede recorrer una string como si uno pasara por una lista
        


#csv (csv en lugar del archivo.txt), random, listas, funciones
#Al parecer es en un sólo archivo