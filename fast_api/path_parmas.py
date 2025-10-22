from fastapi import APIRouter

router = APIRouter(prefix='/path_params', tags=['path_params'])

@router.get('/items/{item_id}')
async def read_item(item_id : int):
    return {'item_id' : item_id}

# 경로 작동은 순차적으로 실행
@router.get('/users/me')
async def read_user_me():
    return {'user_id' : 'current user == me'}

@router.get('/users/{user_id}')
async def read_user(user_id: str):
    return {'user_id' : user_id}
