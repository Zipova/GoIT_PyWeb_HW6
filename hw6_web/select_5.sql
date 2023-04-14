-- Знайти які курси читає певний викладач. (teacher_іd = 2)

SELECT t.fullname, d.name
FROM teachers AS t
JOIN disciplines AS d ON d.teacher_id = t.id
WHERE teacher_id = 2

