# Imagen base oficial de Python 3
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el script Python al contenedor
COPY app.py .

# Expone el puerto 8097
EXPOSE 8097

# Comando para ejecutar el script al iniciar el contenedor
CMD ["python", "app.py"]

