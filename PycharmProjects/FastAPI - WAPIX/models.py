from sqlalchemy import  create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

db = create_engine ('sqlite:///banco.db')

Base = declarative_base()

 class Usuario(Base):
        _tablename_ = 'usuarios'

        id = Column ('id', Integer, primary_key=True, autoincrement=True)
        nome = Column ('nome', String)
        email = Column ('email', String, nullable=False)
        senha = Column ('senha', String)
        ativo = Column ('ativo', Boolean)
        adm = Column ('adm', Boolean, default=False)

        def _Init_(self, nome, email, senha, ativo=True, adm=False):
            self.usuario = nome
            self.email = email
            self.senha = senha
            self.ativo = ativo
            self.adm = adm


 class Pedido(Base):
     _tablename_ = 'pedidos'

     id = Column ('id', Integer, primary_key=True, autoincrement=True)
     status = Column ('satus', String)
     usuario = Column ('usuário', ForeignKey('usuarios.id'))
     preco = Column ('preço', Float)
     #itens = ()

     def _init_(self, status='PENDENTE', usuario, preco=0, itens):
         self.status = status
         self.usuario = usuario
         self.preco = preco
         self.itens = itens

