import random
import string

from app.controllers.utils import Utils
from app.models.bd import Connection
from app.controllers.validacoes import Validacoes


class Links:

    def __init__(self):
        self.dominio = "http://127.0.0.1:5000/urls/"


    def cadastra_urls(self, URL):
        self.shorturl = Links.gerar_codigo(self)
        self.garanta = Validacoes()
        URL = self.garanta.http_existe_na_url(URL)

        try:
            self.bd = Connection()
            self.query = ("INSERT INTO links (hits, url, shorturl) VALUES ({0}, '{1}', '{2}')".format(0 , URL, self.shorturl))
            self.bd.executarSQL(self.query)
            return self.bd.findOne("SELECT * FROM links WHERE shorturl = '{0}'".format(self.shorturl))
        except:
            print("Erro ao inserir as URLs no banco!")
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()


    def gerar_codigo(self):
        try:
            self.bd = Connection()
            self.caracteres = string.digits + string.ascii_letters
            self.shorturl = self.dominio+''.join(random.choices(self.caracteres, k=4))
            self.verifica_url_existe = self.bd.findOne("SELECT * FROM links WHERE shorturl = '{0}'".format(self.shorturl))

            if self.verifica_url_existe:
                Links.gerar_codigo(self)
            return self.shorturl

        except:
            print("Erro ao verificar as codigos no banco!")
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()


    def find_url_original(self, codigo):
        try:
            self.bd = Connection()
            self.urlOriginal = self.bd.findOne("SELECT url FROM links WHERE shorturl = '{0}'".format(self.dominio + codigo))
            return self.urlOriginal
        except:
            print("Erro ao pesquisar a URL original!")
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

    def registra_hits(self, codigo):
        try:
            self.bd = Connection()
            self.bd.executarSQL("UPDATE links SET HITS = ((SELECT HITS FROM LINKS WHERE shorturl = '{0}') + 1) WHERE shorturl = '{1}'".format(self.dominio + codigo, self.dominio + codigo))

        except:
            print("Erro ao incrementar hit!")
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

    def get_stats_by_id(self, id):
        try:
            self.bd = Connection()
            self.query = ("SELECT * FROM links WHERE id = {0}".format(id))
            self.results = self.bd.findOne(self.query)

            if not self.results:
                return False
            return self.results
        except:
            print("Erro no get stats")
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

    def get_stats_all(self):
        try:
            self.bd = Connection()
            self.query = ("SELECT * FROM links".format(id))
            self.results = self.bd.findOne(self.query)
            return self.results

        except:
            print("Erro no get stats")
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

    def delete_url(self, id):
        try:
            self.bd = Connection()
            self.query = ("DELETE FROM links WHERE id = {0}".format(id))
            self.bd.executarSQL(self.query)
        except:
            print("Erro no deletar registro")
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

    def get_analitcs(self):
        try:
            self.bd = Connection()
            self.query = "select sum(hits), count(url) from links"
            self.hits_count = self.bd.findOne("select sum(hits), count(url) from links")
            self.query = "select * from links order by hits desc fetch first 10 rows only"
            self.top_hits = self.bd.findOne(self.query)

            utils = Utils()
            self.top_hits = utils.gera_dict(self.top_hits)

            self.results = {"urlCount": self.hits_count[0][1],
                            "hits": self.hits_count[0][0],
                            "topurls": self.top_hits}


            return self.results
        except:
            print("Erro ao gerar estatisticas do sistema")
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()
