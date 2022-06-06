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
