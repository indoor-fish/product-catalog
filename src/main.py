from fastapi import FastAPI
from src.routes import products, inventory, pricing

app = FastAPI(title="product-catalog", version="1.0.0")
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(inventory.router, prefix="/inventory", tags=["inventory"])
app.include_router(pricing.router, prefix="/products", tags=["pricing"])

@app.get("/health")
async def health():
    return {"status": "ok", "service": "product-catalog"}
