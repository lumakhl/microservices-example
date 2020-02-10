from marshmallow import Schema, fields


class PessoaSchema(Schema):
    id = fields.Int(required=True)
    cpf= fields.Str(required=True)
    nome= fields.Str(required=True)        
    endereco= fields.Str(required=True)

class DividaSchema(Schema):
    id = fields.Int(required=True)
    pessoa = fields.Nested(PessoaSchema, many=True)