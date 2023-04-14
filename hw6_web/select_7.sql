-- Знайти оцінки студентів у окремій групі з певного предмета. (group_id = 1, discipline_id = 1)

SELECT g.grade, s.fullname
FROM grades as g
JOIN students AS s ON s.id = g.student_id
WHERE s.group_id = 1 AND g.discipline_id = 1
