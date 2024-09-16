class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

person1 = Person(name="Alice", age=30, gender="Female")
person2 = Person(name="Benson", age=24, gender="male")


person1.introduce()
person2.introduce()
