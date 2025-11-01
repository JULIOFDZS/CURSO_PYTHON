from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def login_user():
    ci = request.json.get('CI')
    print(f"CI: {ci}")

    codRes,menRes,nombre,apellidos,celular,dir = inicializarvariables(ci) 

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
def inicializarvariables(accion, ci, nombre, apellidos, celular, dir):
    accion = "Success"
    codRes = "SIN_ERROR"
    menRes = "OK"
    ci = "7426277"
    nombre = "Julio"
    apellidos = "Fernandez Silvero"
    celular = "0985154449"
    dir = "San Lorenzo"

    try:
        print("Verificar cliente")
        if ci == ci:
            print("Cliente encontrado")
        else:
            print("Cliente no encontrado")
            accion="Cliente no esta en el sistema"
            codRes = "ERROR"   
            menRes = "Error Cliente"
            ci = "7426277"
    except Exception as e:
        print("ERROR", str(e))
        codRes = "ERROR"
        menRes = 'Msg' +str(e)
        accion = "Error interno"