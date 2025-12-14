**Comparación entre Programación Tradicional y Programación Orientada a Objetos (POO) en Python**

Este proyecto presenta dos soluciones para calcular el promedio semanal de temperaturas, implementadas en Python utilizando:

Programación Tradicional (funciones)

Programación Orientada a Objetos (POO) (clases y métodos)

El objetivo es comprender las diferencias prácticas entre ambos enfoques, analizando la estructura del código, la organización y el estilo de programación.
1. **Programación Tradicional**

En este enfoque, el programa se basa principalmente en funciones independientes.
Las funciones se encargan de:

Solicitar las temperaturas de los 7 días.

Calcular el promedio semanal.

**Archivo: tradicional.py**

**Descripción del funcionamiento**

obtener_temperaturas() solicita los datos al usuario.

calcular_promedio() realiza la operación matemática.

main() controla el flujo del programa.
2. Programación Orientada a Objetos (POO)

En este enfoque se emplea una clase que representa la información del clima semanal.

**Archivo: orientacion_objetos.py**

**Descripción del funcionamiento**

La clase ClimaSemana contiene:

Una lista de temperaturas.

Un método agregar_temp() que añade cada dato ingresado.

Un método promedio() que calcula el promedio.

main() crea un objeto de esta clase y gestiona el flujo del programa.

Este paradigma facilita la organización del código y permite extender el programa con facilidad.

**Conclusiones**

Ambos métodos permiten resolver el mismo problema, pero POO ofrece una estructura más escalable y organizada.

La programación tradicional es útil para problemas simples y rápidos.

La POO es ideal para sistemas más grandes o cuando se requiere reutilización de código.

Python facilita ambos paradigmas con una sintaxis clara y amigable.
