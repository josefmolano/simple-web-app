from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/prueba1', methods=['GET'])
def prueba1():
	return jsonify({'hola': 'mundo'}), 200

@app.route('/api/prueba2/num', methods=['GET'])
def prueba2(num):
	return jsonify({'respuesta': int(num)**2}), 200

@app.route('/api/registro/<nombre>/<apellido>/<edad>', methods=['GET'])
def registro_datos(nombre, apellido, edad):
	print(nombre)
	print(apellido)
	print(edad)
	return jsonify({'mensaje': nombre + ' ' + apellido + ' registrado'}), 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.run(host= '127.0.0.1')
