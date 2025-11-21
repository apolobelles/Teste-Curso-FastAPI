from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth', tags=['autenticação'])

@auth_router.get('/')
async def autenticar():
    '''
Essa é a rota de autenticação padrão do nosso sistema
    '''
    return{'mensagem': 'parabens voce acessou as autenticações', 'autenticado': False}