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
('The Dark Knight', 2008, 9.0, 'LDG9bisJEaI'),
('Inception', 2010, 8.7, 'YoHD9XEInc0'),
('Interstellar', 2014, 8.6, 'zSWdZVtXT7E'),
('Strange World', 2022, 5.6, 'bKh2G73gCCs'),
('Lightyear', 2022, 6.1, 'BwZs3H_UN3k'),
('The Greatest Showman', 2017, 7.5, 'AXCTMGYUg9A'),
('Topgun: Maverick', 2022, 8.3, 'giXco2jaZ_4'),
('Spider-Man: No Way Home', 2021, 8.2, 'JfVOs4VSpmA'),
('Bullet Train', 2022, 7.3, '0IOsk2Vlc4o'),
('Free Guy', 2021, 7.1, 'JORN2hkXLyM'),
('Luck', 2022, 6.4, 'xSG5UX0EQVg'),
('The Banker', 2020, 7.3, 'J_-nk9-sMus'),
('Finch', 2021, 6.9, 'oah4GNeFcsw'),
('Where the Crawdads Sing', 2022, 7.1, 'PY3808Iq0Tg'),
('Elvis', 2022, 7.4, 'wBDLRvjHVOY'),
('The Gray Man', 2022, 6.5, 'BmllggGO4pM'),
('Death on the Nile', 2022, 6.3, 'dZRqB0JLizw'),
('The Lion King', 2019, 6.8, '7TavVZMewpY'),
('Tenet', 2020, 7.3, 'LdOM0x0XDMo'),
('Turning Red', 2022, 7.0, 'XdKzUbAiswE'),
('Everything Everywhere All at Once', 2022, 8.0, 'wxN1T1uxQ2g'),
('Ticket to Paradise', 2022, 6.2, 'hkP4tVTdsz8'),
('Fantastic Beasts and Where to Find Them', 2016, 7.2, 'ViuDsy7yb8M'),
('Jurassic World: Dominion', 2022, 5.2, 'fb5ELWi-ekk'),
('Avengers: Endgame', 2019, 8.2, 'TcMBFSGVi1c'),
('Captain Marvel', 2019, 6.8, 'Z1BCujX3pw8'),
('Thor: Ragnarok', 2017, 7.9, 'ue80QwXMRHg'),
('Prisoners', 2013, 8.1, '2SupordEUpw'),
('Manchester by the Sea', 2016, 7.8, 'NxQmuJnrjxg'),
('The Theory of Everything', 2014, 7.7, 'Salz7uGp72c'),
('Baby Driver', 2017, 7.6, 'z2z857RSfhk'),
('Blade Runner 2049', 2017, 8.0, 'gCcx85zbxz4');

-- To seed db: psql -h 127.0.0.1 whistlejacket-randomizer < seeds/movies_seeds.sql;