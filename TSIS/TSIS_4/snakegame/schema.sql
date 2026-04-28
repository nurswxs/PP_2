CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);


CREATE TABLE game_sessions (
    id SERIAL PRIMARY KEY,
    player_id INT REFERENCES players(id) ON DELETE CASCADE,
    score INT NOT NULL,
    level INT NOT NULL,
    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);