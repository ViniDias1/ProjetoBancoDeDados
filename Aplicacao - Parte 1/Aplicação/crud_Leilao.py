
from imports import *

@app.route('/create_Leilao', methods=['POST'])
def create_Leilao():
	cursor = conexao.cursor()
	organizador = randint(1,20)
	dia = randint(1,30)
	mes = randint(1,12)
	horario_inicio = randint(12,15)

	sql = f"INSERT INTO Leilao VALUES (NULL,'2023-{mes}-{dia}','{horario_inicio}:00','{horario_inicio+3}:00',1,'organizador{organizador}')"
	cursor.execute(sql)

	conexao.commit()
	cursor.close()
	return make_response("Cadastro Realizado!")

@app.route('/selectAll_Leilao', methods=['GET'])
def selectAll_Leilao():
	cursor = conexao.cursor()
	sql = "SELECT * FROM Leilao;"
	cursor.execute(sql)
	resposta = cursor.fetchall()
	cursor.close()
	leiloes = []
	for row in resposta:
		leilao = {
                "id": row[0],
                "data": row[1],
                "horario_inicio": str(row[2]),
                "horario_fim": str(row[3]),
                "status": row[4],
                "organizador": row[5]
        }
		leiloes.append(leilao)
	
	return make_response(
		jsonify(
			dados=leiloes
		)
	)

@app.route('/select_Leilao/<int:idLeilao>', methods=['GET'])
def select_Leilao_id(idLeilao):
	cursor = conexao.cursor()
	sql = f"SELECT * FROM Leilao WHERE idLeilao = {idLeilao};"
	cursor.execute(sql)
	resposta = cursor.fetchall()
	cursor.close()
	leiloes = []
	for row in resposta:
		leilao = {
                "id": row[0],
                "data": row[1],
                "horario_inicio": str(row[2]),
                "horario_fim": str(row[3]),
                "quantidade_lotes": row[4],
                "organizador": row[5]
        }
		leiloes.append(leilao)
	
	return make_response(
		jsonify(
			dados=leiloes
		)
	)


@app.route('/update_Quant_Lotes/<int:idLeilao>', methods=['PUT'])
def update_Quant_Lotes_id(idLeilao):

	# VERIFICAR SE O CARGO MUDOU 
	quantidade_lotes = randint(1,30)
	cursor = conexao.cursor()
	sql = f"UPDATE Leilao SET quantidade_lotes = '{quantidade_lotes}' WHERE idLeilao = {idLeilao}"
	cursor.execute(sql)
	conexao.commit()
	cursor.close()
	return make_response("Quantidade de Lotes Alterado !")


@app.route('/delete_Leilao/<int:idLeilao>', methods=['DELETE'])
def delete_Leilao_id(idLeilao):
	cursor = conexao.cursor()
	sql = f"DELETE FROM Leilao WHERE idLeilao = {idLeilao}"
	cursor.execute(sql)
	conexao.commit()
	cursor.close()
	return make_response("Leilao deletado!")     
