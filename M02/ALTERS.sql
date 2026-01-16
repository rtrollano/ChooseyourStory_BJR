use proyecto_bjr;

alter table characters
modify column CharacterName varchar(80);

alter table characters
add column codAdventure int not null;
