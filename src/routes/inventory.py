from fastapi import APIRouter, HTTPException
from src.schemas.product_schemas import ReserveInventoryRequest
from src.services.inventory_service import get_inventory, reserve_inventory, InsufficientInventoryError

router = APIRouter()

@router.get("/{product_id}")
async def get_inventory_status(product_id: str):
    inv = await get_inventory(product_id)
    return {"inventory": inv}

@router.patch("/{product_id}/reserve")
async def reserve(product_id: str, req: ReserveInventoryRequest):
    try:
        await reserve_inventory(product_id, req.quantity)
        inv = await get_inventory(product_id)
        return {"inventory": inv}
    except InsufficientInventoryError as e:
        raise HTTPException(status_code=409, detail=str(e))
