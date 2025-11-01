from flask import Flask
from cliente import cliente

app = Flask(__name__)
app.register_blueprint(cliente)
@app.route('/')
def home():
    return "Seminario de Python"
if __name__ == '__main__':
    app.run(debug=True,port=5003,host='0.0.0.0')