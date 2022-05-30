class PersonApplier:
  def __init__(self, id,firstname,lastname,salary,finantialSituation,age):
    self.id = id
    self.firstname = firstname
    self.lastname = lastname
    self.salary=salary
    self.finantialSituation=finantialSituation
    self.age = age
  def __str__(self):
    return "PersonApplier(id={}, firstname={}, lastname={}, salary={}, finantialSituation={}, age={})".format(self.id, self.firstname, self.lastname, self.salary, self.finantialSituation, self.age)