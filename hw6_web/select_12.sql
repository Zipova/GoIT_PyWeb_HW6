-- Оцінки студентів у певній групі з певного предмета на останньому занятті. (group_id = 2, discipline_id = 4)

SELECT g.grade, s.fullname, g.date_of
FROM grades as g
JOIN students AS s ON s.id = g.student_id
WHERE g.discipline_id = 4 AND s.group_id = 2 AND g.date_of IN (SELECT MAX(date_of)
                                                                FROM grades)

