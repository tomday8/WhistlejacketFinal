DROP TABLE IF EXISTS user_movies;

CREATE TABLE user_movies (
    id SERIAL PRIMARY KEY,
    user_id INT,
    movie_id INT,
    like_dislike INT DEFAULT 0,
    save_flag INT DEFAULT 0,
    CONSTRAINT unique_user_movie UNIQUE (user_id, movie_id),
    FOREIGN KEY (user_id) REFERENCES "user"(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);

-- To seed db: psql -h 127.0.0.1 whistlejacket-randomizer < seeds/user_movies_seeds.sql;