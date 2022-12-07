class vehicle:
    class_name = 'django'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Details:", self.name, self.salary, self.class_name)

    def bike(self):
        print('honda')


class car(vehicle):
    def max_speed(self):
        print('yes')

    def min_speed(self):
        print('no')


object = car('python', 30000)
object.show()
object.bike()
object.max_speed()
object.min_speed()

object1 = vehicle('postgresql',40000)
object1.show()
object1.bike()

this is example program to polymorphism topic