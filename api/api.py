

from flask import Flask, jsonify, request
import json
from flask_cors import CORS # PARA TESTE COM FRONT END


app = Flask(__name__)
CORS(app,resources={r"/*": {"origins": "*"}}) # PARA TESTE COM FRONT END

def buscaUsuarios():
	try:
		with open("api/arquivo.json", 'r') as arquivo:
			try:
				return json.load(arquivo)
			except json.JSONDecodeError:	
				return []
			
	except FileNotFoundError:
		return []


def salvarUsuario(usuarios):
	with open("api/arquivo.json", 'w') as arquivo:
		json.dump(usuarios, arquivo, indent=4)
		

@app.route('/allUsers', methods=['GET'])
def allUsers():

	usuarios = buscaUsuarios()
	return jsonify(usuarios)


@app.route('/addUser', methods=['POST'])
def addUser():
	requisicao = request.get_json()

	novoUsuario = {
        "cpf": requisicao["cpf"],
        "nome": requisicao["nome"],
        "data_nascimento": requisicao["data_nascimento"]
    }
	usuarios = buscaUsuarios()
	usuarios.append(novoUsuario)

	salvarUsuario(usuarios)
	
	return ("Usuario cadastrado com sucesso!")

@app.route('/user/<int:cpf>')
def userBycpf(cpf):
	usuarios = buscaUsuarios()
	for i in usuarios:
		if i["cpf"] == cpf:
			return jsonify(i)
	


	
if __name__ == '__main__':
	app.run()
	
