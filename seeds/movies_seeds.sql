DROP TABLE IF EXISTS movies; 

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title text,
    year int,
    rating decimal(2,1),
    trailer text
);

INSERT INTO movies ("title", "year", "rating") VALUES
('Shawshank Redemption', 1994, 9.2, 'PLl99DlL6b4'),
('The Godfather', 1972, 9.2, 'UaVTIH8mujA'),
('The Dark Knight', 2008, 9.0, 'LDG9bisJEaI'),
('The Godfather: Part II', 1974, 9.0, 'OA1ij0alE0w'),
('12 Angry Men', 1957, 9.0, 'TEN-2uTi2c0'),
('Schindler''s List', 1993, 8.9, 'mxphAlJID9U'),
('The Lord of the Rings: The Return of the King', 2003, 8.9, 'r5X-hFf6Bwo'),
('Pulp Fiction', 1994, 8.8, 'tGpTpVyI_OQ'),
('The Lord of the Rings: The Fellowship of the Ring', 2001, 8.8, 'V75dMMIW2B4'),
('The Good, the Bad and the Ugly', 1996, 8.8, 'IFNUGzCOQoI'),
('Forrest Gump', 1994, 8.8, 'bLvqoHBptjg'),
('Fight Club', 1999, 8.7, 'dfeUzm6KF4g'),
('The Lord of the Rings: The Two Towers', 2002, 8.7, 'r5X-hFf6Bwo'),
-- ('Inception', 2010, 8.7),
-- ('Star Wars: Episode V - The Empire Strikes Back', 1980, 8.7),
-- ('The Matrix', 1999, 8.7),
-- ('GoodFellas', 1990, 8.7),
-- ('One Flew Over the Cuckoo''s Nest', 1975, 8.6),
-- ('Seven', 1995, 8.6),
-- ('Seven Samurai', 1954, 8.6),
-- ('It''s a Wonderful Life', 1946, 8.6),
-- ('The Silence of the Lambs', 1991, 8.6),
-- ('City of God', 2002, 8.6),
-- ('Saving Private Ryan', 1998, 8.6),
-- ('Life is Beautiful', 1997, 8.6),
-- ('Interstellar', 2014, 8.6),
-- ('The Green Mile', 1999, 8.6),
-- ('Star Wars', 1977, 8.5),
-- ('Terminator 2: Judgement Day', 1991, 8.5),
-- ('Back to the Future', 1985, 8.5);


-- To seed db: psql -h 127.0.0.1 whistlejacket-randomizer < seeds/movies_seeds.sql;