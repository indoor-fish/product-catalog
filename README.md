# product-catalog

Product listings, inventory management, and pricing rule engine.

## Port: 3003

## API Endpoints
- `GET /products` — list all products
- `GET /products/:id` — get product details
- `POST /products` — create product
- `PUT /products/:id` — update product
- `GET /inventory/:productId` — check inventory
- `PATCH /inventory/:productId/reserve` — reserve inventory for an order
- `GET /products/:id/price?user_role=MERCHANT&order_total=600` — get price with rules applied

## Dependencies
- None (leaf node for product data)

See `BUSINESS_RULES.md` for pricing and inventory rules.
# accuracy test trigger
# reindex
