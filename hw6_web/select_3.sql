-- Знайти середній бал у групах з певного предмета. (discipline_id = 1)

SELECT AVG(g.grade) as average_grade, gr.name
FROM grades as g
JOIN students AS s ON s.id = g.student_id
JOIN groups AS gr ON s.group_id = gr.id
WHERE g.discipline_id = 1
GROUP BY gr.name 

