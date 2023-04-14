-- Середній бал, який певний викладач ставить певному студентові. (student_id = 16, teacher_id = 2)

SELECT AVG(g.grade) as average_grade
FROM grades as g
JOIN disciplines AS d ON d.id = g.discipline_id
WHERE g.student_id = 16 AND d.teacher_id = 2
