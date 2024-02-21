# Your code goes here:
def render_person(name, birthdate, eye_color, age, gender):
    return ("{} is a {} years old {} born in {} with {} eyes".format(name, age, gender, birthdate, eye_color))


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))