from flask import Blueprint, request, jsonify

# Crear el Blueprint
velaxing_endpoints = Blueprint("velaxing_endpoints", __name__)


# Endpoint 1
@velaxing_endpoints.route("/hola", methods=["GET"])
def hola():
    return jsonify({
        "mensaje": "¡Bienvenido a Velaxing! Donde cada vela ilumina momentos especiales."
    }), 200


# Endpoint 2
@velaxing_endpoints.route("/saludo", methods=["GET"])
def saludo():

    nombre = request.args.get("nombre")

    if not nombre:
        return jsonify({
            "error": "Debe de ingresar el nombre del estudiante."
        }), 400

    return jsonify({
        "saludo": f"¡Hola {nombre}! Bienvenido a Velaxing."
    }), 200