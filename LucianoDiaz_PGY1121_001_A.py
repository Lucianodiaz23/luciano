from datetime import datetime
def menu():
    print('----------Creativos.cl----------')
    print('Entradas Concierto Michael jam')
    print()
    print('Opcion 1. Comprar entradas')
    print('Opcion 2. Mostrar ubicaciones disponibles')
    print('Opcion 3. Ver listado de asistentes')
    print('Opcion 4. Mostrar ganancias totales')
    print('Opcion 5. Salir')
    print()

asiento_lista = [[1,2,3,4,5,6,7,8,9,10],
  [11,12,13,14,15,16,17,18,19,20],
  [21,22,23,24,25,26,27,28,29,30], 
  [31,32,33,34,35,36,37,38,39,40],
  [41,42,43,44,45,46,47,48,49,50],
  [51,52,53,54,55,56,57,58,59,60],
  [61,62,63,64,65,66,67,68,69,70],
  [71,72,73,74,75,76,77,78,79,80],
  [81,82,83,84,85,86,87,88,89,90],
  [91,92,93,94,95,96,97,98,99,100]]

def precios():
    print('Precio entradas')
    print()
    print('1. Platinum, $120000 (Asientos del 1 al 20)')
    print('2. Gold, $80000 (Asientos del 21 al 50)')
    print('3. Silver, $50000 (Asientos del 51 al 100)')
    print()

def asientos():
    print('Escenario')
    print()
    print('1 2 3 4 5 6 7 8 9 10')
    print('11 12 13 14 15 16 17 18 19 20')
    print('21 22 23 24 25 26 27 28 29 30')
    print('31 32 33 34 35 36 37 38 39 40')
    print('41 42 43 44 45 46 47 48 49 50')
    print('51 52 53 54 55 56 57 58 59 60')
    print('61 62 63 64 65 66 67 68 69 70')
    print('71 72 73 74 75 76 77 78 79 80')
    print('81 82 83 84 85 86 87 88 89 90')
    print('91 92 93 94 95 96 97 98 99 100')
    print()
    print()

def comprar_entradas():
    cant_entradas = int(input('Ingrese la cantidad de entradas que desea comprar: '))
    if cant_entradas > 3:
        cant_entradas = int(input('Tiene que ser entre 1 y 3, ingrese nuevamente: '))
    else:
      for i in range(cant_entradas):
          precios()
          asientos()
          print('Escenario con asientos ocupados')
          print()
          print(asiento_lista)

          selec_asiento = int(input('Seleccione un asiento: '))
          run_cliente = input('Ingrese su run: ')
          cedula_identidad = input('Ingrese su cedula de identidad: ')
          asiento_encontrado = False

          for fila in asiento_lista:
              if selec_asiento in fila:
                indice = fila.index(selec_asiento)
                fila[indice] = "X"
                asiento_encontrado = True
                break
          if asiento_encontrado:
                lista_entradas.append(selec_asiento)
                lista_entradas.append(run_cliente)
                lista_entradas.append(cedula_identidad)
                print('Asiento Ingresado Exitosamente')
          else:
                print('No se han encontrado asientos')      

def listado_asistentes():
    if len(lista_entradas) == 0:
        print('No hay asistentes registrados')
    else:
        print('Listado de asistentes:')
        lista_entradas_ordenadas = sorted(lista_entradas[1::3])
        for rut in lista_entradas_ordenadas:
          print(rut)

def ganancias_totales():
    ganancia_total = 0
    for i in range(0, len(lista_entradas), 3):
        asiento = lista_entradas[i]
        tipo_entrada = obtener_tipo_entrada(asiento)
        if tipo_entrada == "Platinum":
          ganancia_total += 120000
        elif tipo_entrada == "Gold":
          ganancia_total += 80000
        elif tipo_entrada == "Silver":
          ganancia_total += 50000
    return ganancia_total
def obtener_tipo_entrada(asiento):
    if asiento >= 1 and asiento <= 20:
      return "Platinum"
    elif asiento >= 21 and asiento <= 50:
      return "Gold"
    elif asiento >= 51 and asiento <= 100:
      return "Silver"
    else:
      return "Desconocido"
def salir():
    print('Hasta luego...')
    print('Luciano Diaz')
    fecha = datetime.now().date()
    print(fecha)


lista_entradas = []
while True:
    menu()
    op = int(input('Seleccione una opcion: '))
    if op > 0 and op < 6:
        if op == 1:
          comprar_entradas()
        if op == 2:
          print('Ubicaciones Disponibles')
          print()
          print(asiento_lista)
        if op == 3:
          listado_asistentes()
        if op == 4:
          ganancias = ganancias_totales()
          print(f'Ganancias Totales: ${ganancias}')
        if op == 5:
          salir()
          break
