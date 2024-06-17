from sqlalchemy import Column, Integer, VARCHAR
import db


class Usuario(db.Base):
    __tablename__ = "tb_usuario"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    email = Column(VARCHAR(100), nullable=False)

    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email


db.Base.metadata.create_all(db.engine, tables=[Usuario.__table__])
