from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix='/request_body', tags=['request_body'])

class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None
    
@router.post('/items')
async def create_item(item: Item):
    return item

@router.put('/items/{item_id}')
async def update_item(item_id : int, item : Item, q : str | None = None):
    result = {"item_id" : item_id, **item.model_dump()}
    if q:
        result.update({"q" : q})
    return result