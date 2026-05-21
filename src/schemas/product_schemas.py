from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductDTO(BaseModel):
    id: str
    name: str
    description: str
    category: str
    base_price: float
    stock_count: int
    sku: str

class InventoryDTO(BaseModel):
    product_id: str
    available: int
    reserved: int
    last_updated: datetime

class PricingRuleDTO(BaseModel):
    rule_id: str
    type: str
    discount: float
    conditions: dict
    active: bool

class CreateProductRequest(BaseModel):
    name: str
    description: str
    category: str
    base_price: float = Field(gt=0)
    stock_count: int = Field(ge=0)
    sku: str

class PriceResponse(BaseModel):
    product_id: str
    base_price: float
    final_price: float
    discount_applied: float
    rules_applied: list[str]

class ReserveInventoryRequest(BaseModel):
    quantity: int = Field(gt=0)
