CREATE TABLE IF NOT EXISTS Product (
	product_id INT UNIQUE PRIMARY KEY,
	product_name VARCHAR(50),
    manufacturer_name VARCHAR(50),
    cost_dollars FLOAT NOT NULL,
    weight_kg FLOAT NOT NULL,
    CHECK (cost_dollars > 0),
    CHECK (weight_kg > 0)
);

CREATE TABLE IF NOT EXISTS Member (
	member_id INT UNIQUE PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    date_of_birth VARCHAR(8),
    mobile_no INT,
    above_18 BOOLEAN
);

CREATE TABLE IF NOT EXISTS Transactions (
    ts INT UNIQUE PRIMARY KEY,
	member_id INT NOT NULL REFERENCES Member(member_id),
	product_id INT NOT NULL REFERENCES Product(product_id),
    quantity_purchased INT NOT NULL,
    UNIQUE(member_id, product_id)
);
