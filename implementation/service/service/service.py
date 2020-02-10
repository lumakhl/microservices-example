import uuid

from nameko.rpc import rpc
from nameko.events import EventDispatcher
from nameko_sqlalchemy import DatabaseSession
from nameko_redis import Redis

from service.exceptions import NotFound
from service.models import DeclarativeBase, Pessoa, Divida
from service.schemas import PessoaSchema, DividaSchema

class Service:
    name = 'service'

    db = DatabaseSession(DeclarativeBase)
    event_dispatcher = EventDispatcher()

    @rpc
    def get_pessoa(self, pessoa_id):
        pessoa = self.db.query(Pessoa)(pessoa_id)

        if not pessoa:
            raise Notfound('Pessoa com id {} não encontrada'.format(pessoa_id))
        
        return PessoaSchema().dump(pessoa)
    
    @rpc
    def create_pessoa(self, pessoa):
        p = Pessoa(
                    nome=pessoa['nome'],
                    endereco=pessoa['endereco'],
                    cpf=pessoa['cpf']
                )
           
        self.db.add(p)
        self.db.commit()

        p = PessoaSchema().dump(p)

        self.event_dispatcher('pessoa_criada', {
            'pessoa': p,
        })
      
        return pessoa


    @rpc
    def get_dividas(self, pessoa_id):
        dividas = self.db.query(Divida)(pessoa_id)

        if not dividas:
            raise Notfound('Dividas para pessoa com id {} não encontradas'.format(pessoa_id))
        
        return DividaSchema().dump(dividas)
    
    @rpc
    def create_divida(self, divida_nova):
        divida = Divida(
            pessoa_id=divida_nova['pessoa_id'],
        )

        self.db.add(divida)
        self.db.commit()

        divida = DividaSchema().dump(divida)

        self.event_dispatcher('divida_criada', {
            'divida': divida,
        })
      
        return divida