from class_room.room import Room


class Office(Room):
    def __init__(self, room_name):
        super().__init__(room_name)
        self.capacity = 6
