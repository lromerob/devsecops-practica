# Dockerfile Seguro y Mitigado - Pr?ctica 4 DevSecOps
FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Crear el usuario sin privilegios exigido por la gu?a
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY requirements.txt .

# MITIGACI?N: Forzamos la actualizaci?n de pip, wheel y setuptools para eliminar los CVEs HIGH detectados por Trivy
RUN pip install --no-cache-dir --break-system-packages --upgrade pip setuptools wheel

# Instalar los requerimientos de la app (Flask y Azure SDK)
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

COPY app.py .

# Cambiar permisos al usuario no-root
RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
