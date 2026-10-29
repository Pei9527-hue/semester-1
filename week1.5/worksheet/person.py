# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self,name, birth_data):
        self.name = name
        self birth_data = birth_data

    def initials(self):
        return''.join(word[0].upper() for word in self.name.split())

    def is_birthday(self):
        today = data.today()
        return(
            today.month == self.birth_data.month
            and today.day == self.birth_data
        )


    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
