FROM python:3.11-alpine

WORKDIR /app

COPY . /app/

# Actualiza pip
RUN /usr/local/bin/python -m pip install --upgrade pip

# Instala las dependencias para construir paquetes
RUN apk add --no-cache build-base mariadb-dev mariadb-connector-c-dev && \
    rm -rf /var/cache/apk/*

# Instala las dependencias
RUN pip install -r requirements.txt

CMD ["python", "src/app.py"]
