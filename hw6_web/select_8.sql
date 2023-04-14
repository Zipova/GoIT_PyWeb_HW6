-- Знайти середній бал, який ставить певний викладач зі своїх предметів. (teaher_id = 4)

SELECT AVG(g.grade), d.name
FROM grades as g
JOIN disciplines AS d ON d.id = g.discipline_id
WHERE d.teacher_id = 4
GROUP BY d.name