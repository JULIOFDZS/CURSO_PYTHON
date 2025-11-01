from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def login_user():
    ci = request.json.get('CI')
    print(f"CI recibido: {ci}")
    codRes, menRes, nombre, apellidos, celular, dir = inicializarvariables(ci) 

    salida = {
        "codRes": codRes,
        "menRes": menRes,
        "CI": ci,
        "nombre": nombre,
        "apellidos": apellidos,
        "celular": celular,
        "dir": dir
    }
    return jsonify(salida)
def inicializarvariables(ci_entrada): 
    codRes = "SIN_ERROR"
    menRes = "OK"
    nombre = "Julio"
    apellidos = "Fernandez Silvero"
    celular = "0985154449"
    dir = "Av. Brasilia"
    accion = "Success" 

    ci_valido = "7426277"

    try:
        print(f"Verificando cliente con CI: {ci_entrada}")
        if str(ci_entrada) == ci_valido:
            print("Cliente encontrado")
        else:
            print("Cliente no encontrado")
            accion = "Cliente no esta en el sistema"
            codRes = "ERROR" 
            menRes = "Error: Cliente no encontrado"

    except Exception as e:
        print("ERROR", str(e))
        codRes = "ERROR_500"
        menRes = f'Error Interno: {str(e)}'
        accion = "Error interno"
    return codRes, menRes, nombre, apellidos, celular, dir