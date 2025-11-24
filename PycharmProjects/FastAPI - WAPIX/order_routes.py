from fastapi import APIRouter

order_router = APIRouter(prefix='/order', tags=['requisição'])

@order_router.get('/')
async def pedidos():
     return{'mensagem': 'Você acessou as rotas'}