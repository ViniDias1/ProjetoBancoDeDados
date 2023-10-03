from imports import *

@app.route('/transacao', methods=['GET','POST'])
def transacao():
    
    cursor = conexao.cursor()
    
    cursor.execute("SET @@autocommit = OFF;")
    cursor.execute("START TRANSACTION;")
    cursor.execute("DELETE FROM Gerencia_Leilao;")

    try:
        cursor.execute("INSERT INTO Gerencia_Leilao VALUES (NULL,'010',2,'ERRO','2023-01-01 00:00:00')")
    except Exception:
        cursor.execute("ROLLBACK;")

    try:
        cursor.execute("INSERT INTO Gerencia_Leilao VALUES (NULL,'164',17,'OPERACAO DE TRANSACAO',NOW())")
    except Exception:
        cursor.execute("ROLLBACK;")


    cursor.execute("SELECT * FROM Gerencia_Leilao;")

    resposta = cursor.fetchall()
    cursor.execute("SET @@autocommit = ON;")
    cursor.close()
    
    return make_response(
		jsonify(
			dados = resposta
		)
	)