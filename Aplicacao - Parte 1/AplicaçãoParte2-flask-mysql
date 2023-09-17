

from flask import Flask, jsonify, make_response, request
import json
import mysql.connector
from random import randint

conexao = mysql.connector.connect(
    host = "viniemarcelodb-mysql.cor5ekoknnbw.us-east-1.rds.amazonaws.com",
    user = "professor",
    password = "Professor123.",
    database = "mydb"
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


# ---- TABELA USUARIO ---- #	

# CREATE novo usuario
@app.route('/create_Usuario', methods=['POST'])
def create_Usuario():
	cursor = conexao.cursor()
	cpf = str(randint(1,1000))
	numero = randint(1,1000)
	idade = randint(1,100)

	sql = f"INSERT INTO Usuario VALUES ({cpf},'nome{cpf}','sobrenome{cpf}','login{cpf}','senha{cpf}','rua{cpf}','cep{cpf}',{numero},'bairro{cpf}','email{cpf}',{idade})"
	cursor.execute(sql)

	conexao.commit()
	cursor.close()
	return make_response("Usuario Cadastrado!")
# SELECT todos os usuarios
@app.route('/selectAll_Usuario', methods=['GET'])
def selectAll_Usuario():

	cursor = conexao.cursor()
	sql = "SELECT * FROM Usuario"
	cursor.execute(sql)
	resposta = cursor.fetchall()
	cursor.close()
	return make_response(
		jsonify(
			dados = resposta
		)
	)

# SELECT por cpf
@app.route('/selectUsuario_cpf/<int:cpf>', methods=['GET'])
def selectUsuario_cpf(cpf):

	cursor = conexao.cursor()
	sql = f"SELECT * FROM Usuario WHERE cpf = {cpf}"
	cursor.execute(sql)
	resposta = cursor.fetchall()
	cursor.close()
	return make_response(
		jsonify(
			dados = resposta
		)
	)

#UPDATE 
@app.route('/update_Senha_Usuario/<int:cpf>', methods=['PUT'])
def update_Senha_Usuario(cpf):
	cursor = conexao.cursor()
	sql = f"UPDATE Usuario SET senha = 'novaSENHA' WHERE cpf = {cpf}"
	cursor.execute(sql)
	conexao.commit()
	cursor.close()
	return make_response("Senha Alterada!")


#DELETE usuario
@app.route('/delete_Usuario/<int:cpf>', methods=['POST'])
def delete_Usuario(cpf):
	cursor = conexao.cursor()
	sql = f"DELETE FROM Usuario WHERE cpf = {cpf}"
	cursor.execute(sql)
	conexao.commit()
	cursor.close()
	return make_response("Usuario deletado!")

# ---- TABELA USUARIO ---- #	




# @app.route('/addUser', methods=['POST'])
# def addUser():
# 	requisicao = request.get_json()
# 	cpf = requisicao[0]["cpf"]
# 	novoUsuario = {

# 			"cpf": requisicao[0]["cpf"],
# 			"nome": requisicao[0]["nome"],
# 			"data_nascimento": requisicao[0]["data_nascimento"]

#     }

# 	try:
# 		usuarios[0][cpf] = novoUsuario
# 	except IndexError:
# 		usuarios.append({cpf:novoUsuario})
	

# 	salvarUsuario(usuarios)
	
# 	return ("Usuario cadastrado com sucesso!")

# @app.route('/user/<int:cpf>', methods=['GET'])
# def userBycpf(cpf):
# 	try:
# 		cpf = str(cpf)
# 		return jsonify(usuarios[0][cpf])
# 	except KeyError:
# 		return (f"Usuario com o cpf |{cpf}| nao foi encontrado.")
	


	
if __name__ == '__main__':
	app.run()
	
