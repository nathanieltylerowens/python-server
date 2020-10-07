EMPLOYEES = [
    {
        "id": 1,
        "name": "jim",
        "locationId": 2,
        "manager": True,
        "fullTime": False,
        "hourlyRate": 15
    },
    {
        "id": 2,
        "name": "Stu",
        "locationId": 2,
        "manager": True,
        "fullTime": True,
        "hourlyRate": 8
    },
    {
        "id": 3,
        "name": "Lenny",
        "locationId": 1,
        "manager": False,
        "fullTime": False,
        "hourlyRate": 4
    }
]


def get_all_employees():
    return EMPLOYEES
def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee