asientoN = 78900
asientoV = 240000
contAN = 0
contAV = 0
sumaAN = 0
sumaAV = 0
ciclo = 0
print("¿desea comprar un asiento?\n1. si\n2. no ")
resp1 = int(input("ingrese opcion 1 o 2:\n"))
while ciclo == 0:
  print("¿Que tipo de asiento desea?\n1. Asiento normal\n2. Asiento vip")
  tipoA = int(input("ingrese opcion 1 o 2:\n"))
  if tipoA == 1:
    contAN = contAN + 1
    sumaAN = sumaAN + 1
    precioAN = asientoN * contAN
  else:
    if tipoA == 2:
      contAV = contAV + 1
      sumaAV = sumaAV + 1
      precioAV = asientoV * contAV
  print("¿desea comprar otro asiento?\n1.si\n2.no ")
  resp2 = int(input("ingrese opcion 1 o 2:\n"))  
  if resp2 == 1:
    ciclo = 0
  else:
    if resp2 == 2:
      ciclo = 1  
print("*"*40)
print(contAN, "asiento(s) normal comprado(s): ",precioAN)        
print(contAV,"asiento(s) vip comprado(s): ",precioAV)
print("*"*40)
print(sumaAN,"asiento(s) normal(es) vendidos")
print(sumaAV,"asiento(s) vip(s) vendidios")
  
