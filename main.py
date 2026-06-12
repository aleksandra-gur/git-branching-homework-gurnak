# пример начального main.py
print("Student Branching App")
print("Проект для тренировки веток Git")

# main.py после подключения profile.py
from profile import print_profile

print("Student Branching App")
print_profile()


# main.py после подключения subjects.py
from profile import print_profile
from subjects import print_subjects

print("Student Branching App")
print_profile()
print_subjects()

# main.py после подключения report.py
from profile import print_profile
from subjects import print_subjects
from report import print_report

print("Student Branching App")
print_profile()
print_subjects()
print_report()
