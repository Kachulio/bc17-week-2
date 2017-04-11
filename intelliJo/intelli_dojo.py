import sys
import cmd
from docopt import docopt, DocoptExit

from intelliJo.class_dojo.dojo import Dojo


"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    intellijo create_room <room_type> <room_name>...
    intellijo (-i | --interactive)
    intellijo (-h | --help)
Options:
    -o, --output  Save to a txt file
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""




def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive(cmd.Cmd):
    prompt = '(intellijo) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""

        print('Room type: ' + args['<room_type>'])
        print('Room name: ' + args['<room_name>'][0])

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <first_name> <last_name>"""

        print("person created ", args['<first_name>'] + " " + args['<first_name>'])

    def do_quit(self, args):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
