class Car:
 def __init__(self, make, model, year):
  self.make = make
  self.model = model
  self.year = year

 def get_info(self):
  return str(self.year) + " " + self.make + " " + self.model


class Employee:
 def __init__(self, name, position, salary):
  self.name = name
  self.salary = salary

 def get_salary_info(self):
  return "Заробітна плата " + self.name + ": " + str(self.salary)
