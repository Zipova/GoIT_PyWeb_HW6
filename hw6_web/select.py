import sqlite3


def select_from_db(filename):
    with open(filename, "r") as f:
        sql = f.read()

        with sqlite3.connect('hw6.db') as con:
            cur = con.cursor()
            cur.execute(sql)
            return cur.fetchall()


if __name__ == '__main__':
    print('Знайти 5 студентів із найбільшим середнім балом з усіх предметів.')
    print(select_from_db('select_1.sql'))
    print('\nЗнайти студента із найвищим середнім балом з певного предмета. (discipline_id = 6)')
    print(select_from_db('select_2.sql'))
    print('\nЗнайти середній бал у групах з певного предмета. (discipline_id = 1)')
    print(select_from_db('select_3.sql'))
    print('\nЗнайти середній бал на потоці (по всій таблиці оцінок).')
    print(select_from_db('select_4.sql'))
    print('\nЗнайти які курси читає певний викладач. (teacher_іd = 2)')
    print(select_from_db('select_5.sql'))
    print('\nЗнайти список студентів у певній групі. (group_id = 1)')
    print(select_from_db('select_6.sql'))
    print('\nЗнайти оцінки студентів у окремій групі з певного предмета. (group_id = 1, discipline_id = 1)')
    print(select_from_db('select_7.sql'))
    print('\nЗнайти середній бал, який ставить певний викладач зі своїх предметів. (teaher_id = 4)')
    print(select_from_db('select_8.sql'))
    print('\nЗнайти список курсів, які відвідує студент. (student_id = 25)')
    print(select_from_db('select_9.sql'))
    print('\nСписок курсів, які певному студенту читає певний викладач. (student_id = 29, teacher_id = 3)')
    print(select_from_db('select_10.sql'))
    print('\nСередній бал, який певний викладач ставить певному студентові. (student_id = 16, teacher_id = 2)')
    print(select_from_db('select_11.sql'))
    print('\nОцінки студентів у певній групі з певного предмета на останньому занятті. (group_id = 2, discipline_id = 4)')
    print(select_from_db('select_12.sql'))