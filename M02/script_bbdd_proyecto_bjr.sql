DROP SCHEMA IF EXISTS proyecto_bjr2;
CREATE SCHEMA proyecto_bjr2 COLLATE = utf8_general_ci;
USE proyecto_bjr2;

create table if not exists `characters` (
	idCharacter int primary key auto_increment not null,
    CharacterName varchar(45) 
);
create table if not exists `adventure` (
	idAdventure int primary key auto_increment not null,
    Name varchar(45),
    Description varchar(2000),
    idCharacter int ,
    foreign key (`idCharacter`) references characters (`idCharacter`)
);
create table if not exists `bystep_adventure` (
	idByStep_Adventure int primary key auto_increment not null,
    idAdventure int ,
    Description varchar(4000),
    Final_Step tinyint,
    foreign key (`idAdventure`) references adventure (`idAdventure`)
);
create table if not exists `user` (
	idUser int primary key auto_increment not null,
    Username varchar(10),
    Password varchar(45)
);
create table if not exists `game` (
	idGame int primary key auto_increment not null,
	idUser int not null,
	idCharacter int not null,
	idAdventure int not null,
    date datetime,
    foreign key (`idCharacter`) references adventure (`idCharacter`),
    foreign key (`idUser`) references user(`idUser`),
    foreign key (`idAdventure`) references adventure (`idAdventure`)
);
create table if not exists `answers_bysteps_adventure` (
	idAnswers_ByStep_Adventure int primary key auto_increment not null,
    idByStep_Adventure int not null,
    Description varchar(2000),
    Resolution_Answer varchar(200),
    NextStep_Adventure int,
	foreign key (`idByStep_Adventure`) references bystep_adventure (`idByStep_Adventure`),
    foreign key (`NextStep_Adventure`) references bystep_adventure(`idAdventure`)
);
create table if not exists `choices` (
	idGame int not null,
	idByStep_Adventure int not null,
	idAnswers_ByStep_Adventure int not null,
    foreign key (`idGame`) references game (`idGame`),
    foreign key (`idByStep_Adventure`) references bystep_adventure(`idByStep_Adventure`),
    foreign key (`idAnswers_ByStep_Adventure`) references answers_bysteps_adventure (`idAnswers_ByStep_Adventure`)
);
CREATE TABLE `game_states_master` (
    idState INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    initial_value INTEGER NOT NULL
);
CREATE TABLE `steps` (
    idStep INTEGER,
    idAdventure INTEGER,
    description TEXT NOT NULL,
    final_step INTEGER NOT NULL,
    PRIMARY KEY (`idStep`, `idAdventure`),
    FOREIGN KEY (`idAdventure`) REFERENCES adventure(`idAdventure`)
);
CREATE TABLE `answers` (
    idAnswer INTEGER,
    idAdventure INTEGER,
    idStep INTEGER,
    description TEXT NOT NULL,
    resolution_answer TEXT NOT NULL,
    -- states (solo se usan los que aplique cada aventura)
    crew_loss INTEGER DEFAULT 0,
    damage_ship INTEGER DEFAULT 0,
    salud INTEGER DEFAULT 0,
    next_step INTEGER,
    PRIMARY KEY (`idAnswer`, `idAdventure`),
    FOREIGN KEY (`idAdventure`) REFERENCES adventure(`idAdventure`),
    FOREIGN KEY (`idStep`, `idAdventure`) REFERENCES steps(`idStep`, `idAdventure`)
);
CREATE TABLE `adventure_states` (
    idAdventure INTEGER,
    idState INTEGER,
    PRIMARY KEY (`idAdventure`, `idState`),
    FOREIGN KEY (`idAdventure`) REFERENCES adventure(`idAdventure`),
    FOREIGN KEY (`idState`) REFERENCES game_states_master(`idState`)
);
CREATE TABLE answer_state_effects (
    idAnswer INTEGER,
    idAdventure INTEGER,
    idState INTEGER,
    value INTEGER,
    PRIMARY KEY (`idAnswer`, `idAdventure`, `idState`),
    FOREIGN KEY (`idAnswer`, idAdventure) REFERENCES answers(`idAnswer`, `idAdventure`),
    FOREIGN KEY (`idState`) REFERENCES game_states_master(`idState`)
);
CREATE TABLE adventure_context (
    idAdventure INTEGER PRIMARY KEY,
    context_text TEXT NOT NULL,
    FOREIGN KEY (`idAdventure`) REFERENCES adventure (`idAdventure`)
);
CREATE TABLE adventure_characters (
    idAdventure INTEGER,
    idCharacter INTEGER,
    PRIMARY KEY (`idAdventure`, `idCharacter`),
    FOREIGN KEY (`idAdventure`) REFERENCES adventure(`idAdventure`),
    FOREIGN KEY (`idCharacter`) REFERENCES characters(`idCharacter`)
);
CREATE TABLE replay_adventures (
    idReplay INTEGER PRIMARY KEY,
    idUser INTEGER,
    idAdventure INTEGER,
    idCharacter INTEGER,
    adventure_name TEXT,
    character_name TEXT,
    FOREIGN KEY (`idUser`) REFERENCES user(`idUser`),
    FOREIGN KEY (`idAdventure`) REFERENCES adventure(`idAdventure`),
    FOREIGN KEY (`idCharacter`) REFERENCES characters(`idCharacter`)
);
