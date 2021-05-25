BEGIN TRANSACTION;
CREATE TABLE registro(nombre TEXT, apellido TEXT, edad INT);
INSERT INTO "registro" VALUES('Juan','Pérez',18);
INSERT INTO "registro" VALUES('María','González',26);
INSERT INTO "registro" VALUES('Pedro','Ramírez',32);
INSERT INTO "registro" VALUES('José','Buitrago',45);
INSERT INTO "registro" VALUES('Juliana','Rojas',52);
INSERT INTO "registro" VALUES('Rosa','Duarte',63);
COMMIT;
