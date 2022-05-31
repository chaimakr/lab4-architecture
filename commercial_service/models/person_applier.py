class PersonApplier:
  def __init__(self,firstname,lastname,salary,finantialSituation,age):
    self.firstname = firstname
    self.lastname = lastname
    self.salary=salary
    self.finantialSituation=finantialSituation
    self.age = age
  def __str__(self):
    return "PersonApplier(firstname={}, lastname={}, salary={}, finantialSituation={}, age={})".format(self.firstname, self.lastname, self.salary, self.finantialSituation, self.age)