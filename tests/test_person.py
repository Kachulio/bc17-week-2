import unittest

from intelliJo.amity.amity import Amity


class TestPersonClass(unittest.TestCase):
    def setUp(self):
        self.pandc = Amity()

        self.args = {'<accommodation>': None,
                     '<first_name>': 'jose',
                     '<last_name>': 'ngugi',
                     '<type>': 'fellow'
                     }

        self.wrong_args1 = {'<accommodation>': None,
                     '<first_name>': 'jose',
                     '<last_name>': 'ngugi',
                     '<type>': 'admin'
                     }

        self.wrong_args2 = {'<accommodation>': None,
                           '<first_name>': 'mickey',
                           '<last_name>': 'mouse',
                           '<type>': 'staff'
                           }

    def test_add_person_works(self):
        status = self.pandc.add_person(self.args)
        self.assertEquals(status, 'success')

    def test_add_person_only_adds_fellow_or_staff(self):
        error_message = self.pandc.add_person(self.wrong_args1)
        self.assertEqual("TIA You can only be staff or fellow", error_message, msg="You can only be staff or fellow")

    def test_add_person_rejects_invalid_names(self):
        error_message = self.pandc.add_person(self.wrong_args2)
        self.assertEqual(error_message, "Invalid Name", msg="Must be a valid name")

    def test_integrity(self):
        pass

    def test_passion(self):
        pass

    def test_excellence(self):
        pass

    def test_collaboration(self):
        pass
