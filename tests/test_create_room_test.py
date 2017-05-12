import unittest

from intelliJo.amity.amity import Amity
from intelliJo.room.room import Room


class TestCreateRoom(unittest.TestCase):

    def setUp(self):
        self.dojo = Amity()


    def test_create_room_successfully(self):
        my_class_instance = self.dojo
        initial_room_count = Room.all_rooms
        blue_office = my_class_instance.create_room("Blue", "office")
        self.assertTrue(blue_office)

        self.assertEqual(Room.all_rooms - initial_room_count, 1)

    def test_how_many_room(self):
        pass


if __name__ == '__main__':
    unittest.main()
