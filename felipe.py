if op==4:
    while valido:
        try:
            rut=int(input("modificar datos del usuario: \n ingrese rut el cliente (sin puntos ni guion verificador) y su numero de asiento:\n rut: "))
            numasiento=int(input("asiento: "))
            if rut>=10000000 and rut<= 999999999999 and numasiento>=1 and numasiento<=42:
                    if rut==rutClient:
                        print("nombre",nombreClient,"\nrut:",rutClient,"\ntelefono:",teleclient,"\nbanco:",bancoClient,"\nnumero de asiento:",numasiento)    
                        while valido:
                            try:
                                datoclient=input("por favor elija los datos a modificar del cliente: (nombre/telefono):\n")      
                                if datoclient=="nombre":
                                    nombreclient=input("ingrese el nuevo nombre del cliente: ")
                                    print("¡datos guardados exitosamente!")
                                    datocliente
                                    break       
                                elif datoclient=="telefono":
                                    teleclient=int(input("ingrese el nuevo numero de telefono: "))        
                                    if teleclient>=12345678 and teleclient<=98765432:
                                        print("¡datos guardados exitosamente!")
                                        datocliente
                                        break
                            except:
                                print("error. siga las instrucciones correctamente")      
                        break
            else:
                print("rut incorrecto o no registado")  
        except ValueError:
            print("ingrese los datos correctamente por favor")
