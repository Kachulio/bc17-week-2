import unittest
from intelliJo.amity.amity import Amity


class TestDataBase(unittest.TestCase):
    def setUp(self):
        self.amity = Amity()
        self.amity.add_person('james', 'windows', 'staff')

    def tearDown(self):
        self.amity.rooms['office'] = []
        self.amity.rooms['livingspace'] = []
        self.amity.employees['staff'] = []
        self.amity.employees['fellow'] = []
        self.amity.waiting_list_for_office = []
        self.amity.waiting_list_for_living_space = []


    def test_load_people(self):
        self.amity.load_people(None)
        all_people_names = [people.full_name for people in self.amity.waiting_list_for_office]
        self.assertIn('DOMINIC WALTERS', all_people_names)

    def test_save_state_and_load_state(self):
        self.amity.save_state()
        self.amity.load_state()

        self.assertTrue(
            [person for person in self.amity.waiting_list_for_office if person.full_name == 'james windows'])

