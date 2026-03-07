# Solicitar la cantidad de manzanas vendidas
#manzanas = int(input("Digite la cantidad de manzanas vendidas: "))

# Solicitar la cantidad de plátanos vendidos
#platanos = int(input("Digite la cantidad de platanos vendidos: "))

# Comparar las ventas
#if manzanas > platanos:
#print("Las manzanas tuvieron más ventas")
#elif platanos > manzanas:
    #print("Los platanos tuvieron más ventas")
#else:
    #print("Hubo un empate en ventas")


# Solicitar la cantidad de plátanos vendidos

ingresos = float(input("ingrese los ingresos del trimestre:"))
gastos = float(input("ingrese los gastos del trimestre:"))
clientes_nuevos= int(input("ingrese el numero de nuevos clientyes:"))

beneficios = ingresos - gastos

if beneficios > 10000 and clientes_nuevos > 50:
    print("trimestre excelente")
elif beneficios > 5000 and clientes_nuevos>=20:
    print("trimestre bueno")
elif beneficios > 0:
    print("trimestre regular")
else:
    print("trimestre deficitario")        