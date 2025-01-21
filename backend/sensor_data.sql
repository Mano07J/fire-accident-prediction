CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    temperature FLOAT,
    smoke FLOAT,
    humidity FLOAT,
    gas FLOAT,
    fire_risk BOOLEAN,
    created_at TIMESTAMP DEFAULT NOW()
);
