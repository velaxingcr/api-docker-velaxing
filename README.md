# API Docker Velaxing

## Descripción

Este proyecto consiste en una API REST desarrollada con Flask y ejecutada dentro de un contenedor Docker.

El objetivo del proyecto es demostrar cómo Docker permite empaquetar una aplicación junto con todas sus dependencias para que pueda ejecutarse de forma idéntica en cualquier computadora.

## Tecnologías utilizadas

- Python 3.13
- Flask
- Flask-CORS
- Docker
- Git
- GitHub

---

# Estructura del proyecto

```text
api-docker
│
├── Dockerfile
├── README.md
├── requirements.txt
├── .gitignore
└── estudiantes
    └── data
        └── v1
            ├── run.py
            └── app
                ├── __init__.py
                └── controllers
                    └── velaxing.py
```

---

# Endpoints disponibles

## Endpoint 1 - Bienvenida

**Método**

```
GET
```

**Ruta**

```
/estudiantes/api/v1/hola
```

**Respuesta**

```json
{
    "mensaje": "¡Bienvenido a Velaxing! Donde cada vela ilumina momentos especiales."
}
```

---

## Endpoint 2 - Saludo personalizado

**Método**

```
GET
```

**Ruta**

```
/estudiantes/api/v1/saludo?nombre=Estefania
```

**Respuesta**

```json
{
    "saludo": "¡Hola Estefania! Bienvenido a Velaxing."
}
```

Si no se envía el parámetro **nombre**, la API devuelve:

```json
{
    "error": "Debe de ingresar el nombre del estudiante."
}
```

---

# Ejecución con Docker

## 1. Clonar el repositorio

```bash
git clone https://github.com/velaxingcr/api-docker-velaxing.git
```

## 2. Ingresar al proyecto

```bash
cd api-docker-velaxing
```

## 3. Construir la imagen Docker

```bash
docker build -t api-docker-velaxing .
```

## 4. Ejecutar el contenedor

```bash
docker run -p 5000:5000 api-docker-velaxing
```

---

# Probar la API

Abrir en el navegador:

```
http://127.0.0.1:5000/estudiantes/api/v1/hola
```

o

```
http://127.0.0.1:5000/estudiantes/api/v1/saludo?nombre=Estefania
```

---

# Dockerfile

El proyecto utiliza el siguiente flujo para crear la imagen Docker:

- Se utiliza una imagen oficial de Python 3.13.
- Se define una carpeta de trabajo dentro del contenedor.
- Se copian los archivos del proyecto.
- Se instalan las dependencias desde `requirements.txt`.
- Se expone el puerto 5000.
- Finalmente se ejecuta la aplicación Flask mediante `run.py`.

---

# Comandos útiles de Docker

Construir la imagen

```bash
docker build -t api-docker-velaxing .
```

Ejecutar el contenedor

```bash
docker run -p 5000:5000 api-docker-velaxing
```

Ver imágenes

```bash
docker images
```

Ver contenedores activos

```bash
docker ps
```

Ver todos los contenedores

```bash
docker ps -a
```

Detener un contenedor

```bash
docker stop <container_id>
```

---

# Integrantes

- Estefanía Quesada
- Meilyn Flores