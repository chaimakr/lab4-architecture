class PersonApplier:
  def __init__(self, firstname,lastname,salary,financialSituation,age):
    self.firstname = firstname
    self.lastname = lastname
    self.salary=salary
    self.financialSituation=financialSituation
    self.age = age
  def __str__(self):
    return "PersonApplier(firstname={}, lastname={}, salary={}, financialSituation={}, age={})".format(self.firstname, self.lastname, self.salary, self.finantialSituation, self.age)