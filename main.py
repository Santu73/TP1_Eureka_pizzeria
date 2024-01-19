
""" Quesada Santina - 6to A - Programación - TP1 Eureka"""

import os
from recurso import *


def limpiar_pantalla():
    if os.name == 'posix': os.system('clear') # Si el sistema operativo es Unix/Linux/MacOS
    elif os.name == 'nt': os.system('cls')# Si el sistema operativo es Windows

# Esta función muestra una lista de comidas y bebidas, pide al usuario que seleccione una opción, la cantidad que desea y si desea agregar ingredientes adicionales.
def comida(lista_comida, cont_principal, cont_cantidad, lista_agr, cont_ingr, nombre_pri):

    for i in range(0, len(lista_comida), 3):
        cont_principal += 1
        print(f"\t{YELLOW}{cont_principal}{BLACK}- {WHITE}{lista_comida[i]} {BLACK}- {WHITE}({lista_comida[i+1]}) {BLACK}- {WHITE}${lista_comida[i+2]}")

    op = evitar_error(f"{MAGENTA}\nIngrese el número de la opción que elije{WHITE}: ",cont_principal, "lista")
    unidades_comida = evitar_error(f"{CYAN}\n¿Cuántas unidades de este producto le gustaría comprar?{WHITE}: ",None,"unidades")
    agregar_pedido(cont_cantidad, lista_comida, unidades_comida, op, pedidos_finales,nombre_pri)
    ing_extras = evitar_error(f"{MAGENTA}\n¿Desea añadir algún ingrediente extra?\n\n\t{YELLOW}1) {BLACK}- {WHITE}(SI)\n\t{YELLOW}2) {BLACK}- {WHITE}(NO)\n\n{MAGENTA}Ingrese el número de la opción que elije{WHITE}: ",None,"1-2")
    print("")
    
    while ing_extras == 1:
        cont_principal2 = 0
        
        for i in range(0, len(lista_agr), 3):
            cont_principal2 += 1
            print(f"{YELLOW}\t{cont_principal2}{BLACK}- {WHITE}{lista_agr[i]} {BLACK}- {WHITE}${lista_agr[i+2]}")
        
        ing = evitar_error(f"{MAGENTA}\n¿Qué ingrediente desea agregar?{WHITE}: ",cont_principal2,"lista")
        unidades_Ingr = evitar_error(f"{CYAN}\n¿Cuántas unidades quiere de este producto?{WHITE}: ",None,"unidades")
        agregar_pedido(cont_ingr, lista_agr, unidades_Ingr, ing, pedidos_finales,nombre_pri)
        ing_extras = evitar_error(f"{MAGENTA}\n¿Desea añadir algún ingrediente extra más?\n\n\t{YELLOW}1) {BLACK}- {WHITE}(SI)\n\t{YELLOW}2) {BLACK}- {WHITE}(NO)\n\n{MAGENTA}Ingrese el número de la opción que elije{WHITE}: ",None,"1-2")
        print("")
    
    return pedidos_finales

# Esta función agrega un producto a la lista de pedidos y muestra un mensaje de confirmación.
def agregar_pedido(cont_cantidad, lista_pedido, unidades, op, pedidos_finales, nombre_pri):
    
    print("")
    for i in range(0, len(lista_pedido), 3):

        cont_cantidad += 1
        if op == cont_cantidad:
            
            nombre = lista_pedido[i]
            precio = lista_pedido[i+2] * unidades
            pedidos_finales.append(((nombre_pri)+" - "+nombre))
            pedidos_finales.append(precio) 
            print(f"{GREEN}\tUsted ha agregado a su pedido: {nombre_pri} ({nombre}) x{unidades} a ${precio}")
    
    return cont_cantidad,pedidos_finales

# Esta función toma una entrada del usuario y la valida, asegurándose de que sea un número entero dentro del rango válido para la opción seleccionada.
def evitar_error(msj, cont_principal, estado):

    while True:
        try:
            eleccion = int(input(msj))
            if estado == "lista":
                if eleccion != 0 and eleccion <= cont_principal: return eleccion
                else: print(f"{RED}\nPor favor, ingresa una opción del menú anterior")
            
            elif estado == "unidades":
                if eleccion != 0: return eleccion
                else: print(f"{RED}\nPor favor, ingrese un número entero")
            
            elif estado == "1-2":
                if eleccion > 0 and eleccion < 3: return eleccion
                else: print(f"{RED}\nPor favor, ingresa una opción del menú anterior")
            
            elif estado == "varios":
                if eleccion > 0 and eleccion < 5: return eleccion
                else: print(f"{RED}\nPor favor, ingrese un número entero")
            
            elif estado == "0-1":
                if eleccion == 0 or eleccion == 1: return eleccion
                else: print(f"{RED}\nPor favor, ingrese un número entero")
        
        except ValueError:
            print(f"{RED}\nPor favor, ingresa un número entero")

# Esta función crea una factura de compra y la muestra en la pantalla. La función utiliza la lista de productos seleccionados y sus precios para calcular el total y mostrarlo en la factura.
def crear_factura(pedidos_finales):
    
    print(RED+BG_WHITE+'\n\n\t***********************  TICKET DE COMPRA  ***********************')
    print(MAGENTA+".\n\tPIZZERIA EUREKA --------------------------------------------------"+YELLOW+"\n\n\tCUIT Nro.: 12-3456789-0\n\tING. BRUTOS: CM1234567890\n\tNIC. ACT.: 01/11/1911\n\tTEL.: +54 9 3547-123450\n\tDOM. COMER.: AV. LIBERTADOR 1740\n\tBARRIO: CENTRO     CP: 5186\n\tALTA GRACIA        CÓRDOBA"+MAGENTA+"\n\n\tDETALLE DE SU COMPRA ---------------------------------------------\n")
    subtotal = 0
    
    for i in range(1, len(pedidos_finales), 2):
        print(f"{YELLOW}\t{pedidos_finales[i-1]}: ${pedidos_finales[i]}")
        subtotal += pedidos_finales[i]
    
    impuesto = subtotal * 0.21
    total_a_pagar = subtotal + impuesto
    
    # :.2f: Es una sintaxis de formato utilizada en cadenas de texto formateadas en Python para redondear y mostrar un número con dos decimales
    print(f"\n\t{MAGENTA}------------------------------------------------------------------{YELLOW}\n\n\tSUBTOTAL: ${subtotal:.2f}\n\tIMPUESTO (21%): ${impuesto:.2f}\n\tTOTAL: ${total_a_pagar:.2f}\n\n\t{MAGENTA}------------------------------------------------------------------{RED}\n\n\t\t\t      ¡GRACIAS POR SU COMPRA!{RED}\n\n\t\t\t     {YELLOW}www.pizzeriaeureka.com.ar\n\t\t\t    info@pizzeriaeureka.com.ar\n\n\t{RED}******************************************************************\n\n{RESET}\n")
    

# while donde se llevara a cabo la muestra del menú y todas las funciones antes declaradas para que el usuario pueda elegir un plato/comida/agregado y luego se guarde en su lista de pedidos para que por último se le muestre su correspondiente ticket
while seguir == 1:
    
    limpiar_pantalla()
    print(f'{WHITE}\n\n\t***********************  {RED}PIZZERIA EUREKA  {WHITE}***********************\n\n\t\t     {GREEN}"No sacrifiques el sabor por la rapidez,\n\t\t      en nuestro restaurante lo tenemos todo."\n\n\n\t\t\t\t      {YELLOW}MENÚ:\n\n\t\t\t\t   {YELLOW}1) {BLACK}- {WHITE}Pizzas\n\t\t\t\t   {YELLOW}2) {BLACK}- {WHITE}Empanadas\n\t\t\t\t   {YELLOW}3) {BLACK}- {WHITE}Sandwiches\n\t\t\t\t   {YELLOW}4) {BLACK}- {WHITE}Milanesas\n\t\t\t\t   {YELLOW}5) {BLACK}- {WHITE}Papas\n\t\t\t\t   {YELLOW}6) {BLACK}- {WHITE}Ensaladas\n\t\t\t\t   {YELLOW}7) {BLACK}- {WHITE}Bebidas\n\t\t\t\t   {YELLOW}8) {BLACK}- {WHITE}Promociones\n\n\t{WHITE}******************************************************************')
    eleccion = evitar_error(f"{GREEN}\n\nPara elejir una opción ingrese el número de esta{WHITE}: ",8,"lista")

    if eleccion == 1:
        categoria=evitar_error(f"{YELLOW}\nElegiste la opción de pizzas!!\n\n\t1- {WHITE}Pizza Vegetariana\n\t{YELLOW}2- {WHITE}Pizza NO Vegetaria\n\n{MAGENTA}¿Qué opción eliges?{WHITE}: ",None,"1-2")
        print("")
        if categoria == 1: comida(pizzaV,cont_principal,cont_cantidad,pizza_V_Agr,cont_ingr,nombre_pri="Pizza Vegetariana")
        elif categoria == 2: comida(pizzaNoV,cont_principal,cont_cantidad,pizza_noV_Agr,cont_ingr,nombre_pri="Pizza NO Vegetariana")

    elif eleccion == 2: 
        print(f"{YELLOW}Elegiste la opción de Empanadas!!\n\t")
        comida(empanadas,cont_principal,cont_cantidad,general_Agr,cont_ingr,nombre_pri="Empanada")

    elif eleccion == 3:
        categoria=int(input(f"{YELLOW}Elegiste la opción de Sandwich!!\n\t1- {WHITE}Tradicional\n\t{YELLOW}2- {WHITE}Tostados\n\t{YELLOW}3- {WHITE}Hamburguesas\n\t{YELLOW}4- {WHITE}Lomitos\n{MAGENTA}¿Qué opción eliges?{WHITE}: "))
        print("")
        if categoria == 1: comida(sandwiches,cont_principal,cont_cantidad,general_Agr,cont_ingr,nombre_pri="Sandwich")
        elif categoria == 2: comida(tostado,cont_principal,cont_cantidad,general_Agr,cont_ingr,nombre_pri="Tostado")
        elif categoria == 3: comida(burg,cont_principal,cont_cantidad,general_Agr,cont_ingr,nombre_pri="Hamburguesa")
        elif categoria == 4: comida(lomitos,cont_principal,cont_cantidad,general_Agr,cont_ingr,nombre_pri="Lomito")

    elif eleccion == 4:
        print(f"{YELLOW}Elegiste la opción de Milanesas!!\n\t")
        comida(milanesa,cont_principal,cont_cantidad,general_Agr,cont_ingr,nombre_pri="Milanesa")   

    elif eleccion == 5:
        print(f"{YELLOW}Elegiste la opción de Papas!!\n\t")
        comida(papas,cont_principal,cont_cantidad,papas_Agr,cont_ingr,nombre_pri="Papas Fritas")  

    elif eleccion == 6:
        print(f"{YELLOW}Elegiste la opción de Ensaladas!!\n\t")
        comida(ensaladas,cont_principal,cont_cantidad,ensa_Agr,cont_ingr,nombre_pri="Ensalada")

    elif eleccion == 7:
        print(f"{YELLOW}Elegiste la opción de Bebidas!!\n\t")
        comida(bebidas,cont_principal,cont_cantidad,bebi_Agr,cont_ingr,nombre_pri="Bebida")

    elif eleccion == 8:
        print(f"{YELLOW}Elegiste la opción de Promociones!!\n\t")
        comida(promociones,cont_principal,cont_cantidad,bebi_Agr,cont_ingr,nombre_pri="Promoción")
    
    seguir=evitar_error(f"{MAGENTA}\n¿Deseas seguir añadiendo mas comida/bebida a su pedido?\n\n\t{YELLOW}0) {BLACK}- {WHITE}(Cerrar)\n\t{YELLOW}1) {BLACK}- {WHITE}(Continuar)\n{MAGENTA}Ingrese el número de la opción que elije{WHITE}: ",None,"0-1")

crear_factura(pedidos_finales)
print(f"{BLUE}\n\n¡GRACIAS POR VISITARNOS, QUE TENGA UN LINDO DÍA!\n-------------------------------------------------\n\n{RESET}")

