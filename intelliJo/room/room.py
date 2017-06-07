class Room:

    def __init__(self, room_name):
        self.room_name = room_name

    @property
    def room_type(self):
        return self.__class__.__name__


    def insert_user(self, user):
        if len(self.people) == self.max_capacity:
            return "The office {} is full".format(self.room_name)
        else:
            self.people.append(user)
            return 'user added successfully'



class LivingSpace(Room):
    def __init__(self, room_name):
        super().__init__(room_name)
        self.max_capacity = 4
        self.people = []

    def is_full(self):
        return self.max_capacity == self.people

    def __str__(self):
        return "Living Space: " + self.room_name

class Office(Room):
    def __init__(self, room_name):
        super().__init__(room_name)
        self.people = []
        self.max_capacity = 6

    def is_full(self):
        return self.max_capacity == self.people

    def __str__(self):
        return "Office: " + (self.room_name)
