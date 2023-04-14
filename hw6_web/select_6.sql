-- Знайти список студентів у певній групі. (group_id = 1)

SELECT gr.name, s.fullname
FROM students AS s
JOIN groups AS gr ON s.group_id = gr.id
WHERE gr.id = 1

