
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
    idade = randint(1,100)
    numero = randint(1,500)
    
    dados = [
        pk_cpf,
        'nomeTeste',
        'sobrenomeTeste',
        'loginTeste',
        'senhaTeste',
        'ruaTeste',
        'cepTeste',
        numero,
        'bairroTeste',
        'emailTeste@gmail', 
        idade
    ]
        
    try:
        sqlComando = "INSERT INTO Usuario VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sqlComando,dados)
        conexao.commit()
        print(f"Usuario com CPF |{pk_cpf}| inserido com sucesso!\n\n")
        return
    except mysql.connector.errors.IntegrityError:
        print(f"CPF |{pk_cpf}| já cadastrado. Tente novamente!\n\n")
        return

insertUsuario()
for linha in consultaTabela("Usuario"):
    print(linha)

cursor.close()
conexao.close()
