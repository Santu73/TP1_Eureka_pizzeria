
# variables:
seguir = 1
eleccion = 1
pedidos_finales = []
precio_total = 0
cont_principal = 0 
cont_cantidad = 0 
cont_ingr = 0
contador2 = 0 
cant = 0
suma = 0

"""
cont_principal (int): Contador de opciones de comida principal.
cont_cantidad (int): Contador de cantidad de unidades.
cont_ingr (int): Contador de opciones de ingredientes adicionales.
nombre_pri (str): Nombre de la comida principal.
unidades (int): Cantidad de unidades del pedido.
op (int): Opción elegida del pedido.
msj (str): Mensaje para solicitar entrada de datos al usuario.
estado (str): Estado actual de la entrada de datos.
eleccion (int): Valor numérico ingresado por el usuario.

lista_comida (list): Lista de comida disponible.
lista_agr (list): Lista de ingredientes adicionales.
pedidos_finales (dict): Lista con los pedidos finales.
lista_pedido (list): Lista de pedido disponible.


"""

# listas:
pizzaV=["Muzzarela","Salsa y mozzarella",1020,"Doble Muzzarela","Salsa y doble mozzarella",1420,"Ananá(Sin jamón)","Salsa, mozzarella y ananá",1500,"Choclo","Salsa, mozzarella y granos de choclo",1900,"Napolitana","Salsa, mozzarella y tomates en varilla",1200,"Fugazzeta","Salsa, mozzarella y cebolla en varilla",1300]
pizzaNoV=["Calabresa","Salsa, mozzarella y salchicha calabresa en rodajas",900,"Napolitana con Jamón","Salsa, mozzarella, tomates en rodajas y jamón",1200,"Muzzarella con Jamón y Huevo","Salsa, mozzarella, jamón, huevo",1000,"Muzzarella con Panceta y Cebolla","salsa, mozzarella, panceta, cebolla",1300]
empanadas=["Jamon y queso","Jamón, queso y huevo batido",170,"Humita","Choclo, cebolla, ají, queso, leche y harina",190,"Criollas","Carne, cebolla, pimiento, aceitunas, pasa de uvas y huevo",180,"Arabes","Carne, cebolla, limón, aceitunas, y huevo",180,"Cebolla y Queso","Cebolla, aceitunas y queso",170,"Pollo","Pollo,cebolla, pimiento, aceitunas y huevo",180,"Verdura","Espinacas, zanahorias, zapallo, cebolla, queso, aceitunas y huevo",150]
sandwiches=["Sandwich de pollo","Pechuga de pollo, queso, lechuga o espinacas, tomate en rodajas y aderezo(opc)",1300,"Sandwich de milanesa","Milanesa de ternera o pollo, queso, lechuga o espinacas, tomate en rodajas y aderezo(opc)",1420,"Jamón y Queso","Jamón, queso, lechuga o espinacas, tomate en rodajas y aderezo(opc)",1100,"Vegetariano","Queso, palta, tomate, pepino, lechuga o espinacas, aderezo(opc)",1230]
tostado=["Tostado simple","Jamón, queso y manteca",1000,"Tostado completo","Jamón, queso, manteca, huevo, tomate, lechuga o espinacas y aderezo(opc)",1100]
burg=["Hamburguesa Completa","Carne, Queso cheddar(opc), lechuga, tomate y aderezo(opc)",2300,"Hamburguesa Simple","Carne, Queso cheddar(opc), tocino, lechuga, tomate, cebolla, pepinillos y aderezo(opc)",1800]
lomitos=["Lomo de ternera","Bife de ternera, lechuga o espinacas, tomate, cebolla, pimiento, huevo frito y aderezo(opc)",1200,"Lomo de pollo","Pechuga de pollo, lechuga o espinacas, tomate, cebolla, pimiento, huevo frito y aderezo(opc)",1200,"Lomo criollo","Bife de chorizo o lomo de cerdo, lechuga o espinacas, tomate, cebolla, pimiento, Chimichurri y aderezo(opc)",1300]
milanesa=["Milanesa de carne","Carne vacuna, huevo y  pan rallado",1200,"Milansa de pollo","Pechuga de pollo, huevo y pan rallado",1400,"Bife de pollo al limón","Pechuga de pollo, limón y harina",1150,"Napolitana","Milanesa de pollo o carne, salsa, mozzarella, jamón y aceitunas",1300,"Costeleta de cerdo","Costeleta de cerdo, huevo y pan rallado",1100,"Medallón de pollo","Pechuga de pollo, huevo y pan rallado",1100,"Mila de merluza","Filete de merluza, harina, huevo y pan rallado",1300]
papas=["Fritas","Papas cortadas en bastones",750,"Con chedar","Papas fritas, queso cheddar y cebolla",900,"Al verdeo","Papas cortadas en cubos, cebolla, cebolla de verdeo y caldo de verdura",900,"Tortilla","Papas cortadas en rodajas, cebolla y huevo",1200 ]
ensaladas=["L-T-CEB","lechuga, tomate y cebolla",400,"L-T-Z","lechuga, tomate y zanahoria",450,"L-T-Z-H-JyQ","lechuga, tomate, zanahoria, hongos y jamón y queso",500]
bebidas=["Agua Mineral","2lt",200,"Agua Saborizada","2lt",230,"Coca-Cola","2lt",300,"Sprite","2lt",250,"Pritty","2lt",200,"Fanta","2lt",300,"Cerveza","1lt",580]
promociones=["2 Pizza Muzzarela + 1 Cerveza 1lt","Validos solo los fines de semana",2500,"1 Hamburguesa simple + 1 cono de papas + 1 Sprite 2lt","Validos solo los fines de semana",2300,"2 Tostados + 2 Agua saborizada 500mlt c/u","Validos solo los fines de semana",1500,"1 Ensalada L-T-CEB + 1 Agua saborizada 500mlt","Validos solo los fines de semana",800,"2 lomos criollo + 2 conos de papas + 2 Sprite 500mlt c/u","Validos solo los fines de semana",3200]
pizza_V_Agr=["Extra-Tofu","",40,"Extra-Pimiento","",40]
pizza_noV_Agr=["Extra-Peperoni","",45,"Extra-Jamon","",45,"Extra-Salmon","",45]
general_Agr=["Extra-choclo","",30,"Extra-Queso","",50,"Extra-Jamón","",60,"Extra-lomo","",80,"Extra-Carne","",80,"Extra-pollo","",60,"Extra-Aceituna","",10,"Extra-limón","",30,"Extra-Tomate","",50,"Extra-Pepino","",60,"Extra-Cebolla","",55,"Extra-Aderezo","",10]
papas_Agr=["Extra-oregano","",20,"Extra-Huevo","",40,"Extra-Chedar","",20,"Extra-Aceituna","",10]
ensa_Agr=["Extra-Lechuga","",40,"Extra-Tomate","",40,"Extra-Cebolla","",30,"Extra-Aceituna","",10,"Extra-Zanahoria","",30,"Extra-Hongos","",20]
bebi_Agr=["Vasos descartables","",20,"Sorbetes","",10,"Hielo","",50,"Maní","",30,"Rodajas de Limón","",10]


# Colores de texto en la terminal
RESET = '\033[0m'
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'

# Colores de fondo en la terminal
BG_RESET = '\033[49m'
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'