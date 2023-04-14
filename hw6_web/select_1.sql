-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT AVG(g.grade) as average_grade, s.fullname
FROM grades as g
JOIN students AS s ON s.id = g.student_id
GROUP BY s.fullname 
ORDER BY average_grade DESC
LIMIT 5;