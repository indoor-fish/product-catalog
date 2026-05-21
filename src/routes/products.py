from fastapi import APIRouter, HTTPException
from src.schemas.product_schemas import CreateProductRequest
from src.services import product_service

router = APIRouter()

@router.get("/")
async def list_products():
    products = await product_service.list_products()
    return {"products": products}

@router.get("/{product_id}")
async def get_product(product_id: str):
    product = await product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    return {"product": product}

@router.post("/")
async def create_product(req: CreateProductRequest):
    product = await product_service.create_product(req.model_dump())
    return {"product": product}

@router.put("/{product_id}")
async def update_product(product_id: str, updates: dict):
    product = await product_service.update_product(product_id, updates)
    if not product:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    return {"product": product}
