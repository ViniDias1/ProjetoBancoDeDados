
from imports import *

@app.route('/create_Usuario/Admin/<int:cpf>', methods=['POST'])
def create_Usuario_Admin(cpf):

	random_cargo = randint(0,4)
	cursor = conexao.cursor()

	sql = f"INSERT INTO Administrador VALUES ({cpf},'{cargos[random_cargo]}')"
	cursor.execute(sql)

	conexao.commit()
	cursor.close()
	return make_response("Usuario Cadastrado!")

@app.route('/selectAll_Usuario/Admin', methods=['GET'])
def selectAll_Usuario_Admin():

	cursor = conexao.cursor()

	sql = "SELECT * FROM Administrador"
	cursor.execute(sql)

	resposta = cursor.fetchall()
	cursor.close()
	return make_response(
		jsonify(
			dados = resposta
		)
	)

@app.route('/selectUsuario_cpf/Admin/<int:cpf>', methods=['GET'])
def selectUsuario_cpf_Admin(cpf):

	cursor = conexao.cursor()

	sql = f"SELECT * FROM Administrador WHERE cpf_administrador = {cpf}"
	cursor.execute(sql)

	resposta = cursor.fetchall()
	cursor.close()
	return make_response(
		jsonify(
			dados = resposta
		)
	)

#UPDATE 
@app.route('/update_Cargo_Usuario/Admin/<int:cpf>', methods=['PUT'])
def update_Cargo_Usuario_Admin(cpf):

	cursor = conexao.cursor()

	select_cargo_alterar = f"SELECT cargo FROM Administrador WHERE cpf_administrador = {cpf}"
	cursor.execute(select_cargo_alterar)
	cargo_alterar = cursor.fetchall()
	novo_cargo = cargos[randint(0,4)]

	while True:
		if novo_cargo == cargo_alterar:
			novo_cargo = cargos[randint(0,4)]
		else:
			break

	sql = f"UPDATE Administrador SET cargo = '{novo_cargo}' WHERE cpf_administrador = {cpf}"
	cursor.execute(sql)

	conexao.commit()
	cursor.close()
	return make_response("Cargo Alterado!")


@app.route('/delete_Usuario/Admin/<int:cpf>', methods=['DELETE'])
def delete_Usuario_Admin(cpf):

	cursor = conexao.cursor()

	sql = f"DELETE FROM Administrador WHERE cpf_administrador = {cpf}"
	cursor.execute(sql)

	conexao.commit()
	cursor.close()
	return make_response("Usuario deletado!")

