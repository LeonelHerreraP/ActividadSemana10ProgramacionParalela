```markdown
# WordCount con Hadoop MapReduce y Python Streaming

Este proyecto implementa un conteo de palabras (**WordCount**) utilizando **Hadoop MapReduce** y scripts en **Python**, ejecutado dentro de un clúster Hadoop montado con Docker y Docker Compose.

---

## 📁 Estructura del proyecto
```

HADOOPCLUSTER/
├── scripts/
│ ├── example.txt # Archivo de entrada con texto
│ ├── mapper.py # Script Python para la fase Map
│ └── reducer.py # Script Python para la fase Reduce
├── Dockerfile.namenode # Dockerfile que instala Python en el Namenode
├── docker-compose.yml # Define todos los servicios del clúster Hadoop
└── README.md # Esta guía

````

---

## 🧱 Requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- PowerShell, Terminal Linux o WSL (Windows Subsystem for Linux)

---

## 🚀 Instrucciones para ejecución

### 1. Construir y levantar el clúster

```bash
docker-compose up -d --build
````

> Espera unos segundos para que los contenedores namenode y datanode estén activos.

---

### 2. Entrar al contenedor del Namenode

```bash
docker exec -it namenode bash
```

---

### 3. Inicializar el sistema de archivos HDFS (solo la primera vez)

```bash
hdfs namenode -format
start-dfs.sh
```

> Si los daemon no arrancan, reinicia los contenedores o ejecuta `hadoop-daemon.sh start datanode`.

---

### 4. Crear el directorio en HDFS y subir el archivo de entrada

```bash
hdfs dfs -mkdir -p /input
hdfs dfs -put /data/example.txt /input
```

---

### 5. Ejecutar el job de MapReduce

```bash
hadoop jar /opt/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /input \
-output /output \
-mapper /data/mapper.py \
-reducer /data/reducer.py
```

> ⚠️ Si recibes el error de que `/output` ya existe:

```bash
hdfs dfs -rm -r /output
```

---

### 6. Ver el resultado

```bash
hdfs dfs -cat /output/part-00000
```

---

## 🧠 Sobre los scripts

### `mapper.py`

Lee cada línea, separa en palabras y emite pares `(palabra, 1)`:

```python
for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        print(f"{word.lower()}\t1")
```

### `reducer.py`

Agrupa por palabra y suma las ocurrencias:

```python
current_word = None
total = 0

for line in sys.stdin:
    word, count = line.strip().split('\t')
    count = int(count)

    if current_word == word:
        total += count
    else:
        if current_word:
            print(f"{current_word}\t{total}")
        current_word = word
        total = count

if current_word:
    print(f"{current_word}\t{total}")
```

---

## 🐳 Acceso al clúster

- Namenode Web UI: [http://localhost:9870](http://localhost:9870)
- ResourceManager UI: [http://localhost:8088](http://localhost:8088)

---

## 🧹 Limpieza del entorno

```bash
docker-compose down -v
```

Esto detiene y elimina contenedores, redes y volúmenes.
