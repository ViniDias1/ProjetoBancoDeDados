from flask import Flask, jsonify, make_response, request
import json
import mysql.connector
from random import randint

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

conexao = mysql.connector.connect(
    host = "viniemarcelodb-mysql.cor5ekoknnbw.us-east-1.rds.amazonaws.com",
    user = "professor",
    password = "Professor123.",
    database = "mydb"
)
cargos = ['estagiario','supervisor','gestor','gerente','fiscal']

cargos_funcao = {
    'estagiario':'alterou quantidade de lotes',
    'supervisor': 'Autorizou Leilão',
    'gestor': 'Autorizou Lotes',
    'gerente': 'Coordenou Leilão',
    'fiscal': 'Fiscalizou os Lotes'
}

