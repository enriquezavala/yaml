import yaml

students = [{'name' : 'Enrique', 'age' : 17},
            {'name' : 'Katlin', 'age' : 15}]

print(yaml.dump(students))