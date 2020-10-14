class Employee():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, position, working):
      self.id = id
      self.name = name
      self.position = position
      self.working = working
    def __repr__(self):
      return f"Is {self.name} working? {self.working}."