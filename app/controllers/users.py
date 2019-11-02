from app.models.bd import Connection


class Users():

    def cadastrarUser(self, id):
        try:
            self.bd = Connection()
            self.query = ("INSERT INTO users (usuario) VALUES ('{0}')".format(id))
            self.bd.executarSQL(self.query)
        except:
            print('Erro ao cadastrar usuario')
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

    def deletarUser(self, id):
        try:
            self.bd = Connection()
            self.query = ("DELETE FROM users WHERE id_usuario = ('{0}')".format(id))
            self.bd.executarSQL(self.query)
        except:
            print('Erro ao cadastrar usuario')
        finally:
            self.bd.cursor.close()
            self.bd.connection.close()

