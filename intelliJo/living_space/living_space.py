from intelliJo.room.room import Room


class LivingSpace(Room):
    def __init__(self, room_name):
        super().__init__(room_name)
        self.capacity = 4

    def __str__(self):
        print(self.room_name)