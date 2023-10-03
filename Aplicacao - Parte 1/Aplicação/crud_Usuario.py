from imports import *

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

@app.route('/update_Senha_Usuario/<int:cpf>', methods=['PUT'])
def update_Senha_Usuario(cpf):

	cursor = conexao.cursor()

	sql = f"UPDATE Usuario SET senha = 'novaSENHA' WHERE cpf = {cpf}"
	cursor.execute(sql)

	conexao.commit()
	cursor.close()
	return make_response("Senha Alterada!")

@app.route('/delete_Usuario/<int:cpf>', methods=['DELETE'])
def delete_Usuario(cpf):

	cursor = conexao.cursor()

	sql = f"DELETE FROM Usuario WHERE cpf = {cpf}"
	cursor.execute(sql)

	conexao.commit()
	cursor.close()
	return make_response("Usuario deletado!")
