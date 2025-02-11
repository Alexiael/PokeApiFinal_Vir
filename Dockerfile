# Usa la imagen oficial de Python
FROM python:3.10-slim

# Crea un directorio de trabajo
WORKDIR /app

# Copia primero el archivo de requirements para aprovechar la cache en Docker
COPY requirements.txt .

# Instala dependencias del sistema (build-essential, si algunas librerías necesitan compilarse)
RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*

# Instala las dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia el resto del proyecto a /app
COPY . .

# Expone el puerto 8000 (FastAPI)
EXPOSE 8000

# Comando para arrancar la app con uvicorn en modo "producción"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
