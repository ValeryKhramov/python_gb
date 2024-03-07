# 1. Взять класс студент из дз 12-го семинара,
# добавить запуск из командной строки(передача в качестве аргумента название csv-файла с предметами),
# логирование и написать 3-5 тестов с использованием pytest.

import csv
import pytest
import argparse
import logging



def parser():
    parser = argparse.ArgumentParser(description='student_init')
    parser.add_argument('-n', '--name', default='Nike')
    parser.add_argument('-f', '--csv_file', default='example.csv')

    args = parser.parse_args()

    return Student(args.name, args.csv_file)


class Student:

    def __init__(self, name, subjects_file):

        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        logging.info(f'Студент {name} создан')

    def __setattr__(self, name, value):
        if name == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise AttributeError(f"Предмет {name} не найден")

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                subject = row[0]
                if subject not in self.subjects:
                    self.subjects[subject] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        test_scores = self.subjects[subject]['test_scores']
        if len(test_scores) == 0:
            return 0
        return sum(test_scores) / len(test_scores)

    def get_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            grades = self.subjects[subject]['grades']
            if len(grades) > 0:
                total_grades.extend(grades)
        if len(total_grades) == 0:
            return 0
        return sum(total_grades) / len(total_grades)



# # @pytest.fixture
# # def create_student():
# #     return Student("Alex", "test_example.csv")


def test_name():
    student = Student("Alex", "test_example.csv")
    assert student.name == "Alex"

def test_fail_name1():
    with pytest.raises(ValueError):
        student = Student("alex", "test_example.csv")

def test_load_subjects():
    student = Student("Иван", "test_example.csv")
    assert student.subjects == {'Математика': {'grades': [], 'test_scores': []},
                                'Физика': {'grades': [], 'test_scores': []},
                                'История': {'grades': [], 'test_scores': []},
                                'Литература': {'grades': [], 'test_scores': []}}

def test_add_grade():
    student = Student("Иван", "test_example.csv")
    student.add_grade('Математика', 4)
    assert student.subjects == {'Математика': {'grades': [4], 'test_scores': []},
                                'Физика': {'grades': [], 'test_scores': []},
                                'История': {'grades': [], 'test_scores': []},
                                'Литература': {'grades': [], 'test_scores': []}}





if __name__ == '__main__':
     # parser()

    # s = Student("Nike", "example.csv")
    # # s.add_grade('Математика', 4)
    # print(s.subjects)
    #
    # s1 = Student("Alex", "example.csv")

    pytest.main(['-vv'])