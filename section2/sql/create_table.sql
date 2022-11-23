BEGIN;

CREATE TABLE IF NOT EXISTS Product (
	product_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	product_name VARCHAR(50),
    manufacturer_name VARCHAR(50),
    cost_dollars FLOAT NOT NULL,
    weight_kg FLOAT NOT NULL,
    CHECK (cost_dollars > 0),
    CHECK (weight_kg > 0)
);

CREATE TABLE IF NOT EXISTS Member (
	member_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    date_of_birth VARCHAR(8),
    mobile_no INT,
    above_18 BOOLEAN
);

CREATE TABLE IF NOT EXISTS Transactions (
    ts TIMESTAMP GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	member_id INT NOT NULL REFERENCES Member(member_id),
	product_id INT NOT NULL REFERENCES Product(product_id),
    cost_dollars_per_qty FLOAT NOT NULL REFERENCES Product(cost_dollars),
    weight_kg FLOAT NOT NULL REFERENCES Product(weight_kg),
    quantity_purchased INT NOT NULL,
    CHECK (ts <= NOW()),
    UNIQUE(member_id, product_id)
);

END;