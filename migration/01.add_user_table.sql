CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    hashed_pw TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);


CREATE UNIQUE INDEX email_uindex ON users (email);
CREATE UNIQUE INDEX user_uindex ON users (username);