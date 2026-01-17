use proyecto_bjr;

alter table characters
modify column CharacterName varchar(80);

alter table characters
add column codAdventure int not null;

ALTER TABLE characters
ADD CONSTRAINT fk_characters_codAdventure
FOREIGN KEY (codAdventure)
REFERENCES adventure (idAdventure);
