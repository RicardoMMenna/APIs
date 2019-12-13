# -*- coding: UTF-8 -*-

# python -m pip install flask

from flask import Flask, request
from pprint import pprint
from pymongo import MongoClient
from produto import Produto
from db_api import DB_API

import json

app = Flask(__name__)

@app.route('/itens', methods=['GET'])
def getData():
    result = api.findAll()
    newResult = []
    for prod in result:
        item = api.convJsonToProduto(prod)
        newResult.append(api.convProdutoToJson(item))
    return json.dumps(newResult)

@app.route('/itens', methods=['POST'])
def createData():
    # le a requisicao json
    req_data = request.get_json()

    # Converte o Json em um Produto
    prod = api.convJsonToProduto(req_data)

    # cria o novo registro no banco de dados
    result = api.create(prod)
    result = api.convProdutoToJson(result)
    return json.dumps(result)

@app.route('/itens', methods=['PUT'])
def updateData():
    # le a requisicao json
    req_data = request.get_json()

    # Converte o Json em um Produto
    prod = api.convJsonToProduto(req_data)

    # Altera o registro desejado no banco de dados
    result = api.update(prod)
    result = { 'result': result }
    return json.dumps(result)

@app.route('/itens/<cod>', methods=['DELETE'])
def deleteData(cod):
    item = api.delete(cod)
    result = { 'result': item }
    return json.dumps(result)

@app.route('/zera', methods=['PURGE'])
def wipeData():
    item = api.zera()
    result = { 'result': item }
    return json.dumps(result)

@app.route('/')
def default():
     return getData()

app.debug = True

api = DB_API()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=54321)
