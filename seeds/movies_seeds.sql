DROP TABLE IF EXISTS movies; 

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title text,
    year int,
    rating decimal(2,1),
    trailer text,
    ON DELETE CASCADE
);

INSERT INTO movies ("title", "year", "rating", "trailer") VALUES
('Shawshank Redemption', 1994, 9.2, 'PLl99DlL6b4'),
('The Godfather', 1972, 9.2, 'UaVTIH8mujA'),
('The Dark Knight', 2008, 9.0, 'LDG9bisJEaI'),
('The Godfather: Part II', 1974, 9.0, 'OA1ij0alE0w'),
('12 Angry Men', 1957, 9.0, 'TEN-2uTi2c0'),
('Schindler''s List', 1993, 8.9, 'mxphAlJID9U'),
('The Lord of the Rings: The Return of the King', 2003, 8.9, 'JFpIPkJ31Uw'),
('Pulp Fiction', 1994, 8.8, 'tGpTpVyI_OQ'),
('The Lord of the Rings: The Fellowship of the Ring', 2001, 8.8, 'cKEGZ-CvWHk'),
('The Good, the Bad and the Ugly', 1996, 8.8, 'IFNUGzCOQoI'),
('Forrest Gump', 1994, 8.8, 'bLvqoHBptjg'),
('Fight Club', 1999, 8.7, 'dfeUzm6KF4g'),
('The Lord of the Rings: The Two Towers', 2002, 8.7, 'hYcw5ksV8YQ'),
('Inception', 2010, 8.7, 'YoHD9XEInc0'),
('Star Wars: Episode V - The Empire Strikes Back', 1980, 8.7, 'JNwNXF9Y6kY'),
('The Matrix', 1999, 8.7, 'vKQi3bBA1y8'),
('GoodFellas', 1990, 8.7, 'xWMxvFvhAB8'),
('One Flew Over the Cuckoo''s Nest', 1975, 8.6, 'OXrcDonY-B8'),
('Seven', 1995, 8.6, 'znmZoVkCjpI'),
('Seven Samurai', 1954, 8.6, 'wJ1TOratCTo'),
('It''s a Wonderful Life', 1946, 8.6, 'iLR3gZrU2Xo'),
('The Silence of the Lambs', 1991, 8.6, 'W6Mm8Sbe__o'),
('City of God', 2002, 8.6, 'RfnGQetbX-U'),
('Saving Private Ryan', 1998, 8.6, '9CiW_DgxCnQ'),
('Life is Beautiful', 1997, 8.6, '8CTjcVr9Iao'),
('Interstellar', 2014, 8.6, 'zSWdZVtXT7E'),
('The Green Mile', 1999, 8.6, 'Ki4haFrqSrw'),
('Star Wars', 1977, 8.5, 'vZ734NWnAHA'),
('Terminator 2: Judgment Day', 1991, 8.5, 'CRRlbK5w8AE'),
('Back to the Future', 1985, 8.5, 'qvsgGtivCgs');


-- To seed db: psql -h 127.0.0.1 whistlejacket-randomizer < seeds/movies_seeds.sql;