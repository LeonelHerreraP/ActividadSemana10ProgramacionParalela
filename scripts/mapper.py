import sys  # Importa el módulo para leer entrada estándar (stdin)

# Itera sobre cada línea recibida desde la entrada estándar (proporcionada por Hadoop)
for linea in sys.stdin:
    palabras = linea.strip().split()  # Elimina espacios y divide la línea en palabras
    for palabra in palabras:
        # Imprime la palabra en minúscula seguida del número 1, separados por tabulación
        print("{}\t{}".format(palabra.lower(), 1))
