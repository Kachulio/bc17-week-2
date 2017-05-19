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

        self.wrong_args3 = {'<accommodation>': None,
                            '<first_name>': 'tomas1',
                            '<last_name>': 'duse',
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
        error_message2 = self.pandc.add_person(self.wrong_args3)

        self.assertEqual(error_message, "Invalid Name", msg="Must be a valid name")
        self.assertEqual('Name cannot contain digits or funny characters.', error_message2)



