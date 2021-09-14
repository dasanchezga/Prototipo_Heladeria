# Programa heladeria
def mostrar_menu():
    # Función Menú
    # Muestra el menu principal
    print("*****Administración de Heladeria*****")
    print()
    print("Seleccione una opción (1-5) o q para salir")
    print("1. Comprar")
    print("2. Agregar un nuevo producto")
    print("3. Ver inventario")
    print("4. Agregar al inventario")
    print("5. Total ventas del día")
    print("q: Salir")


def venta():
    # Funcion de ventas
    # Permite las ventas
    sabores = ''
    cobertura = ''
    global productosH, preciosH, porcionesH, productosC, preciosC, porcionesC, porciones, ventas_totales
    if len(productosH) == 0 and len(productosC) == 0:
        # sin productos en el inventario
        print("No hay productos disponibles en el inventario\n")
    else:
        # Nuevas ventas
        print("Nueva Venta: ")
        print("Escoja un sabor: ")
        for i in range(len(productosH)):
            if porcionesH[i] >0:
                print(str(i + 1) + ')' + productosH[i] + '\t' + '\t' + '\t' + str(preciosH[i]) + '\t' + str(porcionesH[i]))
        sabores = int(input())
        if sabores > 0 and sabores < (len(productosH) + 1) and (porcionesH[sabores-1] > 0):
            # Seleccion de sabores
            print("Usted seleccionó: ")
            print(str(sabores) + ')' + productosH[sabores - 1] + '\t' + '\t' + '\t' + str(
                preciosH[sabores - 1]) + '\t' + str(porcionesH[sabores - 1]))
            print("¿Cuántas porciones?: ")
            porciones = int(input())  # Porciones escogidas
            porcionesH[sabores - 1:sabores] = [porcionesH[sabores - 1] - porciones]
            if (len(productosC)) > 0:
                print("¿Desea cobertura? (s/n): ")
                decision = str(input())
                if decision != 's' and decision != 'n':
                    print("Escoja una opción valida. (s/n) ")
                    decision = str(input())
                elif decision == 's':  # con coberturas
                    print("Escoja la cobertura ")
                    for e in range(len(productosC)):
                        print(str(e + 1) + ')' + productosC[e] + '\t' + '\t' + '\t' + str(preciosC[e]) + '\t' + str(
                        porcionesC[e]))
                    cobertura = int(input())
                    if cobertura > len(productosC):
                        print("Opción no valida. ")
                    else:
                        print("Usted seleccionó: ")  # escoger coberturas
                        print(str(cobertura) + ')' + productosC[cobertura - 1] + '\t' + '\t' + '\t' + '\t' + str(
                        preciosC[cobertura - 1]) + '\t' + '\t' + str(porcionesC[cobertura - 1]))
                        porcionesC[cobertura - 1:cobertura] = [porcionesC[cobertura - 1] - 1]
                        venta = (preciosH[sabores - 1] * porciones) + preciosC[cobertura - 1]
                        print("Total a pagar:  " + str(venta))
                        ventas_totales = ventas_totales + venta
                elif decision == 'n':
                # sin coberturas
                     venta = (preciosH[sabores - 1] * porciones)
                     print("Total a pagar: " + str(venta))
                     ventas_totales = ventas_totales + venta
        else:
            print("Escoja una opcion valida. ")


def nuevo_prod():
    # Funcion Nuevo Producto
    print("Tipo de producto (1 o 2)")
    print("1. Helado")
    print("2. Cobertura")
    print("q. salir")
    eleccion = input()
    while eleccion != 'q':
        if eleccion != 'q' and eleccion == '1' or eleccion == '2':
            if eleccion == '1':  # Helados
                # Sub menu Funcion agregar productos
                global productosH, preciosH, porcionesH
                nuevo_producto = str(input("Ingrese el nombre del producto (Ejemplo: Galletas, M&M, etc.):"))
                if nuevo_producto in productosH:
                    posicion = productosH.index(nuevo_producto)
                    c = int(input("Ingrese el valor de la porción: "))
                    preciosH[posicion] = preciosH[posicion] + c
                    c = int(input("Ingrese el número de porciones disponibles: "))
                    porcionesH[posicion] = porcionesH[posicion] + c
                    break
                else:
                    productosH += [nuevo_producto]
                    preciosH += [int(input("Ingrese el valor de la porción: "))]
                    porcionesH += [int(input("Ingrese el número de porciones disponibles: "))]
                break
            elif eleccion == '2':  # Agregar Coberturas
                global productosC, preciosC, porcionesC
                nuevo_producto = str(input("Ingrese el nombre del producto (Ejemplo: Galletas, M&M, etc.):"))
                if nuevo_producto in productosC:
                    posicion = productosC.index(nuevo_producto)
                    c = int(input("Ingrese el valor de la porción: "))
                    preciosC[posicion] = preciosC[posicion] + c
                    c = int(input("Ingrese el número de porciones disponibles: "))
                    porcionesC[posicion] = porcionesC[posicion] + c
                    break
                else:
                    productosC += [nuevo_producto]
                    preciosC += [int(input("Ingrese el valor de la porción: "))]
                    porcionesC += [int(input("Ingrese el número de porciones disponibles: "))]
                break
        else:
            print("Escoja una opción valida. ")
            print()
            print("Tipo de producto (1 o 2)")
            print("1. Helado")
            print("2. Cobertura")
            print("q. salir")
            eleccion = input()


def mostrar_inventario():
    global productosH, preciosH, porcionesH, preciosC, porcionesC, productosC
    if len(productosH) == 0 and len(productosC) == 0:
        print('Sin productos en el inventario')
    else:
        print('Helados')
        for i in range(len(productosH)):
            if porcionesH[i] > 0:
                print(str(i + 1) + ')' + productosH[i] + '\t' + '\t' + '\t' + str(preciosH[i]) + '\t' + str(
                    porcionesH[i]))
        print()
        print('Coberturas')
        for e in range(len(productosC)):
            if porcionesC[e] > 0:
                print(str(e + 1) + ')' + productosC[e] + '\t' + '\t' + '\t' + str(preciosC[e]) + '\t' + '\t' + str(
                    porcionesC[e]))


def agregar_inv():
    print("Tipo de producto (1 o 2)")
    print("1. Helado")
    print("2. Cobertura")
    print("q. salir")
    eleccion = input()
    while eleccion != 'q':
        if eleccion != 'q' and eleccion == '1' or eleccion == '2':
            if len(productosH) == 0 and len(productosC) == 0:
                print("No hay productos en el inventario")
                break
            elif eleccion == '1':
                print("Seleccione un producto ")
                for i in range(len(productosH)):
                    print(str(i + 1) + ')' + productosH[i] + '\t' + '\t' + '\t' + str(preciosH[i]) + '\t' + str(
                        porcionesH[i]))
                producto = int(input())
                print("Usted seleccionó: ")
                print(str(producto) + ')' + str(productosH[producto - 1]) + '\t' + '\t' + '\t' + str(
                    preciosH[producto - 1]) + '\t' + str(porcionesH[producto - 1]))
                print()
                print("Ingrese la cantidad de porciones a registrar:  ")
                porciones_regH = int(input())
                porcionesH[producto - 1:producto] = [porcionesH[producto - 1] + porciones_regH]
                break
            elif eleccion == '2':
                print("Seleccione un producto ")
                for e in range(len(productosC)):
                    print(str(e + 1) + ')' + productosC[e] + '\t' + '\t' + '\t' + str(preciosC[e]) + '\t' + '\t' + str(
                        porcionesC[e]))
                producto = int(input())
                print("Usted seleccionó: ")
                print(str(producto) + ')' + str(productosC[producto - 1]) + '\t' + '\t' + '\t' + str(
                    preciosC[producto - 1]) + '\t' + '\t' + str(porcionesC[producto - 1]))
                print()
                print("Ingrese la cantidad de porciones a registrar:  ")
                porciones_regC = int(input())
                porcionesC[producto - 1:producto] = [porcionesC[producto - 1] + porciones_regC]
                break
        else:
            print("Escoja una opción valida. ")
            print()
            print("Tipo de producto (1 o 2)")
            print("1. Helado")
            print("2. Cobertura")
            print("q. salir")
            eleccion = input()


def ventas_dia():
    # Ventas Totales
    global ventas_totales
    print("Total de ventas del dia: " + str(ventas_totales))


a = ''
productosH = []
preciosH = []
porcionesH = []
productosC = []
preciosC = []
porcionesC = []
porciones = 0
contador = 0
ventas_totales = 0
while a != 'q':
    mostrar_menu()
    a = input()
    if a != 'q' and a != '1' and a != '2' and a != '3' and a != '4' and a != '5':
        print("Entrada inválida. Por favor intente de nuevo \n\n")
    elif a == '1':
        venta()
    elif a == '2':
        nuevo_prod()
    elif a == '3':
        mostrar_inventario()
    elif a == '4':
        agregar_inv()
    elif a == '5':
        ventas_dia()