#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    IntelliJo add_person <person_name> <fellow|staff> [accommodation]
    IntelliJo create_room <room_type> <room_name>...
    IntelliJo print_room <room_name>
    IntelliJo print_unallocated [filename]
    IntelliJo print_allocations [filename]
    IntelliJo load_people [file_name]
    IntelliJo save_state [--db=sqlite_database]
    IntelliJo load_state <sqlite_database>
    IntelliJo print_all_people
    IntelliJo tcp <host> <port> [--timeout=<seconds>]
    IntelliJo serial <port> [--baud=<n>] [--timeout=<seconds>]
    IntelliJo (-i | --interactive)
    IntelliJo (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys, os
import cmd
from docopt import docopt, DocoptExit
from intelliJo.amity.amity import Amity, animate_string
from pyfiglet import figlet_format

dojo = Amity()


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

            animate_string('Man Learn How To Type A Command!')
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
    os.system('clear')
    animate_string(figlet_format("\t" + 'T I A ', 's-relief'), t=0.001)
    print('\n')
    intro = animate_string(figlet_format('A     M     I     T     Y\n', 'lildevil') \
                           + '', 'cyan', t=0.001)
    animate_string(figlet_format('type help for a list of commands'.upper(), "digital"), 'yellow', t=0.001)
    prompt = '(IntelliJo) '
    file = None

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <type> [<accommodation>]"""
        print()
        firstname, lastname, person_type, accommodation = arg['<first_name>'], arg['<last_name>'], arg['<type>'], arg[
            '<accommodation>']
        print(dojo.add_person(firstname, lastname, person_type, accommodation))


    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        print()
        room_names, room_type, = arg['<room_name>'], arg['<room_type>']
        for name in room_names:
            print(dojo.create_room(name, room_type))

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>"""
        print()
        print(dojo.print_room(arg['<room_name>']))

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_identifier> <new_room_name>"""
        print()
        print(dojo.reallocate_person(p_id=arg["<person_identifier>"], new_room=arg["<new_room_name>"]))

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [<file_name>]"""
        print()
        dojo.print_unallocated(arg['<file_name>'])

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [<file_name>]"""

        print(dojo.print_allocations(arg['<file_name>']))

    @docopt_cmd
    def do_load_people(self, arg):
        """Usage: load_people [file_name]"""
        print()
        dojo.load_people(arg)

    @docopt_cmd
    def do_save_state(self, arg):
        """Usage: save_state [--db=sqlite_database]"""
        dojo.save_state(arg['--db'])

    @docopt_cmd
    def do_load_state(self, arg):
        """Usage: load_state <sqlite_database>"""
        dojo.load_state(arg["<sqlite_database>"])


    def do_print_all_people(self,arg):

        print(dojo.print_all_people())

    def do_print_all_rooms(self,arg):

        print(dojo.print_all_rooms())

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
