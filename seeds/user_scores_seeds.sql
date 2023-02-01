CREATE TABLE user_scores (
  user_id INT NOT NULL,
  genre text NOT NULL,
  score INT NOT NULL,
  PRIMARY KEY (user_id, genre)
);
