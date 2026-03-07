# Solicitar la temperatura actual
#temperatura = float(input("Digite la temperatura actual de la sala de servidores (°C): "))

# Verificar si la temperatura es crítica
#if temperatura >= 25:
   #print("¡ALERTA! La temperatura es crítica")
   #print(f"La temperatura actual de {temperatura}°C supera el límite recomendado de 25°C")
#else:
 #  print("La temperatura está dentro del rango seguro")
  # print(f"Temperatura actual: {temperatura}°C")

#temperatura = float(input("Digite la temperatura actual de la sala de servidores (°C): "))
#if temperatura >= 25:
   # print("¡ALERTA! La temperatura es crítica")
    #print(f"La temperatura actual de {temperatura}°C supera el límite recomendado de 25°C")
#else:
 #print("La temperatura está dentro del rango seguro")
  #print(f"Temperatura actual: {temperatura}°C")

# Solicitar y validar la puntuación y los años trabajados
#while True:
    #try:
       #puntuacion = float(input("Ingrese la puntuación del desempeño (0 a 100): "))
        #anios = int(input("Ingrese la cantidad de años trabajados: "))
    #except ValueError:
        #print("Entrada no válida. Por favor ingrese números.")
        #continue

    #if not 0 <= puntuacion <= 100:
        #print("La puntuación debe estar entre 0 y 100.")
        #continue
    #if anios < 0:
        #print("Los años trabajados no pueden ser negativos.")
        #continue
    #break

# Lógica de decisión (umbral original: 7)
#if puntuacion >= 7:
    #if anios > 5:
        #print("Elegible para ascenso")
    #else:
        #print("Buen desempeño, sigue así")
#else:
    #print("Necesita mejorar")
    


# pedir y validar un entero
while True:
    try:
        numero = int(input("Ingresa un número entero: "))
        break
    except ValueError:
        print("Entrada no válida. Por favor ingresa un número entero.")

# comprobar divisibilidad
if numero % 3 == 0 and numero % 5 == 0:
    print("¡Número mágico!")
elif numero % 3 == 0:
    print("Divisible por 3")
elif numero % 5 == 0:
    print("Divisible por 5")
else:
    print("No es un número mágico")

