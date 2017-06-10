import unittest
import sys
from intelliJo.amity.amity import Amity, animate_string
from intelliJo.person.person import Fellow
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

    def tearDown(self):
        self.oscar.rooms['office'] = []
        self.oscar.rooms['livingspace'] = []
        self.oscar.employees['staff'] = []
        self.oscar.employees['fellow'] = []
        self.oscar.waiting_list_for_office = []
        self.oscar.waiting_list_for_living_space = []

    def test_create_office_successfully(self):
        self.oscar.create_room("Blue", 'office')
        self.assertTrue(self.oscar.rooms['office'])

    def test_create_living_space_successfully(self):
        self.oscar.create_room("Red", 'livingspace')
        self.assertTrue(self.oscar.rooms['livingspace'])

    def test_office_does_not_exceed_max_capacity(self):

        for i in self.people:
            self.office.insert_user(i)
        self.assertEqual("The office Orange is full", self.office.insert_user('judas'))

    # def test_reallocate_to_a_room_that_does_not_exist(self):
    #     self.oscar.add_person('joseph','ngugi','staff')
    #     self.assertEqual(self.oscar.reallocate_person(4,'lavender'),'Room does not exist')
    #

    def test_living_space_does_not_exceed_max_capacity_(self):
        for i in self.people:
            self.living_space.insert_user(i)

        self.assertEqual(self.living_space.insert_user('doris'), 'The office Braka is full')

    def test_print_room_returns_expected_message(self):
        val = self.oscar.print_room('b')
        self.assertEqual('No room named: b', val)



    def test_print_room_when_the_room_is_empty__message(self):
        self.oscar.create_room('Blue','office')
        self.assertEqual(self.oscar.print_room('Blue'),'the room is empty')

    def test_print_room_with_people(self):
        self.oscar.create_room('Grey', 'office')
        self.oscar.add_person('jeb', 'tacos', 'fellow')
        self.assertEqual(self.oscar.print_room('Grey'), None)

    def test_expected_message_after_successfully_allocating_a_fellow(self):
        self.oscar.create_room('yellow', 'livingspace')
        self.assertEqual(self.oscar.allocate_room(Fellow('kim','aladdin'),'y'),'success')

    def test_reallocate_person_error_message(self):
        # assert for person does not exist
        print(self.oscar.waiting_list_for_office)
        print(self.oscar.waiting_list_for_living_space)

        self.assertEqual(self.oscar.reallocate_person(1, 'Braka'), "Person does not exist")

    def test_print_allocations(self):
        self.oscar.create_room('Blue', 'office')
        self.oscar.create_room('green', 'office')
        self.oscar.add_person('joseph','joseph','staff')
        self.assertEqual(self.oscar.print_allocations(None), 'those are all the allocations we currently have')

    def test_print_allocations_after_printing_all_allocations(self):
        pass
    def test_print_unallocated(self):
        # assert unallocated method return the expected message if there is no staff or fellow in the unallocated
        # my teardown is not working so i need to do this
        self.oscar.waiting_list_for_living_space=[]
        self.oscar.waiting_list_for_office=[]
        self.assertEqual(self.oscar.print_unallocated('file'),'No one is in the unallocated \n')

        # assert unallocated method returns the expected message if the were people in the unallocated
        self.oscar.add_person('Bie', 'Go', 'staff')
        self.oscar.add_person('Python', 'Java', 'fellow','y')
        self.oscar.add_person('Beautiful', 'Soup', 'fellow', 'y')
        self.oscar.add_person('Bie', 'Go', 'staff')
        self.oscar.add_person('Python', 'Java', 'fellow', 'y')
        self.oscar.add_person('Beautiful', 'Soup', 'fellow', 'y')
        self.oscar.add_person('Bie', 'Go', 'staff')
        self.oscar.add_person('Python', 'Java', 'fellow', 'y')
        self.oscar.add_person('Beautiful', 'Soup', 'fellow', 'y')
        self.assertEqual(self.oscar.print_unallocated(None), 'printed all the unallocated people successfully \n')

    def test_create_room_with_wrong_room_type(self):
        self.assertEqual(self.oscar.create_room('Green','Nasa'),"We currently don't have Nasa that type of room")

    def test_create_room_that_already_exist(self):
        self.oscar.create_room('red','office')
        # should get an empty string because am using a command to speak to the user so i cannot test the voice
        self.assertEqual(self.oscar.create_room('red','office'),'')



if __name__ == '__main__':
    unittest.main()
