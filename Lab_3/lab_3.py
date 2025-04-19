import csv
from datetime import date

class Person:
    def __init__(self, surname, first_name, nickname, birth_date_str):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname if nickname else ""
        year, month, day = map(int, birth_date_str.split("-"))
        self.birth_date = date(year, month, day)

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return str(age)

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"

# Функція для створення тестового файлу
def create_test_file(filename):
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["surname", "first_name", "nickname", "birth_date"])
        writer.writerow(["Білець", "Максим", "Максон", "2001-05-20"])
        writer.writerow(["Яресько", "Соня", "", "2005-01-02"])
        writer.writerow(["Ковтун", "Саша", "Саньок", "2001-10-15"])


def modifier(filename):
    people = []

    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:
        person = Person(
            surname=row["surname"],
            first_name=row["first_name"],
            nickname=row.get("nickname", ""),
            birth_date_str=row["birth_date"]
        )
        row["fullname"] = person.get_fullname()
        row["age"] = person.get_age()
        people.append(row)

    fieldnames = ["surname", "first_name", "fullname", "nickname", "birth_date", "age"]
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(people)

# Запуск
if __name__ == "__main__":
    path = "D:/python/.venv/contacts.txt"  # правильний шлях з прямими слешами
    create_test_file(path)
    modifier(path)
    print("Файл оновлено успішно!")
