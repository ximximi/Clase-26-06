import funciones

cont_vip = 0
cont_gal = 0
cont_can = 0

rut = input ("Ingresa rut: ")
while funciones.validar_rut(rut) == False:
    rut = input("Ingresa rut: ")
    
correo = input("Ingresa correo: ")
while not funciones.validar_correo(correo):
    correo = input("Ingresa correo: ")

#el while == False y el while not son lo mismo
    
while True:
    opc = funciones.menu()
    if opc == "1":
        cont_vip += 1

    elif opc == "2":
        cont_gal += 1

    elif opc == "3":
        cont_can += 1

    else: print(f"La opción {opc} es incorrecta")

    seguir = input ("¿Quiere seguir comprando? (Sí/No): ")
    while seguir != "si" and seguir != "no":
        seguir = input("")

    if seguir == "si":
        continue
    if seguir == "no":
        break

funciones.generar_boleta(cont_vip, cont_gal, cont_can)
