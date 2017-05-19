class Person:
    # this constructor takes three arguments firstName, lastName
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name


class Fellow(Person):
    def __init__(self, first_name, last_name):
        super().__init__(
            first_name,
            last_name,
        )

    def __str__(self):
        return self.first_name + " " + self.last_name

class Staff(Person):
    def __init__(self, first_name, last_name):
        super().__init__(
            first_name,
            last_name,
        )