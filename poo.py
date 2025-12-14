# Programación Orientada a Objetos (POO)

class ClimaSemana:
    def __init__(self):
        self.temperaturas = []

    def agregar_temp(self, t):
        self.temperaturas.append(t)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Función principal
def main():
    clima = ClimaSemana()  # Creamos una instancia de la clase ClimaSemana
    for i in range(7):  # 7 días de la semana
        temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
        clima.agregar_temp(temperatura)
    
    promedio = clima.promedio()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f} °C")

if __name__ == "__main__":
    main()
