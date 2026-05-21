from fastapi import APIRouter, HTTPException, Query
from src.services.pricing_service import get_price
from src.services.product_service import get_product

router = APIRouter()

@router.get("/{product_id}/price")
async def get_product_price(
    product_id: str,
    user_role: str = Query(default="CUSTOMER"),
    order_total: float = Query(default=0.0),
):
    product = await get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    result = await get_price(product_id, product["base_price"], product["category"], user_role, order_total)
    return result
