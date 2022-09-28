#!/usr/bin/python3
"""
Create a class Student that defines a student with: first_name, last_name
and age.
"""


class Student:
    """
    Public attributes: first_name, last_name, age """
    def __init__(self, first_name, last_name, age):
        """Initializes instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of Student instance
        Returns the dict representation of the instance.
        """
        return self.__dict__

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        Public method
        """
        if attrs is None:
            return self.__dict__
        else:
            dictionary = {}
            for attribute in attrs:
                # the keys (of the dict)
                if attribute in self.__dict__.keys():
                    dictionary[attribute] = self.__dict__[attribute]
                    # value (of the dict)
            return dictionary

    def reload_from_json(self, json):
        """
        Public method
        Replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
            # self.__dict__[key] = value
