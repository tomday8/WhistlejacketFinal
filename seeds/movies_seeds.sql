DROP TABLE IF EXISTS movies CASCADE; 

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title text,
    year int,
    rating decimal(2,1),
    trailer text,
    genre text
    -- ON DELETE CASCADE
);

INSERT INTO movies ("title", "year", "rating", "trailer", "genre") VALUES
('The Dark Knight', 2008, 9.0, 'LDG9bisJEaI', 'Action'),
('Inception', 2010, 8.7, 'YoHD9XEInc0', 'Action'),
('Interstellar', 2014, 8.6, 'zSWdZVtXT7E', 'Sci Fi'),
('Strange World', 2022, 5.6, 'bKh2G73gCCs', 'Animation'),
('Lightyear', 2022, 6.1, 'BwZs3H_UN3k', 'Animation'),
('The Greatest Showman', 2017, 7.5, 'AXCTMGYUg9A', 'Musical'),
('Topgun: Maverick', 2022, 8.3, 'giXco2jaZ_4', 'Action'),
('Spider-Man: No Way Home', 2021, 8.2, 'JfVOs4VSpmA', 'Action'),
('Bullet Train', 2022, 7.3, '0IOsk2Vlc4o', 'Action'),
('Free Guy', 2021, 7.1, 'JORN2hkXLyM', 'Sci Fi'),
('Luck', 2022, 6.4, 'xSG5UX0EQVg', 'Animation'),
('The Banker', 2020, 7.3, 'J_-nk9-sMus', 'Drama'),
('Finch', 2021, 6.9, 'oah4GNeFcsw', 'Sci Fi'),
('Where the Crawdads Sing', 2022, 7.1, 'PY3808Iq0Tg', 'Drama'),
('Elvis', 2022, 7.4, 'wBDLRvjHVOY', 'Musical'),
('The Gray Man', 2022, 6.5, 'BmllggGO4pM', 'Action'),
('Death on the Nile', 2022, 6.3, 'dZRqB0JLizw', 'Action'),
('The Lion King', 2019, 6.8, '7TavVZMewpY', 'Animation'),
('Tenet', 2020, 7.3, 'LdOM0x0XDMo', 'Sci Fi'),
('Turning Red', 2022, 7.0, 'XdKzUbAiswE', 'Animation'),
('Everything Everywhere All at Once', 2022, 8.0, 'wxN1T1uxQ2g', 'Action'),
('Ticket to Paradise', 2022, 6.2, 'hkP4tVTdsz8', 'Action'),
('Fantastic Beasts and Where to Find Them', 2016, 7.2, 'ViuDsy7yb8M', 'Action'),
('Jurassic World: Dominion', 2022, 5.2, 'fb5ELWi-ekk', 'Action'),
('Avengers: Endgame', 2019, 8.2, 'TcMBFSGVi1c', 'Sci Fi'),
('Captain Marvel', 2019, 6.8, 'Z1BCujX3pw8', 'Sci Fi'),
('Thor: Ragnarok', 2017, 7.9, 'ue80QwXMRHg', 'Sci Fi'),
('Prisoners', 2013, 8.1, '2SupordEUpw', 'Action'),
('Manchester by the Sea', 2016, 7.8, 'NxQmuJnrjxg', 'Drama'),
('The Theory of Everything', 2014, 7.7, 'Salz7uGp72c', 'Drama'),
('Baby Driver', 2017, 7.6, 'z2z857RSfhk', 'Action'),
('Blade Runner 2049', 2017, 8.0, 'gCcx85zbxz4', 'Sci Fi');

-- To seed db: psql -h 127.0.0.1 whistlejacket-randomizer < seeds/movies_seeds.sql;