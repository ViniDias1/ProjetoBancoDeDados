
import mysql.connector

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

def insertUsuario(dados):
    sqlComando = "INSERT INTO Usuario VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sqlComando,dados)
    conexao.commit()
    return

def execucao(userResp):
    # Consulta Tabela
    if (userResp == 1):
        retorno = consultaTabela('Usuario')
        for i in retorno:
            print(i)
        return 
    
    #Insert um usuario
    dados = []
    print("Informe: CPF, Nome, Sobrenome, Login, Senha, Rua, CEP, Numero, Bairro, Email, Idade")
    for i in range(11):
        info = input()
        dados.append(info)

    insertUsuario(dados)
    print("Usuario cadastrado com sucesso")
    return


while True:
    userResp = int(input("\nQual operacao voce deseja fazer?:\n1.SELECT\n2.INSERT\n3.Sair\n"))
    if (userResp == 3):
        break

    execucao(userResp)


cursor.close()
conexao.close()