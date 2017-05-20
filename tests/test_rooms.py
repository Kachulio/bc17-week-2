import unittest

from intelliJo.amity.amity import Amity
from intelliJo.person.person import Fellow, Staff
from intelliJo.room.room import Office, LivingSpace



class TestCreateRoom(unittest.TestCase):

    def setUp(self):
        self.oscar = Amity()
        self.living_space = LivingSpace("Braka")
        self.office = Office('Orange')
        self.people = [
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


    def test_office_does_not_exceed_max_capacity(self):
        for i in self.people:
            self.office.insert_user(i)
        self.assertEqual("The office Orange is full", self.office.insert_user('judas'))

    def test_living_space_does_not_exceed_max_capacity_(self):
        for i in self.people:
            self.living_space.insert_user(i)

        self.assertEqual(self.living_space.insert_user('doris'), 'The office Braka is full')


    def test_print_room_returns_expected_message(self):
        val = self.oscar.print_room('b')
        self.assertEqual('there is no room named b',val )

    def test_reallocate_person_success(self):
        # success_message = self.oscar.reallocate_person(2, "blue")
        # self.assertEqual('joseph has been allocated to blue living space', success_message)
        pass


if __name__ == '__main__':
    unittest.main()
