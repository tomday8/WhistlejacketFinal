DROP TABLE IF EXISTS movies CASCADE; 

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title text,
    year int,
    rating decimal(2,1),
    trailer text
    -- ON DELETE CASCADE
);

INSERT INTO movies ("title", "year", "rating", "trailer") VALUES
('Shawshank Redemption', 1994, 9.2, 'PLl99DlL6b4'),
('The Godfather', 1972, 9.2, 'UaVTIH8mujA'),
('The Dark Knight', 2008, 9.0, 'LDG9bisJEaI'),
('The Godfather: Part II', 1974, 9.0, 'OA1ij0alE0w'),
('The Lord of the Rings: The Return of the King', 2003, 8.9, 'JFpIPkJ31Uw'),
('Pulp Fiction', 1994, 8.8, 'tGpTpVyI_OQ'),
('The Lord of the Rings: The Fellowship of the Ring', 2001, 8.8, 'cKEGZ-CvWHk'),
('Forrest Gump', 1994, 8.8, 'bLvqoHBptjg'),
('The Lord of the Rings: The Two Towers', 2002, 8.7, 'hYcw5ksV8YQ'),
('Inception', 2010, 8.7, 'YoHD9XEInc0'),
('Star Wars: Episode V - The Empire Strikes Back', 1980, 8.7, 'JNwNXF9Y6kY'),
('The Matrix', 1999, 8.7, 'EweuTOz7g-g'),
('One Flew Over the Cuckoo''s Nest', 1975, 8.6, 'OXrcDonY-B8'),
('City of God', 2002, 8.6, 'RfnGQetbX-U'),
('Life is Beautiful', 1997, 8.6, '8CTjcVr9Iao'),
('Interstellar', 2014, 8.6, 'zSWdZVtXT7E'),
('The Green Mile', 1999, 8.6, 'Ki4haFrqSrw'),
('Star Wars', 1977, 8.5, 'vZ734NWnAHA'),
('Terminator 2: Judgment Day', 1991, 8.5, 'CRRlbK5w8AE'),
('Back to the Future', 1985, 8.5, 'qvsgGtivCgs'),
('Strange World', 2022, 5.6, 'bKh2G73gCCs'),
('Lightyear', 2022, 6.1, 'BwZs3H_UN3k'),
('The Greatest Showman', 2017, 7.5, 'AXCTMGYUg9A'),
('Topgun: Maverick', 2022, 8.3, 'giXco2jaZ_4'),
('Spider-Man: No Way Home', 2021, 8.2, 'JfVOs4VSpmA'),
('Bullet Train', 2022, 7.3, '0IOsk2Vlc4o'),
('Free Guy', 2021, 7.1, 'JORN2hkXLyM'),
('Luck', 2022, 6.4, 'xSG5UX0EQVg'),
('The Banker', 2020, 7.3, 'J_-nk9-sMus'),
('Finch', 2021, 6.9, 'oah4GNeFcsw');





-- To seed db: psql -h 127.0.0.1 whistlejacket-randomizer < seeds/movies_seeds.sql;