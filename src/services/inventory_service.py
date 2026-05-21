from datetime import datetime, timezone

# In-memory store; replace with DB in production
_inventory: dict[str, dict] = {}

class InsufficientInventoryError(Exception):
    pass

async def get_inventory(product_id: str) -> dict:
    if product_id not in _inventory:
        _inventory[product_id] = {"product_id": product_id, "available": 100, "reserved": 0, "last_updated": datetime.now(timezone.utc)}
    return _inventory[product_id]

async def reserve_inventory(product_id: str, quantity: int) -> None:
    """
    Atomically reserves inventory when an order is placed.
    Raises InsufficientInventoryError if available stock < requested quantity.
    """
    inv = await get_inventory(product_id)
    if inv["available"] < quantity:
        raise InsufficientInventoryError(
            f"Insufficient inventory for product {product_id}: requested {quantity}, available {inv['available']}"
        )
    inv["available"] -= quantity
    inv["reserved"] += quantity
    inv["last_updated"] = datetime.now(timezone.utc)

async def release_inventory(product_id: str, quantity: int) -> None:
    """Releases previously reserved inventory (e.g. on order cancellation)."""
    inv = await get_inventory(product_id)
    inv["reserved"] = max(0, inv["reserved"] - quantity)
    inv["available"] += quantity
    inv["last_updated"] = datetime.now(timezone.utc)

async def update_stock(product_id: str, delta: int) -> None:
    inv = await get_inventory(product_id)
    inv["available"] = max(0, inv["available"] + delta)
    inv["last_updated"] = datetime.now(timezone.utc)
