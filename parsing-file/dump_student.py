import yaml

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student('Enrique', 17)
dump_student = yaml.dump(student)
print(dump_student)