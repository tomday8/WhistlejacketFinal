DROP TABLE IF EXISTS "user";

CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    firstname text,
    email text,
    password_hash text,
    joined_at date
);

-- To seed db: psql -h 127.0.0.1 whistlejacket-randomizer < seeds/user_seeds.sql;