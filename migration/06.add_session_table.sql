CREATE TABLE IF NOT EXISTS  sessions (
    uuid TEXT PRIMARY KEY,
    user_id INTEGER NOT NULL,
    expire_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
);  