import uuid
from datetime import datetime, timezone

_products: dict[str, dict] = {
    "prod-001": {"id": "prod-001", "name": "Widget Pro", "description": "High-quality widget", "category": "electronics", "base_price": 299.99, "stock_count": 50, "sku": "WGT-001"},
    "prod-002": {"id": "prod-002", "name": "Clearance Gadget", "description": "Discounted gadget", "category": "clearance", "base_price": 49.99, "stock_count": 5, "sku": "CLR-002"},
}

async def get_product(product_id: str) -> dict | None:
    return _products.get(product_id)

async def list_products() -> list[dict]:
    return list(_products.values())

async def create_product(data: dict) -> dict:
    product_id = str(uuid.uuid4())
    product = {"id": product_id, **data}
    _products[product_id] = product
    return product

async def update_product(product_id: str, updates: dict) -> dict | None:
    product = _products.get(product_id)
    if not product:
        return None
    product.update(updates)
    return product
