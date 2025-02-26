FROM python:3.10

RUN apt update && apt install -y libmariadb-dev

WORKDIR /app
COPY . /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
# Exponer el puerto en el que correrá la aplicación
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "tu_proyecto.wsgi:application"]
