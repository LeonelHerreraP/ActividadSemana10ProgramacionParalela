import sys  # Importa el módulo para leer entrada estándar (stdin)

palabra_actual = None  # Guarda la palabra que se está contando actualmente
total = 0 # Contador total de ocurrencias de la palabra

# Recorre cada línea de entrada recibida del mapper
for linea in sys.stdin:
    palabra, conteo = linea.strip().split('\t')  # Separa la palabra y el conteo
    conteo = int(conteo)  # Convierte el conteo a entero

    # Si es la misma palabra que la anterior, acumula el conteo
    if palabra_actual == palabra:
        total += conteo
    else:
        # Si la palabra cambió y no es la primera vez, imprime el total acumulado
        if palabra_actual:
            print("{}\t{}".format(palabra_actual, total))
        palabra_actual = palabra  # Actualiza a la nueva palabra
        total = conteo  # Reinicia el conteo para la nueva palabra

# Al finalizar, imprime la última palabra y su total
if palabra_actual:
    print("{}\t{}".format(palabra_actual, total))
