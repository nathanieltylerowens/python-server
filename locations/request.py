LOCATIONS = [
    {
        "id": 1,
        "name": "north",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "south",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "west",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1
    }
]


def get_all_locations():
    return LOCATIONS
def get_single_location(id):
    # Variable to hold the found animal, if it exists
    requested_location = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location ["id"] == id:
            requested_location = location

    return requested_location