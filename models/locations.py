class Location():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city
    def __repr__(self):
      return f"{self.name} is in {self.city}."