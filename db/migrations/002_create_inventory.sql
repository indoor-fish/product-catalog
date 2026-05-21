CREATE TABLE inventory (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  product_id UUID REFERENCES products(id) UNIQUE,
  available INT NOT NULL DEFAULT 0,
  reserved INT NOT NULL DEFAULT 0,
  last_updated TIMESTAMPTZ DEFAULT now()
);
