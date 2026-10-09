from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from logica import calcular, OPERACIONES

app = Flask(__name__)
CORS(app)

historial = []  # vive en memoria del backend (no hay base de datos)


@app.route("/api/operaciones", methods=["GET"])
def api_operaciones():
    print("[BACKEND] La UI pidió el catálogo de operaciones")
    return jsonify(OPERACIONES)


@app.route("/api/calcular", methods=["POST"])
def api_calcular():
    datos = request.get_json()
    print(f"[BACKEND] Petición recibida: {datos}")
    try:
        operacion = datos["operacion"]
        a = float(datos["a"])
        unaria = OPERACIONES.get(operacion, {}).get("unaria", False)
        b = 0.0 if unaria else float(datos["b"])

        resultado = calcular(a, b, operacion)
        print(f"[LÓGICA] {operacion}({a}, {b}) = {resultado}")

        historial.append({
            "hora": datetime.now().strftime("%H:%M:%S"),
            "operacion": operacion,
            "a": datos["a"],
            "b": None if unaria else datos["b"],
            "resultado": resultado,
        })
        return jsonify({"ok": True, "resultado": resultado})
    except (ValueError, KeyError, TypeError, OverflowError) as e:
        print(f"[LÓGICA] Error: {e}")
        return jsonify({"ok": False, "error": str(e)}), 400


@app.route("/api/historial", methods=["GET"])
def api_historial():
    return jsonify(historial)


@app.route("/api/historial", methods=["DELETE"])
def api_borrar_historial():
    historial.clear()
    print("[BACKEND] Historial borrado")
    return jsonify({"ok": True})


if __name__ == "__main__":
    app.run(port=5000, debug=True)