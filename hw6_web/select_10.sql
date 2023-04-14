-- Список курсів, які певному студенту читає певний викладач. (student_id = 29, teacher_id = 3)

SELECT d.name
FROM grades as g
JOIN disciplines AS d ON d.id = g.discipline_id
WHERE g.student_id = 29 AND d.teacher_id = 3
GROUP BY d.name
