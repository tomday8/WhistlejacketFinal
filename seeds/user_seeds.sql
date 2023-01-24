CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    username text,
    email text,
    password_hash text,
    joined_at date
);