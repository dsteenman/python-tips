class Person:
    pass

person = Person()

person_info = {'first': 'Danny', 'last': 'Steenman'}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))
