
CREATE TABLE student (id INTEGER, student_name TEXT, PRIMARY KEY(id));
INSERT INTO student (id,student_name) SELECT id, student_name FROM students;


CREATE TABLE house (id INTEGER, house TEXT, PRIMARY KEY(id));
INSERT INTO house (id,house) SELECT id, house FROM students;

CREATE TABLE head (house TEXT, head TEXT, PRIMARY KEY(house));
INSERT INTO head (house, head) SELECT DISTINCT house,head FROM students;