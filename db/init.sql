CREATE TABLE IF NOT EXISTS patient (
    id SERIAL PRIMARY KEY,
    nhs_number VARCHAR(10) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    postcode VARCHAR(8) NOT NULL
);

CREATE INDEX ix_nhs_number on patient(nhs_number);