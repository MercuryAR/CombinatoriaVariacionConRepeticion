# TP de Combinatoria - Caso 6: Variaciones con Repetición

Este proyecto contiene el desarrollo del **Trabajo Práctico de Combinatoria - Caso 6**, realizado para la materia Matemática Discreta en el año 2026. El programa calcula la cantidad de claves o contraseñas posibles de una longitud determinada (n) utilizando un conjunto de símbolos disponibles (m), donde la repetición de elementos está permitida y el orden de los mismos es importante.

---

## 👥 Integrantes

- **Paulo Orsini**
- **Luis Troche**
- **Comisión:** 9
- **Año:** 2026

---

## 📐 Fundamento Teórico

El problema plantea un escenario de **Variación con Repetición**.

- **Definición:** Dados m elementos distintos, las variaciones con repetición de estos m elementos tomados de n en n son los diferentes grupos que se pueden formar de manera que en cada grupo haya n elementos (pudiendo repetirse) y dos grupos se consideran distintos si difieren en algún elemento o en su orden.
- **Fórmula Matemática:**

  ```
  VR(m, n) = m^n
  ```

Donde:

- **m** = Cantidad de símbolos disponibles (número entero positivo, m ≥ 1).
- **n** = Longitud de la clave (número entero positivo, n ≥ 1).

---

## 🛠️ Requisitos previos

Para ejecutar este programa solo necesitás tener instalado **Python 3** en tu sistema. El programa utiliza la librería **`math`**, que viene incluida en Python y no requiere instalación adicional.

### Verificar instalación de Python:

Podés verificar si tenés Python instalado ejecutando el siguiente comando en tu terminal:

```bash
python3 --version
```

---

## 🚀 Instrucciones de Uso

1. **Abrir la Terminal:** Abrí tu terminal (Consola, Símbolo del Sistema o Terminal de macOS/Linux) y navegá hasta el directorio del proyecto:

   ```bash
   cd ruta/al/proyecto
   ```

2. **Ejecutar el Programa:** Corré el script `tp_combinatoria.py` con el siguiente comando:

   ```bash
   python3 tp_combinatoria.py
   ```

3. **Ingresar los Datos:**
   - El programa te dará la bienvenida y te solicitará ingresar el valor de **m** (símbolos disponibles).
   - Luego te solicitará ingresar el valor de **n** (longitud de la clave).
   - **Validación de entrada:** El programa cuenta con validación robusta. Si ingresás letras, símbolos no numéricos o valores fuera de rango (números negativos, cero o decimales), el sistema te informará del error y te solicitará el ingreso nuevamente hasta que sea correcto.

4. **Obtener el Resultado:** Una vez ingresados los datos válidos, se mostrará en pantalla la cantidad de claves posibles calculadas con la fórmula teórica. Si el resultado supera los 4300 dígitos, el programa lo indicará en notación aproximada (`≈ 10^n`) en lugar de mostrar el número completo.

---

## 📝 Ejemplos de Ejecución

### Ejemplo 1: Clave de 4 símbolos usando 4 disponibles → VR(4, 4)

```text
Bienvenidos al TP de Combinatoria - Caso 6
Alumnos Paulo Orsini y Luis Troche
Comisión 9 - Año 2026

Este programa calcula la cantidad de claves posibles de longitud n
usando m símbolos disponibles, con repetición permitida y orden importante.
Tipo de conteo: Variación con Repetición → Fórmula: VR(m, n) = m^n

Ingrese el valor de m (cantidad de símbolos disponibles): -4
Error: El valor de m debe ser un número natural (entero positivo)
Ingrese el valor de m (cantidad de símbolos disponibles): 4
Ingrese el valor de n (longitud de la clave): -2
Error: El valor de n debe ser un número natural (entero positivo)
Ingrese el valor de n (longitud de la clave): 4

La cantidad de claves posibles es: 256
Este programa resuelve una combinatoria de variación con repetición cuya fórmula es: VR(m, n) = m^n
```

### Ejemplo 2: Clave de 5 símbolos usando 3 disponibles → VR(3, 5)

```text
Ingrese el valor de m (cantidad de símbolos disponibles): a
Error: Por favor, ingrese un número válido
Ingrese el valor de m (cantidad de símbolos disponibles): 3
Ingrese el valor de n (longitud de la clave): d
Error: Por favor, ingrese un número válido
Ingrese el valor de n (longitud de la clave): 5

La cantidad de claves posibles es: 243
Este programa resuelve una combinatoria de variación con repetición cuya fórmula es: VR(m, n) = m^n
```

### Ejemplo 3: Resultado con más de 4300 dígitos → VR(10, 4301)

```text
Ingrese el valor de m (cantidad de símbolos disponibles): 10
Ingrese el valor de n (longitud de la clave): 4301

La cantidad de claves posibles es: aproximadamente 10^4302 (resultado demasiado grande para mostrar completo)
Este programa resuelve una combinatoria de variación con repetición cuya fórmula es: VR(m, n) = m^n
```

---

## 📂 Estructura del Proyecto

- `tp_combinatoria.py`: Script principal interactivo en Python. Contiene las validaciones de entrada, la función de cálculo `resolver(m, n)` y la interfaz de consola.
- `README.md`: Este archivo, con la documentación e instrucciones de uso.
- `PRD_Programa_de_Combinatoria.pdf`: Documento de requisitos del producto.
