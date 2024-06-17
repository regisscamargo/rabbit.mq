import json
from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession
from ModelUsuario import Usuario, db


class ServiceUsuario:
    name = "service_usuario"
    db = DatabaseSession(db.Base)

    @rpc
    def AddUser(self, event):
        try:
            aux = json.dumps(event)
            dados = json.loads(aux)
            user = Usuario(None, dados["nome"], dados["email"])
            self.db.add(user)
            self.db.commit()
            return {
                "id": user.id,
                "nome": user.nome,
                "email": user.email,
                "msg": "insert ok",
            }
        except Exception as e:
            self.db.rollback()
            return {"erro": str(e)}
        finally:
            self.db.close()

    @rpc
    def GetUser(self, event):
        try:
            aux = json.dumps(event)
            dados = json.loads(aux)
            user = self.db.query(Usuario).filter(Usuario.id == dados["id"]).one()
            return {
                "id": user.id,
                "nome": user.nome,
                "email": user.email,
                "msg": "get ok",
            }
        except Exception as e:
            return {"erro": str(e)}
        finally:
            self.db.close()

    @rpc
    def UpdateUser(self, event):
        try:
            aux = json.dumps(event)
            dados = json.loads(aux)
            user = self.db.query(Usuario).filter(Usuario.id == dados["id"]).one()
            user.nome = dados["nome"]
            user.email = dados["email"]
            self.db.add(user)
            self.db.commit()
            return {
                "id": user.id,
                "nome": user.nome,
                "email": user.email,
                "msg": "update ok",
            }
        except Exception as e:
            self.db.rollback()
            return {"erro": str(e)}, 400
        finally:
            self.db.close()

    @rpc
    def DeleteUser(self, event):
        try:
            aux = json.dumps(event)
            dados = json.loads(aux)
            user = self.db.query(Usuario).filter(Usuario.id == dados["id"]).one()
            self.db.delete(user)
            self.db.commit()
            return {
                "id": user.id,
                "nome": user.nome,
                "email": user.email,
                "msg": "delete ok",
            }
        except Exception as e:
            self.db.rollback()
            return {"erro": str(e)}, 400
        finally:
            self.db.close()
