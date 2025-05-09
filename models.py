from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import scoped_session,sessionmaker,relationship,declarative_base

engine = create_engine('sqlite:///base.sqlite3')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Livro(Base):
    __tablename__ = 'TAB_LIVROS'
    id_livro = Column(Integer, primary_key=True)
    titulo = Column(nullable=False, index=True)
    autor = Column(nullable=False, index=True)
    categoria = Column(nullable=False, index=True)
    descricao = Column(nullable=False, index=True)

    def __repr__(self):
        return 'Livro: {} {} {} {}'.format( self.titulo, self.autor, self.categoria,self.descricao)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def __delete__(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_livro(self):
        dados_livro = {
            'id_livro': self.id_livro,
            'titulo': self.titulo,
            'autor': self.autor,
            'categoria': self.categoria,
            'descricao': self.descricao,
        }
        return dados_livro

class Usuario(Base):
    __tablename__ = 'TAB_USUARIOS'
    id_usuario = Column(Integer, primary_key=True)
    nome = Column(nullable=False, index=True)
    profissao = Column(nullable=False, index=True)
    salario = Column(nullable=False, index=True)

    def __repr__(self):
        return 'Usuario: {} {} {}'.format( self.nome, self.profissao, self.salario)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def __delete__(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_usuario(self):
        dados_usuario = {
            'id_usuario': self.id_usuario,
            'nome': self.nome,
            'profissao': self.profissao,
            'salario': self.salario,
        }
        return dados_usuario

def init_db():
    Base.metadata.create_all(engine)
if __name__ == '__main__':
    init_db()

