import unittest

from intelliJo.amity.amity import Amity
from intelliJo.person.person import Fellow, Staff



class TestCreateRoom(unittest.TestCase):

    def setUp(self):
        self.oscar = Amity()
        self.office_count = len(Amity.office_rooms)
        self.living_space_count = len(Amity.free_living_space)

        self.people = [
            'John',
            'Awesome',
            'Oti',
            'Ben',
            'Grace',
            'Monica',
            'Helen',

        ]


    def test_create_office_successfully(self):
        self.oscar.create_office("Blue")
        self.assertTrue(self.oscar.office_rooms)


    def test_create_living_space_successfully(self):
        self.oscar.create_living_space("Red")
        self.assertTrue(self.oscar.free_living_space)


    def test_max_capacity_for_office(self):


        pass

    def test_max_capacity_for_living_space(self):

        pass

    def test_print_room_returns_expected_message(self):
        val = self.oscar.print_room('b')
        self.assertEqual('there is no room named b',val )


if __name__ == '__main__':
    unittest.main()
