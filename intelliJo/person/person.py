class Person:
    count = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Person.count += 1
        self.pk = Person.count

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def set_id(self, id):
        self.pk = id

    @property
    def person_type(self):
        return self.__class__.__name__


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

    def __str__(self):
        return self.first_name + " " + self.last_name
