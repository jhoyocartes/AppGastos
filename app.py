from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'data/gastos.json'

# Funciones para manejar la carga y guardado de datos


def cargar_datos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"personas": [], "gastos": []}


def guardar_datos(datos):
    with open(DATA_FILE, 'w') as f:
        json.dump(datos, f, indent=4)

# Ruta principal para mostrar el formulario y los resultados


@app.route('/', methods=['GET', 'POST'])
def index():
    datos = cargar_datos()
    personas = datos['personas']
    gastos = datos['gastos']

    if request.method == 'POST':
        # Recibir datos del formulario
        cantidad = float(request.form['cantidad'])
        pagador = request.form['pagador']
        beneficiarios = request.form.getlist('beneficiarios')

        # Crear un nuevo gasto
        nuevo_gasto = {
            'cantidad': cantidad,
            'pagador': pagador,
            'beneficiarios': beneficiarios
        }
        gastos.append(nuevo_gasto)
        guardar_datos(datos)

        return redirect(url_for('index'))

    # Cálculo de saldos
    saldos = calcular_saldos(personas, gastos)
    transacciones = calcular_transacciones(saldos)

    return render_template('index.html', personas=personas, transacciones=transacciones, gastos=gastos)

# Ruta para agregar nuevas personas


@app.route('/agregar_persona', methods=['POST'])
def agregar_persona():
    nombre = request.form['nombre']
    datos = cargar_datos()
    datos['personas'].append(nombre)
    guardar_datos(datos)
    return redirect(url_for('index'))

# Ruta para eliminar personas


@app.route('/eliminar_persona', methods=['POST'])
def eliminar_persona():
    nombre = request.form['nombre']
    datos = cargar_datos()

    if nombre in datos['personas']:
        datos['personas'].remove(nombre)
        # Eliminar gastos relacionados
        datos['gastos'] = [
            gasto for gasto in datos['gastos']
            if gasto['pagador'] != nombre and nombre not in gasto['beneficiarios']
        ]

    guardar_datos(datos)
    return redirect(url_for('index'))

# Función para calcular saldos


def calcular_saldos(personas, gastos):
    saldos = {persona: 0 for persona in personas}

    for gasto in gastos:
        if gasto['pagador'] is None or not gasto['beneficiarios']:
            continue  # Omitir gastos con pagador None o sin beneficiarios

        monto_por_persona = gasto['cantidad'] / len(gasto['beneficiarios'])
        for beneficiario in gasto['beneficiarios']:
            if beneficiario in saldos:
                saldos[beneficiario] -= monto_por_persona
        if gasto['pagador'] in saldos:
            saldos[gasto['pagador']] += gasto['cantidad']

    return saldos

# Función para calcular quién le debe a quién


def calcular_transacciones(saldos):
    deudores = [(p, s) for p, s in saldos.items() if s < 0]
    acreedores = [(p, s) for p, s in saldos.items() if s > 0]

    transacciones = []

    while deudores and acreedores:
        deudor, deuda = deudores.pop(0)
        acreedor, credito = acreedores.pop(0)

        pago = min(-deuda, credito)
        transacciones.append((deudor, acreedor, f"${pago:.2f}"))  # Formatear con $ y 2 decimales

        deuda += pago
        credito -= pago

        if deuda < 0:
            deudores.insert(0, (deudor, deuda))
        if credito > 0:
            acreedores.insert(0, (acreedor, credito))

    return transacciones



if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
