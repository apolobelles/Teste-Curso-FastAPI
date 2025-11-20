from fastapi import APIRouter
from pygments.styles.rainbow_dash import RainbowDashStyle

order_router = APIRouter(prefix='/order', tags=['requisição'])

@order_router.get('/')
async def pedidos():
     return{'mensagem': 'Você acessou as rotas'}