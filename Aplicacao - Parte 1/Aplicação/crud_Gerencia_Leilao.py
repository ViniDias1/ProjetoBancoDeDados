from imports import *

@app.route('/create_Gerencia_Leilao/<int:cpf_admin>/<int:idLeilao>', methods=['POST'])
def create_Gerencia_Leilao(cpf_admin,idLeilao):

	cursor = conexao.cursor()
	
	dia = randint(1,30)
	mes = randint(1,12)
	hora_operacao = randint(7,19)
	minutos_operacao = randint(0,59)
	
	select_cargo = f"SELECT cargo FROM Administrador WHERE cpf_administrador = {cpf_admin}"
	cursor.execute(select_cargo)
	select_cargo = cursor.fetchone()
	
	sql = f"INSERT INTO Gerencia_Leilao VALUES (NULL,'{cpf_admin}',{idLeilao},'{cargos_funcao[select_cargo[0]]}','2023-{mes}-{dia} {hora_operacao}:{minutos_operacao}:00')"
	
	cursor.execute(sql)
	conexao.commit()
	cursor.close()
	return make_response("Cadastro Realizado!")

@app.route('/selectAll_Gerencia_Leilao', methods=['GET'])
def selectAll_Gerencia_Leilao():

	cursor = conexao.cursor()

	sql = "SELECT * FROM Gerencia_Leilao;"
	cursor.execute(sql)

	resposta = cursor.fetchall()
	cursor.close()
	leilao_gerenciado = []
	for row in resposta:
		leilao = {
                "idGerencia_Leilao": row[0],
                "cpf_admin": row[1],
                "idLeilao": row[2],
                "tipo_operacao": row[3],
                "data_horario_operacao": str(row[4])
        }
		leilao_gerenciado.append(leilao)
	
	return make_response(
		jsonify(
			dados=leilao_gerenciado
		)
	)

@app.route('/selectGerencia_Leilao/Admin/<int:cpf>', methods=['GET'])
def selectGerencia_Leilao_Admin(cpf):

	cursor = conexao.cursor()

	sql = f"SELECT * FROM Gerencia_Leilao WHERE idGerencia_Leilao = {cpf}"
	cursor.execute(sql)

	resposta = cursor.fetchall()
	cursor.close()
	return make_response(
		jsonify(
			dados = resposta
		)
	)

@app.route('/update_idLeilao_Gerencia_Leilao/<int:cpf_admin>/<int:idLeilao>', methods=['PUT'])
def update_idLeilao_Gerencia_Leilao(idLeilao,cpf_admin):

	cursor = conexao.cursor()

	sql = f"UPDATE Gerencia_Leilao SET idLeilao_gerencia = '{idLeilao}' WHERE Administrador_cpf_administrador = {cpf_admin}"
	cursor.execute(sql)

	conexao.commit()
	cursor.close()
	return make_response("Id do Leilao Alterado!")


@app.route('/delete_Gerencia_Leilao/<int:idLeilao>', methods=['DELETE'])
def delete_Gerencia_Leilao(idLeilao):

	cursor = conexao.cursor()

	sql = f"DELETE FROM Gerencia_Leilao WHERE idLeilao_gerencia = {idLeilao}"
	cursor.execute(sql)

	conexao.commit()
	cursor.close()
	return make_response("Deletado!")
