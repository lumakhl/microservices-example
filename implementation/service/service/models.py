import datetime

from sqlalchemy import (
    DECIMAL, Column, DateTime, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Base(object):
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )


DeclarativeBase = declarative_base(cls=Base)


class Pessoa(DeclarativeBase):
    __tablename__ = "pessoa"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String(11))
    nome = Column(String(50))
    endereco = Column(String(150))


class Divida(DeclarativeBase):
    __tablename__ = "divida"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pessoa_id = Column(
        Integer,
        ForeignKey("pessoa.id", name="fk_pessoa"),
        nullable=False
    )
    pessoa = relationship(Pessoa, backref="pessoa")




    
