from app.models.bd import Connection

class Validacoes:
    def __init__(self):
        self.dominio = "http://127.0.0.1:5000/urls/"

    def short_url_existe(self, codigo):
        self.short_url = self.dominio+codigo
        self.bd = Connection()
        self.query = ("SELECT * FROM links WHERE shorturl = '{0}'".format(self.short_url))
        self.result = self.bd.findOne(self.query)
        if not self.result:
            return False
        return True

    def id_existe(self, id):
        self.bd = Connection()
        self.query = ("SELECT * FROM links WHERE id = {0}".format(id))
        self.result = self.bd.findOne(self.query)
        if not self.result:
            return False
        return True

    def http_existe_na_url(self,URL):
        if URL[:7] == 'http://' or URL[:8] == 'https://':
            return URL
        return 'http://'+URL

    def existem_dados(self):
        self.bd = Connection()
        self.query = "SELECT * FROM links"
        self.results = self.bd.findOne(self.query)
        if not self.results:
            return False
        return True



