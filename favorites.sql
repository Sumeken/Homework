UPDATE shows SET title = 'Brooklyn Nine-Nine' WHERE title LIKE 'Brooklyn%';
UPDATE shows SET title = 'Game of Thrones' WHERE title LIKE 'Game%';
UPDATE shows SET title = 'Grey’s Anatomy' WHERE title LIKE 'Grey%';
UPDATE shows SET title = 'It’s Always Sunny in Philadelphia' WHERE title LIKE 'Its Always%';
UPDATE shows SET title = 'Parks and Recreation' WHERE title LIKE 'Parks and%';
UPDATE shows SET title = 'The Office' WHERE title LIKE '%office%';
UPDATE shows SET title = 'The Office' WHERE title LIKE 'Office%';
SELECT * from shows ORDER BY title;