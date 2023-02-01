CREATE TABLE user_scores (
  user_id INT NOT NULL,
  genre text NOT NULL,
  score INT NOT NULL,
  PRIMARY KEY (user_id, genre)
);

-- To seed db: psql -h 127.0.0.1 whistlejacket-randomizer < seeds/user_scores_seeds.sql;