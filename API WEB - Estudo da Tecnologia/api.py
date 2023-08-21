

from flask import Flask, jsonify, request
import json

app = Flask(__name__)


def buscaUsuarios():
	try:
		with open("arquivo.json", 'r') as arquivo:
			try:
				return json.load(arquivo)
			except json.JSONDecodeError:	
				return []
			
	except FileNotFoundError:
		return []


def salvarUsuario(usuarios):
	with open("arquivo.json", 'w') as arquivo:
		json.dump(usuarios, arquivo, indent=4)
		

@app.route('/allUsers', methods=['GET'])
def allUsers():

	usuarios = buscaUsuarios()
	return jsonify(usuarios[0])


@app.route('/addUser', methods=['POST'])
def addUser():
	requisicao = request.get_json()
	cpf = requisicao[0]["cpf"]
	novoUsuario = {

			"cpf": requisicao[0]["cpf"],
			"nome": requisicao[0]["nome"],
			"data_nascimento": requisicao[0]["data_nascimento"]

    }
	usuarios = buscaUsuarios()
	try:
		usuarios[0][cpf] = novoUsuario
	except IndexError:
		usuarios.append({cpf:novoUsuario})
	

	salvarUsuario(usuarios)
	
	return ("Usuario cadastrado com sucesso!")

@app.route('/user/<int:cpf>', methods=['GET'])
def userBycpf(cpf):
	try:
		usuarios = buscaUsuarios()
		cpf = str(cpf)
		return jsonify(usuarios[0][cpf])
	except KeyError:
		return (f"Usuario com o cpf |{cpf}| nao foi encontrado.")
	


	
if __name__ == '__main__':
	app.run()
	
