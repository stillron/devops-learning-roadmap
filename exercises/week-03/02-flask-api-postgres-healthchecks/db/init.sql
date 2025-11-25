CREATE TYPE status_enum AS ENUM ('running', 'stopped');

CREATE TABLE IF NOT EXISTS containers (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    image TEXT NOT NULL,
    ports INTEGER[] NOT NULL,
    status status_enum NOT NULL
);

INSERT INTO containers (name, image, ports, status) VALUES
    ( 'nginx-1', 'nginx:latest', '{80, 443}', 'running'),
    ('postgres1', 'postgres:latest', '{5432}', 'running');