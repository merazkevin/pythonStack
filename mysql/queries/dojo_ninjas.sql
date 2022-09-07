-- DELETE FROM table_name WHERE condition;
-- SELECT * FROM users;
-- UPDATE table_name SET column1 = value1, column2 = value2, WHERE condition;
-- INSERT INTO table_name (column_name1, column_name2) VALUES('column1_value', 'column2_value');



-- add 3 dojos----.>
INSERT INTO dojos_ninjas.dojo(dojo.name) VALUE('Combat_Fitness');
INSERT INTO dojos_ninjas.dojo(dojo.name) VALUE('Combat_Fitness1');
INSERT INTO dojos_ninjas.dojo(dojo.name) VALUE('Combat_Fitness2');
INSERT INTO dojos_ninjas.dojo(dojo.name) VALUE('Combat_Fitness3');

-- delete 3 dojos------
SELECT * FROM dojos_ninjas.dojo;
DELETE FROM dojos_ninjas.dojo Where id=10;
DELETE FROM dojos_ninjas.dojo Where id=11;
DELETE FROM dojos_ninjas.dojo Where id BETWEEN 2 and 4;

-- Query: Create 3 more dojos--->
SELECT * FROM dojos_ninjas.dojo;
INSERT INTO dojos_ninjas.dojo(dojo.name) VALUE('Combat_Fitness4');
INSERT INTO dojos_ninjas.dojo(dojo.name) VALUE('Combat_Fitness5');
INSERT INTO dojos_ninjas.dojo(dojo.name) VALUE('Combat_Fitness6');

-- INSERT INTO table_name (column_name1, column_name2) VALUES('column1_value', 'column2_value');
-- create 3 nijas that belong to the firts dojo---->
SELECT * FROM dojos_ninjas.ninjas;
INSERT INTO dojos_ninjas.ninjas(first_name, last_name, age) VALUE('Jesus', 'Lara', 32);
INSERT INTO dojos_ninjas.ninjas(ninjas.id, ninjas.first_name, ninjas.last_name, ninjas.age) VALUE('1','Kevin', 'M', '29');
INSERT INTO dojos_ninjas.ninjas(ninjas.id, first_name, last_name, age) VALUE('6','Deepay', 'S', '36');
INSERT INTO dojos_ninjas.ninjas(ninjas.id, first_name, last_name, age) VALUE('Alia', 'M', '27');
DELETE FROM dojos_ninjas.ninjas WHERE ninjas.id='6';
SELECT * FROM dojo LEFT JOIN ninjas ON dojo.id = ninjas.dojo_id;