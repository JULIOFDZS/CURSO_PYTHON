from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def login_user():
    user = request.json.get('user')
    password = request.json.get('password')
    print("Headers:", request.headers)
    print(f"Usuario: {user}, Password: {password}")

    codRes,menRes,accion = inicializarvariables(user, password) #Llama a la duncion de login

    salida = {
        "codRes": codRes,
        "menRes": menRes,
        "user": user,
        "accion": accion
    }
    return jsonify(salida)
def inicializarvariables(user, password):
    userlocal = "juliof"
    passlocal = "unida123"
    codRes = "SIN_ERROR"
    menRes = "OK"

    try:
        print("Verificar login")
        if user == userlocal and password == passlocal:
            print("Login exitoso")
            accion = "Succes"
        else:
            print("Usuario o contraseña incorrectos")
            codRes = "ERROR_1"
            menRes = "Usuario o Password incorrecto"
            print("Login fallido")
            accion="No_Succes"
    except Exception as e:
        print("ERROR", str(e))
        codRes = "ERRO"
        menRes = 'Msg' +str(e)
        accion = "Error interno"
    return codRes, menRes, accion

