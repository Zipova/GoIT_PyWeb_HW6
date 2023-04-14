-- Знайти список курсів, які відвідує студент. (student_id = 25)

SELECT d.name
FROM grades as g
JOIN disciplines AS d ON d.id = g.discipline_id
WHERE g.student_id = 25
GROUP BY d.name
