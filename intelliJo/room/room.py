class Room:
    # class variable
    all_rooms = 0

    def __init__(self, room_name):
        self.room_name = room_name
        Room.all_rooms += 1
