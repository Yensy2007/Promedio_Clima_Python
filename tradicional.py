# Programación Tradicional

def obtener_temperaturas():
    temperaturas = []
    for i in range(7):  # Para 7 días de la semana
        temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal
def main():
    temperaturas = obtener_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f} °C")

if __name__ == "__main__":
    main()
