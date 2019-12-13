# -*- coding: UTF-8 -*-

import json

from produto import Produto
from pymongo import MongoClient

mongoDBUrl = 'mongodb://localhost'

class DB_API(object):
    def __init__(self):
        self.cData = ""
        self.client = MongoClient(mongoDBUrl)
        self.db = self.client.testeapi
        self.table = self.db.produtos

    def find(self, pCod):
        # le um registro do banco de dados
        return self.table.find_one({'codigo': pCod})

    def findAll(self):
        # le todos os registros do banco de dados
        return self.table.find()

    def findLast(self):
        # le o ultimo registro do banco de dados
        return self.table.find_one({'$query': {}, '$orderby': {'$natural': -1}})

    def findFirst(self):
        # le o ultimo registro do banco de dados
        return self.table.find_one({'$query': {}, '$orderby': {'$natural': 1}})

    def exist(self, pCod):
        # verifica se existe o registro no banco de dados
        result = self.find(pCod)
        return result != None

    def create(self, prod):
        # cria um novo um registro do banco de dados
        cJson = self.convProdutoToJson(prod)
        self.table.insert(cJson)
        return prod

    def update(self, prod):
        if self.exist(prod.codigo):
            result = self.find(prod.codigo)
            cJsonProd = self.convProdutoToJson(prod)
            self.table.update_one({'_id': result.get('_id')}, {'$set': cJsonProd})
            return True
        return False

    def delete(self, pCod):
        if self.exist(pCod):
            result = self.find(pCod)
            self.table.remove({'_id': result.get('_id')})
            return True
        return False

    def total(self):
        # le o total de registros do banco de dados
        return self.table.count()

    def zera(self):
        # zera o conteudo da tabela no banco de dados
        self.table.remove()
        return True

    def convJsonToProduto(self, cJson):
        # cria o Produto com base nas informacoes do JSon
        prod = Produto(cJson['codigo'], cJson['descricao'],
                       cJson['unidade'], cJson['valor'],
                       cJson['quantidade'])
        return prod

    def convProdutoToJson(self, prod):
        # cria um json com base no Produto
        cJson = {"codigo": prod.codigo, "descricao": prod.descricao,
                 "unidade": prod.unidade, "valor": prod.valor,
                 "quantidade": prod.quantidade}
        return cJson
