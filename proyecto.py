# PONER AL INICIO DEL CODIGO Y EJECUTAR
# UNA SOLA VEZ, O CADA QUE SE QUIERA RESETEAR 
# LOS ASIENTOS DEL AVION

columna=[]
fila=[]
aux=[]
contAs=0
for x in range(14):
    for j in range(3):
        contAs +=1
        fila.append(contAs)
        aux=fila.copy()
    columna.append(aux)
    fila.clear()
    
# SELECCIONAR ASIENTO DEL AVION

def Selec_Asiento(nroPedido):
  
  nroAsiento=0
  proceso=True
  while proceso:
    for x in range(len(columna)):   
      for j in range(len(aux)):      
        nroAsiento +=1
        if nroPedido==nroAsiento:
          if columna[x][j]=="X":
            print("Asiento no disponible")
            proceso=False
            break
          else:
            columna[x][j]="X"
            proceso=False
            break
            
# MUESTRA EL ESTADO ACTUAL DE LOS ASIENTOS DISPONIBLES Y/O OCUPADOS

def Estado_Asientos():
  print("|",columna[0][0],columna[0][1],columna[0][2],"\t",columna[1][0],columna[1][1],columna[1][2],"|",sep="\t")
  print("|","|",sep="\t"*9)
  print("|",columna[2][0],columna[2][1],columna[2][2],"\t",columna[3][0],columna[3][1],columna[3][2],"|",sep="\t")
  print("|","|",sep="\t"*9)
  print("|",columna[4][0],columna[4][1],columna[4][2],"\t",columna[5][0],columna[5][1],columna[5][2],"|",sep="\t")
  print("|","|",sep="\t"*9)
  print("|",columna[6][0],columna[6][1],columna[6][2],"\t",columna[7][0],columna[7][1],columna[7][2],"|",sep="\t")
  print("|","|",sep="\t"*9)
  print("|",columna[8][0],columna[8][1],columna[8][2],"\t",columna[9][0],columna[9][1],columna[9][2],"|",sep="\t")

  print(" |","_"*23,"\t\t","     ","_"*23,"|")
  print(" |","_"*23,"\t\t","     ","_"*23,"|")


  print("|",columna[10][0],columna[10][1],columna[10][2],"\t",columna[11][0],columna[11][1],columna[11][2],"|",sep="\t")
  print("|","|",sep="\t"*9)
  print("|",columna[12][0],columna[12][1],columna[12][2],"\t",columna[13][0],columna[13][1],columna[13][2],"|",sep="\t")
  print("|","|",sep="\t"*9)


# ANULACION DE ASIENTOS

def Anular_Asiento(recorrido):
  contador=0
  for x in range(14):
    for j in range(3):
      contador+=1
      if contador==recorrido:
        columna[x][j]=contador
        print("Asiento Liberado Exitosamente")
        



# menú básico
menu=True
válido=True
while menu:
    print("*"*40)
    print(" bienvenido a las aereolineas DUOC")
    print(" 1- ver asientos disponibles")
    print(" 2- comprar asiento")
    print(" 3- anular pasaje")
    print(" 4- modificar datos del de pasajero")
    print(" 5- salir" )
    print("*"* 40)
    while válido:
      try:
          op=int(input("elija una opción 1 o 2 o 3 o 4 o 5 : "))
          if op== 1 or op ==2 or op ==3 or op ==4 or op ==5 :
              break
          else:
              print("debe ingresar una opción válida ")
      except:
          print("debe ingresar una opción desde el 1 al 5")

    if op ==1:
        Estado_Asientos()
        print(" disponibilidad de asientos ")
        


    elif op ==2: 
        nombreClient=str(input(" ingrese su nombre : "))
        while válido:
            try:
                rutClient=int(input(" ingrese su rut, en caso de poseer  dígito verificador perteneciente al (K), reemplace por un 0 : "))
                if rutClient >=10000000 and rutClient <= 999999999:
                    break
                else:
                    print(" debe ingresar un rut válido")
            except:
                print(" debe ingresar un rut desde el rango 10000000 y 999999999")

        while válido:
            try:
                teleclient=int(input( "ingrese su teléfono celular : "))
                if teleclient >= 100000000 and teleclient <= 999999999:
                    break
                else:
                    print(" debe ingresar  un número de contacto de 9 dígitos ")
            except:
                print(" debe ingresar un número de contacto válido ")
        bancoClient=str( input(" ingrese el banco al cual esta afiliado, banco duoc/ otros : "))
        bancoClient .lower()
        if bancoClient == "banco duoc" or "bancoduoc":
          descBanco
        else:
          print(" no hay descuento ")




    elif op ==5:
     

        print("saliendo del sistema.....")
        break
