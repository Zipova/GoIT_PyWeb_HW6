-- Знайти середній бал на потоці (по всій таблиці оцінок).

SELECT AVG(g.grade) as average_grade
FROM grades as g
