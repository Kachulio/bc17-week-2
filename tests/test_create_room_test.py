import unittest

from intelliJo.dojo.dojo import Dojo
from intelliJo.room.room import Room


class TestCreateRoom(unittest.TestCase):
    def test_create_room_successfully(self):
        my_class_instance = Dojo()
        initial_room_count = Room.all_rooms
        blue_office = my_class_instance.create_room("Blue", "office")
        self.assertTrue(blue_office)

        self.assertEqual(Room.all_rooms - initial_room_count, 1)


if __name__ == '__main__':
    unittest.main()
