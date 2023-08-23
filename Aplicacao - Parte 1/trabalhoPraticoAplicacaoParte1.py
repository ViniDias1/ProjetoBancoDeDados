
import mysql.connector
from random import randint

conexao = mysql.connector.connect(
    host = "viniemarcelodb-mysql.cor5ekoknnbw.us-east-1.rds.amazonaws.com",
    user = "professor",
    password = "Professor123.",
    database = "mydb"
)

cursor = conexao.cursor()


def consultaTabela(tabela):
    sqlComando = f"SELECT * FROM {tabela}"
    cursor.execute(sqlComando)
    resultado = cursor.fetchall()
    return resultado

def insertUsuario():
    pk_cpf = str(randint(1,1000))
    idade = str(randint(1,100))
    

    dados = (
        pk_cpf,
        'nomeTeste',
        'sobrenomeTeste',
        'loginTeste',
        'senhaTeste',
        'ruaTeste',
        'cepTeste',
        'numeroTeste',
        'bairroTeste',
        'emailTeste@gmail', 
        idade
    )

    sqlComando = "INSERT INTO Usuario VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"


    try:
        cursor.execute(sqlComando,dados)
        conexao.commit()
        print(f"Usuario com cpf {dados[0]} inserido com sucesso!\n\n")
        return
    except mysql.connector.errors.IntegrityError:
        print("CPF já cadastrado. Tente novamente!\n\n")
        return


insertUsuario()
for i in consultaTabela("Usuario"):
    print(i)


cursor.close()
conexao.close()
