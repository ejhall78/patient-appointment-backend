CREATE TABLE IF NOT EXISTS patient (
    id SERIAL PRIMARY KEY,
    nhs_number VARCHAR(10) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    postcode VARCHAR(8) NOT NULL
);

-- INSERT INTO patient (nhs_number, name, date_of_birth, postcode)
-- VALUES ('1373645350', 'Dr Glenn Clark', '1996-02-01', 'N6 2FA');