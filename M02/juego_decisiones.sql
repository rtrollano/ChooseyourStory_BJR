DROP DATABASE IF EXISTS juego_decisiones;
CREATE DATABASE juego_decisiones;
USE juego_decisiones;

CREATE TABLE users (
    id_user INTEGER PRIMARY KEY,
    username TEXT NOT NULL
);


CREATE TABLE adventures (
    id_adventure INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);


CREATE TABLE characters (
    id_character INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);


CREATE TABLE game_states_master (
    id_state INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    initial_value INTEGER NOT NULL
);


CREATE TABLE adventure_states (
    id_adventure INTEGER,
    id_state INTEGER,
    PRIMARY KEY (id_adventure, id_state),
    FOREIGN KEY (id_adventure) REFERENCES adventures(id_adventure),
    FOREIGN KEY (id_state) REFERENCES game_states_master(id_state)
);


CREATE TABLE adventure_context (
    id_adventure INTEGER PRIMARY KEY,
    context_text TEXT NOT NULL,
    FOREIGN KEY (id_adventure) REFERENCES adventures(id_adventure)
);


CREATE TABLE adventure_characters (
    id_adventure INTEGER,
    id_character INTEGER,
    PRIMARY KEY (id_adventure, id_character),
    FOREIGN KEY (id_adventure) REFERENCES adventures(id_adventure),
    FOREIGN KEY (id_character) REFERENCES characters(id_character)
);


CREATE TABLE steps (
    id_step INTEGER,
    id_adventure INTEGER,
    description TEXT NOT NULL,
    final_step INTEGER NOT NULL,
    PRIMARY KEY (id_step, id_adventure),
    FOREIGN KEY (id_adventure) REFERENCES adventures(id_adventure)
);


CREATE TABLE answers (
    id_answer INTEGER,
    id_adventure INTEGER,
    id_step INTEGER,
    description TEXT NOT NULL,
    resolution_answer TEXT NOT NULL,

    -- states (solo se usan los que aplique cada aventura)
    crew_loss INTEGER DEFAULT 0,
    damage_ship INTEGER DEFAULT 0,
    salud INTEGER DEFAULT 0,

    next_step INTEGER,

    PRIMARY KEY (id_answer, id_adventure),
    FOREIGN KEY (id_adventure) REFERENCES adventures(id_adventure),
    FOREIGN KEY (id_step, id_adventure) REFERENCES steps(id_step, id_adventure)
);



CREATE TABLE replay_adventures (
    id_replay INTEGER PRIMARY KEY,
    id_user INTEGER,
    id_adventure INTEGER,
    id_character INTEGER,
    adventure_name TEXT,
    character_name TEXT,
    FOREIGN KEY (id_user) REFERENCES users(id_user),
    FOREIGN KEY (id_adventure) REFERENCES adventures(id_adventure),
    FOREIGN KEY (id_character) REFERENCES characters(id_character)
);


