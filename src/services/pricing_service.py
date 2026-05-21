from src.services.inventory_service import get_inventory

async def get_price(product_id: str, base_price: float, category: str, user_role: str = "CUSTOMER", order_total: float = 0.0) -> dict:
    """
    Applies all pricing rules and returns the final price with audit trail.
    """
    final_price = base_price
    rules_applied: list[str] = []

    inv = await get_inventory(product_id)
    available = inv["available"]

    # Business Rule: Inventory below 10 units triggers automatic price increase of 8%
    if available < 10:
        final_price *= 1.08
        rules_applied.append("scarcity_surcharge_8pct")

    # Business Rule: Products in 'clearance' category cannot have additional discount codes applied
    if category.lower() == "clearance":
        rules_applied.append("clearance_no_discount")
        return {
            "product_id": product_id,
            "base_price": base_price,
            "final_price": round(final_price, 2),
            "discount_applied": 0.0,
            "rules_applied": rules_applied,
        }

    # Business Rule: MERCHANT tier customers receive 15% discount on orders above $500
    if user_role == "MERCHANT" and order_total > 500:
        discount = final_price * 0.15
        final_price -= discount
        rules_applied.append("merchant_tier_15pct_discount")

    discount_applied = round(base_price - final_price, 2)
    return {
        "product_id": product_id,
        "base_price": base_price,
        "final_price": round(final_price, 2),
        "discount_applied": discount_applied,
        "rules_applied": rules_applied,
    }
