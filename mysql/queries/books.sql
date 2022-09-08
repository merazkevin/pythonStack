SELECT * FROM users;
SELECT * FROM books;

#Query: Create 5 different users: Jane Amsden, Emily Dixon,Theodore Dostoevsky, William Shapiro, Lao Xiu
INSERT INTO users (first_name, last_name) 
values ('Jane', 'Amsden'), ('Emily', 'Dixon'), ('Theodore', 'Dostoevsky'), ('William', 'Shapiro'), ('Lao', 'Xiu');
#Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
INSERT INTO books (tittle) VALUES (' C Sharp'), ('Java'), ('Python'), ('PHP'), ('Ruby');
#Query: Change the name of the C Sharp book to C#
UPDATE books SET tittle='C#' WHERE tittle='';