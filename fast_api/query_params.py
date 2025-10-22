from fastapi import APIRouter

router = APIRouter(prefix='/query_params', tags=['query_params'])

fake_item_db = [
    {"item_name" : "김밥"},
    {"item_name" : "떡볶이"},
    {"item_name" : "순대"},
    {"item_name" : "어묵"},
    {"item_name" : "튀김"},
]

@router.get('/items')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_item_db[skip : skip + limit]

@router.get('/products/{product_id}')
async def read_product(product_id: str, q: str | int = None):
    if q:
        return {'product_id' : product_id, 'q' : q}
    return {'product_id' : product_id}