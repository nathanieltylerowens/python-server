class Employee():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, name, manager, fullTime, locationId, customerId):
        self.name = name
        self.manager = manager
        self.fullTime = fullTime
        self.locationId = locationId
        self.hourlyRate = hourlyRate
    def __repr__(self):
      return f"Is {self.name} working? {self.working}."