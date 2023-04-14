from datetime import datetime, timedelta
from random import randint, choice
import sqlite3

from faker import Faker

disciplines = [
    "Русофобія",
    "Мемологія",
    "Дресировка комарів та гусей",
    "Борщ по-бандерівськи",
    "Хакерська справа",
    "Курс забування російської мови",
    "Вирощування бавовни на росії",
    "Тепловізор своїми руками"
]

groups = ["Шевченківці", "Лесяукраїнці", "Іванофранківці"]

NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50
NUMBER_GRADES_FOR_STUDENT = 20
fake = Faker('uk-UA')
connect = sqlite3.connect('hw6.db')
cur = connect.cursor()


def seed_teachers():
    teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]
    sql = "INSERT INTO teachers(fullname) VALUES(?);"
    cur.executemany(sql, zip(teachers, ))


def seed_disciplines():
    sql = "INSERT INTO disciplines(name, teacher_id) VALUES(?, ?);"
    cur.executemany(sql, zip(disciplines, iter(randint(1, NUMBER_TEACHERS) for _ in range(len(disciplines)))))


def seed_groups():
    sql = "INSERT INTO groups(name) VALUES(?);"
    cur.executemany(sql, zip(groups, ))


def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    sql = "INSERT INTO students(fullname, group_id) VALUES(?, ?);"
    cur.executemany(sql, zip(students, iter(randint(1, len(groups)) for _ in range(len(students)))))


def seed_grades():
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-06-30", "%Y-%m-%d")
    sql = "INSERT INTO grades(discipline_id, student_id, grade, date_of) VALUES(?, ?, ?, ?)"

    def get_list_date(start, end):
        result = []
        now = datetime.now()
        if now < end:
            end = now
        current_date = start
        while current_date <= end:
            if current_date.isoweekday() < 6:
                result.append(current_date)
            current_date += timedelta(1)
        return result

    list_dates = get_list_date(start_date, end_date)

    grades = []
    for discipline_id in range(1, len(disciplines)+1):
        for student in range(1, NUMBER_STUDENTS+1):
            for _ in range(0, 20):
                random_date = choice(list_dates)
                grades.append((discipline_id, student, randint(1, 12), random_date))
    cur.executemany(sql, grades)


if __name__ == '__main__':
    try:
        seed_teachers()
        seed_disciplines()
        seed_groups()
        seed_students()
        seed_grades()
        connect.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        connect.close()