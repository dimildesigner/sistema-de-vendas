from flask import Flask, jsonify, request,Blueprint
from categoria_repository import CategoriaRepository
from cetegoria import Categoria
import categoria_repository

categoria_bp = Blueprint("cetegoria",__name__)


@categoria_bp.route("/ola", methods = ["GET"])        # funcao get (pegar,dar clientes ex), post (cadastrar informaçao), delete(remover inf), put (atualização total), patch (atualizar so um dado)
def ola():
    return "minha primeira API"

@categoria_bp.route("/clientes", methods = ["GET"])
def listar_clientes():
    dados = [{"nome":"Leandro"}, {"nome":"Maria"},{"nome":"Silvio"},{"nome":"Marta"}]
    return jsonify (dados)

@categoria_bp.route("/categorias", methods = {"GET"})
def listar_categorias():
    repo = CategoriaRepository()
    categorias_raw = repo.find_all()
   
    # Transforma a lista em dicionários estruturados
    dados = []
    for cat in categorias_raw:
        dados.append({
            "id": cat[0],
            "nome": cat[1],
            "descricao": cat[2]
        })
    return jsonify(dados)
   
    # 2ª maneira pra fazer é igual o 1ª
    #dados = [
        #{"id":"1","nome":"Eletrônicos","descrição":"Produtos eletrônicos como celulares, computadores, etc."},
        #{"id":"2","nome":"Roupas","descrição":"Vestuário masculino, feminino e infantil"},
        #{"id":"3","nome":"Móveis","descrição":"Móveis para casa e escritório"},
        #{"id":"4","nome":"Alimentos","descrição":"Produtos alimentícios e bebidas"},
            #]  
            #  
@categoria_bp.route("/categorias/<int:categoriaID>")
def buscar_por_id(categoriaID):   #mesmo nome na de cima
    repo = CategoriaRepository()
    categoria = repo.find_by_id(categoriaID)
    categoria_retorno = {"id":categoria[0], "nome":categoria[1],"descrição":categoria[2]}
    return jsonify(categoria_retorno)

@categoria_bp.route('/categorias', methods = ['POST'])
def cadastrar_categoria():
    repo = CategoriaRepository()

    dados_json = request.get_json()

    #pegando osdados recebidos do json
    id = dados_json.get("id")
    nome = dados_json.get("nome")
    descricao = dados_json.get("descricao")

    #enviando para o banco de dados
    repo.create(nome,descricao)

    return jsonify({"Mensagem":"Categoria cadastrada com sucesso.",
                    "nome":nome,
                    "descricao":descricao}),201


@categoria_bp.route("/categorias/<int:id_categoria>",methods = ['DELETE'])
def remover_categoria(id_categoria):
    #objeto de comunicação com banco de dados
    repo = CategoriaRepository()
    #removendo a categoria do banco de dados
    repo.delete(id_categoria)

    return jsonify({
        "mensagem":"Categoria removida com sucesso."
    })