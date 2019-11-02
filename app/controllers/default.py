from http import HTTPStatus

from flask import request, jsonify
from werkzeug.utils import redirect

from app.controllers.links import Links
from app.controllers.utils import Utils
from app.controllers.validacoes import Validacoes
from app import app
from app.controllers.users import *


@app.route("/urls", methods=["POST"])
def encurtarURL():
    data = request.json
    short = Links()
    data = short.cadastra_urls(data["URL"])
    utils = Utils()
    data = utils.gera_dict(data)
    return jsonify(data), HTTPStatus.CREATED


@app.route("/urls/<codigo>", methods=["GET"])
def redireciona(codigo):
    garanta = Validacoes()

    if not garanta.short_url_existe(codigo):
        return '', HTTPStatus.NOT_FOUND

    link = Links()
    link.registra_hits(codigo)
    url_original = link.find_url_original(codigo)

    return redirect(url_original[0][0], HTTPStatus.MOVED_PERMANENTLY)


@app.route("/stats/<id>", methods=["GET"])
def stats_id(id):
    garanta = Validacoes()
    if not garanta.id_existe(id):
        return '', HTTPStatus.NOT_FOUND

    url = Links()
    results = url.get_stats_by_id(id)
    utils = Utils()
    results = utils.gera_dict(results)
    return jsonify(results)


@app.route("/stats", methods=['GET'])
def stats():
    garanta = Validacoes()
    results = garanta.existem_dados()
    if not results:
        return 'No Data', HTTPStatus.NOT_FOUND

    links = Links()
    stats_geral = links.get_analitcs()
    return jsonify(stats_geral)


@app.route("/urls/<id>", methods=["DELETE"])
def delete(id):
    garanta = Validacoes()
    results = garanta.id_existe(id)
    if not results:
        return '', HTTPStatus.NOT_FOUND
    link = Links()
    link.delete_url(id)
    return '', HTTPStatus.OK


@app.route("/users", methods=["POST"])
def cadastrarUser():
    garanta = Validacoes()
    data = request.json
    if not garanta.user_existe(user=data['id']):
        return '', HTTPStatus.CONFLICT

    user = Users()
    user.cadastrarUser(data['id'])
    return jsonify(data), HTTPStatus.CREATED


@app.route("/users/<id>", methods=['DELETE'])
def deletarUser(id):
    garanta = Validacoes()
    if garanta.user_existe(id=id):
        return 'User não existe', HTTPStatus.NOT_FOUND

    user = Users()
    user.deletarUser(id)
    return '', HTTPStatus.OK




