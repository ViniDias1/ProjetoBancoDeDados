

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
	return jsonify(usuarios[0])


@app.route('/addUser', methods=['POST'])
def addUser():
	requisicao = request.get_json()
	cpf = requisicao["cpf"]
	novoUsuario = {

			"cpf": requisicao["cpf"],
			"nome": requisicao["nome"],
			"data_nascimento": requisicao["data_nascimento"]

        
    }
	usuarios = buscaUsuarios()
	try:
		usuarios[0][cpf] = novoUsuario
	except IndexError:
		usuarios.append({cpf:novoUsuario})
	

	salvarUsuario(usuarios)
	
	return ("Usuario cadastrado com sucesso!")

@app.route('/user/<int:cpf>')
def userBycpf(cpf):
	usuarios = buscaUsuarios()
	cpf = str(cpf)
	return jsonify(usuarios[0][cpf])
	


	
if __name__ == '__main__':
	app.run()
	
