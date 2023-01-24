DROP TABLE IF EXISTS movies; 

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title text,
    rating decimal(2,1)
);

INSERT INTO movies ("title", "rating") VALUES
('Shawshank Redemption', 9.2),
('The Godfather', 9.0),
('The Dark Knight', 9.0);

-- To seed db: psql -h 127.0.0.1 whistlejacket-randomizer < seeds/movies_seeds.sql;