class Animal():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, name, species, status, locationId, customerId):
        self.name = name
        self.species = species
        self.status = status
        self.locationId = locationId
        self.customerId = customerId
    def __repr__(self):
        return f"{self.name} is a {self.species}"
