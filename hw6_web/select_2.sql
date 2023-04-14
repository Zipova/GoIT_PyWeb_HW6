-- Знайти студента із найвищим середнім балом з певного предмета. (discipline_id = 6)

SELECT AVG(g.grade) as average_grade, s.fullname
FROM grades as g
JOIN students AS s ON s.id = g.student_id
WHERE discipline_id = 6
GROUP BY s.fullname 
ORDER BY average_grade DESC
LIMIT 1;

