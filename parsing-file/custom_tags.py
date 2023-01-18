import yaml

def constructor(loader, node):
    fields = loader.construct_mapping(node)
    return Student(**fields);

yaml.add_constructor('!Student', constructor)

class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

with open("custom_tags.yaml", "r") as stream:
    try:
        dict_student = yaml.unsafe_load(stream)
        print(dict_student)
        student = dict_student["student"]
        print(student.name, student.age)
    except yaml.YAMLError as e:
        print(e)
