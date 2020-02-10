import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http

class GatewayService:
    name = 'gateway'
    
    service_rpc = RpcProxy('service')

    @http('GET', '/pessoa/<string:pessoa_id>')
    def get_pessoa(self, request, airport_id):
        pessoa = self.service_rpc.get_pessoa(pessoa_id)
        return json.dumps({'pessoa': pessoa})
    
    @http('POST', '/pessoa')
    def post_pessoa(self, request):
        data = json.load(request.get_data(as_text=True))
        pessoa = self.service_rpc.create_pessoa(data['pessoa'])

        return pessoa

    @http('GET', '/divida/<string:pessoa_id>')
    def get_divida(self, request, pessoa_id):
        dividas = self.service_rpc.get_divida(pessoa_id)
        return json.dumps({'dividas': dividas})

    @http('POST', '/divida')
    def post_divida(self, request):
        data = json.loads(request.get_data(as_text=True))
        divida = self.service_rpc.create_divida(data['divida'])

        return divida

