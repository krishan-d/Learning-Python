"""
Encoding and Decoding Custom Objects:
"""

import json
from json import JSONEncoder


# Custom Encoding:
class Person:
    def __init__(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address

    def to_json(self):
        """
        convert the instance of this class to json
        """
        # default: is a function that should return a serializable version of obj or raise TypeError.
        return json.dumps(self, indent=4, default=lambda o: o.__dict__)
        # return json.dumps(self, indent=4)  # Raise TypeError: Person object ain't JSON serializable


class Address:
    def __init__(self, city, street, pin):
        self.city = city
        self.street = street
        self.pin = pin


# Another way custom encoding:
class EncodePerson(JSONEncoder):
    def default(self, o):
        return o.__dict__


def main():
    add = Address("Noida", "SEZ", "200001")
    p = Person("Edwina", 53, add)

    # Encoding
    # person_json = p.to_json()
    # or
    person_json = json.dumps(p, indent=4, cls=EncodePerson)

    print(person_json)
    print(type(person_json))

    # Decoding
    person = json.loads(person_json)
    print(person)
    print(type(person))


# Custom Decoding: Using object_hook parameter of loads method.
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['img'])
    return dct


if __name__ == '__main__':
    main()

    print("\nParameter object_hook:")
    s = '{"__complex__": true, "real": 1, "img": 2}'
    # Decoding
    res = json.loads(s, object_hook=as_complex)

    print(res)
    print(type(res))
