import unittest

from intelliJo.amity.amity import Amity
from intelliJo.person.person import Person
from termcolor import colored
import sys


class TestPersonClass(unittest.TestCase):
    def setUp(self):
        self.pandc = Amity()
        self.test_subject = Person('John', "Doe")

    def tearDown(self):

        self.pandc.rooms['office'] = []
        self.pandc.rooms['livingspace'] = []
        self.pandc.employees['staff'] = []
        self.pandc.employees['fellow'] = []
        self.pandc.waiting_list_for_office = []
        self.pandc.waiting_list_for_living_space = []

    def test_add_person_works(self):
        from io import StringIO
        out = StringIO()
        sys.stdout = out
        test_setid = Person('fred','ping')
        test_setid.set_id(0)
        self.pandc.add_person('joseph', 'ngugi', 'fellow')
        self.pandc.add_person('hannah', 'wong', 'staff')
        print(self.pandc.employees['staff'][0])
        print(self.pandc.employees['fellow'][0])
        output = out.getvalue().strip()[:56]

        self.assertGreater(colored("Fellow joseph ngugi has been successfully added.",'green'), output)

    def test_add_person_only_adds_fellow_or_staff(self):
        error_message = self.pandc.add_person('joseph', 'ngugi', 'dancer')
        self.assertEqual("TIA You can only be staff or fellow", error_message, msg="You can only be staff or fellow")

    def test_add_person_rejects_invalid_names(self):
        error_message = self.pandc.add_person('mickey', 'mouse', 'staff')
        error_message2 = self.pandc.add_person('fred1', 'r@ck', 'fellow')

        self.assertEqual(error_message, "Invalid Name", msg="Must be a valid name")
        self.assertEqual(colored('Name cannot contain digits or funny characters.','red'), error_message2.strip())

    def test_person_full_name_works(self):
        self.assertEqual(self.test_subject.full_name, "John Doe")

