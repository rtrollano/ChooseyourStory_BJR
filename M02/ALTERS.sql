use proyecto_bjr2;

alter table characters
modify column CharacterName varchar(80);

alter table adventure
add column codAdventure int not null;
