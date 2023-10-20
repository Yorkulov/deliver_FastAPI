from fastapi import APIRouter

order_router = APIRouter(
    prefix="/orders",
)

@order_router.get('/')
async def signup():
    return {"message": "Bu Order sahifasi"}