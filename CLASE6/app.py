from flask import Flask
from login import login #Importamos el blueprint desde Login.py
from logout import logout

app = Flask(__name__)
app.register_blueprint(login) #registramos el blueprint
app.register_blueprint(logout)
@app.route('/')
def home():
    return "Hola, Unida Experto en Pyrhon!"
if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')