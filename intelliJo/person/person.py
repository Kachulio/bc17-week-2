class Person:
    # this constructor takes three arguments firstName, lastName
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def get_full_name(self):
        return self.first_name + " " + self.last_name

