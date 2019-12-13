# -*- coding: UTF-8 -*-

from endpoints import Controller
from endpoints.decorators import version, param, post_param

from produto import Produto
from db_api import DB_API

import json

api = DB_API()

class Itens(Controller):
  def GET(self):
    result = api.findAll()
    newResult = []
    for prod in result:
        item = api.convJsonToProduto(prod)
        newResult.append(api.convProdutoToJson(item))
    return newResult

  def POST(self, codigo, descricao, unidade, valor, quantidade):
      # cria um novo produto
      prod = Produto(codigo, descricao, unidade, valor, quantidade)

      # cria o novo registro no banco de dados
      result = api.create(prod)
      result = api.convProdutoToJson(result)
      return result

  def PUT(self, codigo, descricao, unidade, valor, quantidade):
    # cria uma nova instancia do produto
    prod = Produto(codigo, descricao, unidade, valor, quantidade)

    # Altera o registro desejado no banco de dados
    result = api.update(prod)
    result = { 'result': result }
    return result

  def DELETE(self, codigo):
    item = api.delete(codigo)
    result = { 'result': item }
    return result

  def PURGE(self):
    item = api.zera()
    result = { 'result': item }
    return result
