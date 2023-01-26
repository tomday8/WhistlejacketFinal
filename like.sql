-- SAVE --
INSERT INTO user_movies (user_id, movie_id, save_flag)
VALUES (7, 1, 1)
ON CONFLICT (user_id, movie_id) 
DO UPDATE SET save_flag = 1;


-- REMOVE --
UPDATE user_movies
SET save_flag = 0
WHERE user_id=user.id AND movie_id = movie.id;



-- LIKE --
INSERT INTO user_movies (user_id, movie_id, like_dislike)
VALUES (7, 1, 1)
ON CONFLICT (user_id, movie_id) 
DO UPDATE SET like_dislike = 1;


-- DISLIKE --
INSERT INTO user_movies (user_id, movie_id, like_dislike)
VALUES (7, 1, -1)
ON CONFLICT (user_id, movie_id) 
DO UPDATE SET like_dislike = -1;


-- NEUTRAL
INSERT INTO user_movies (user_id, movie_id, like_dislike)
VALUES (7, 1, 0)
ON CONFLICT (user_id, movie_id) 
DO UPDATE SET like_dislike = 0;
