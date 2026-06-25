# Práctica #2 - API REST con Flask

## Descripción

Este proyecto corresponde a la **Práctica #2** del curso **Desarrollo con Plataformas Abiertas**.

Se desarrolló una API REST utilizando **Flask**, cumpliendo con los requisitos solicitados por el profesor y adaptando la temática al emprendimiento **Velaxing**, una marca de velas aromáticas artesanales.

## Tecnologías utilizadas

* Python 3.13
* Flask
* Flask-CORS
* Postman
* Git
* GitHub

## Estructura del proyecto

```text
tareas-plataformas-abiertas
│
├── .gitignore
├── requirements.txt
└── estudiantes
    └── data
        └── v1
            ├── run.py
            └── app
                ├── __init__.py
                └── controllers
                    └── velaxing.py
```

## Instalación

Instalar las dependencias del proyecto:

```bash
py -m pip install -r requirements.txt
```

## Ejecución

Ubicarse en la carpeta:

```bash
cd estudiantes/data/v1
```

Ejecutar la API:

```bash
py run.py
```

La aplicación se ejecutará en:

```text
http://127.0.0.1:5000
```

## Endpoints disponibles

### 1. Bienvenida

**Método:** GET

```text
/estudiantes/api/v1/hola
```

**Respuesta**

```json
{
    "mensaje": "¡Bienvenido a Velaxing! Donde cada vela ilumina momentos especiales."
}
```

---

### 2. Saludo personalizado

**Método:** GET

```text
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

## Pruebas

Los endpoints fueron probados utilizando **Postman** y también desde el navegador, verificando el correcto funcionamiento de la API y los códigos de respuesta HTTP correspondientes.

## Autora

Estefanía Quesada
