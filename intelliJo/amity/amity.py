import random
import sqlite3
import pickle
from intelliJo.person.person import Fellow
from intelliJo.person.person import Staff
from intelliJo.room.room import LivingSpace
from intelliJo.room.room import Office
import time
import sys
import os


class Amity:
    rooms = {"office": [], "livingspace": []}
    employees = {"staff": [], "fellow": []}

    waiting_list_for_office = []
    waiting_list_for_living_space = []

    # please do note that add_person and create_room are being called from intelli_dojo.py file
    # add person adds aether a fellow or staff
    def add_person(self, firstname, lastname, person_type, accommodation=None):
        # a list of cartoon names soon it will be an api call to cartoon network to get a full list of names
        toon_names = ["mickey mouse", "donald duck"]

        # concatenate firstname and lastname and checks whether it's in the toon_names  lists
        if firstname + ' ' + lastname in toon_names:
            print("TIA, maybe you're looking for Walt Disney")
            return "Invalid Name"
        # checks that fists name and last name must only be alphabets
        elif not str(firstname + lastname).isalpha():
            return 'Name cannot contain digits or funny characters.'

        # an if statement to check if the person type variable is staff
        if person_type.lower() == "staff":
            # creates an instance of Staff
            staff = Staff(firstname, lastname)
            self.employees['staff'].append(staff)
            # gives feedback to the user that the staff has been created
            animate_string("Staff {} {} has been successfully added.".format(staff.first_name, staff.last_name),
                           'green', t=0.01)
            # calls the allocate room method and passes the staff object as parameter
            # allocate_room method is defined in line 92
            self.allocate_room(staff)

        elif person_type.lower() == "fellow":
            fellow = Fellow(firstname, lastname)
            self.employees['fellow'].append(fellow)
            print("Fellow {} {} has been successfully added.".format(fellow.first_name, fellow.last_name))

            self.allocate_room(fellow, accommodation)
        else:
            return "TIA You can only be staff or fellow"

    # this method creates rooms depending on the room type that was passed
    def create_room(self, room_name, room_type):
        # convert the string to lowercase because the user might enter something like this LivInGspAce
        if self.check_room(room_name):
            os.system('say A room named {} already exist'.format(room_name))
            return

        if room_type.lower() == "livingspace":
            livingspace = LivingSpace(room_name)
            self.rooms["livingspace"].append(livingspace)
            print("A LivingSpace called {} has been successfully created!".format(room_name))


        elif room_type.lower() == 'office':
            office = Office(room_name)
            self.rooms["office"].append(office)
            print("An Office called {} has been successfully created!".format(room_name))

        else:
            return "We currently don't have {} that type of room".format(room_type)

    # returns a true if there is a room else it returns false if there is no room
    def check_room(self, room_name):
        living = [room for room in self.rooms["livingspace"] if room.room_name.lower() == room_name.lower()]
        office = [room for room in self.rooms["office"] if room.room_name.lower() == room_name.lower()]

        return bool(living) or bool(office)

    # this method is responsible for  allocating rooms for fellows and staff
    def allocate_room(self, person, accommodation=''):
        # check empty rooms
        vacant_office = [office for office in self.rooms['office'] if not office.is_full()]
        if not vacant_office:
            animate_string("Oscar: ops this is embarrassing there are no offices right now", t=0.01)
            animate_string('Oscar: But Construction for offices are currently going on', t=0.01)
            animate_string("Oscar: So this won't take long sorry :-(", t=0.01)
            self.waiting_list_for_office.append(person)
            animate_string("Oscar: I have just added you to the waiting list.", t=0.01)
            print()
        else:
            office = random.choice(vacant_office)
            office.insert_user(person)
            animate_string("{} has been allocated to Office: {}".format(person.first_name, office.room_name), 'white',
                           t=0.01)

        if isinstance(person, Fellow) and accommodation in ("y", "yes", "Y" or "YES"):
            vacant_living_space = [living_space for living_space in self.rooms['livingspace'] if
                                   not living_space.is_full()]
            if not vacant_living_space:
                print('there is no living space')
                self.waiting_list_for_living_space.append(person)
                print("Oscar: I have just added you to the waiting list.")
                return None
            space = random.choice(vacant_living_space)
            space.insert_user(person)
            animate_string("{} has been allocated the livingspace: {}".format(person.first_name, space.room_name),
                           "white", t=0.02)
            print()

    # prints all the people in the specified room name
    def print_room(self, name):
        if self.check_room(name):
            found_room = [room for room in self.rooms['office'] + self.rooms['livingspace'] if room.room_name == name]

            if found_room:
                animate_string("\t\t " + "{}: {}".format(found_room[0].room_type, found_room[0].room_name),
                               found_room[0].room_name)
                print('--------------------------------------------------------------------------')
                if found_room[0].people:
                    for occupant in found_room[0].people:
                        sys.stdout.write('')
                        sys.stdout.write('\t-{}: {}'.format(occupant.person_type, occupant.full_name))
                        sys.stdout.flush()
                        time.sleep(0.2)
                    print('\n')
        else:
            return "No room named: {}".format(name)

    def reallocate_person(self, p_id, new_room):
        # returns a person object in a list or empty list if there is no person with the id provided
        person = [person for person in self.employees['staff'] + self.employees['fellow'] if person.pk == int(p_id)]
        # check if person exists
        if not person:
            return 'Person does not exist'

        # returns aether a living space object or an office object or an empty list if the new_room is not found.
        room = [room for room in self.rooms['office'] + self.rooms['livingspace'] if room.room_name == new_room]
        # check if room exists
        if not room:
            return 'Room does not exist'

        # just to make the code clean and readable, i don't want to keep using the person object inside the list
        # returned in line 135 after using a list comprehension
        person = person[0]
        # same as the person comment
        room = room[0]

        # check if the new_room is full
        if room.is_full():
            return 'the room is full'

        # checks if the person is a staff and wants to be allocated to a living space
        if person.person_type == "Staff" and room.room_type == "LivingSpace":
            return 'Staff cannot be allocated to a living space wacha ukora'

        # checks if the person is in the same room
        if person in room.people:
            return 'Person is already in tha room'

        # if person is in the waiting list for living space, allocate him/her to the new living space
        if person in self.waiting_list_for_living_space and room.room_type == "LivingSpace":
            print(
                'reallocating {} from unallocated to {}: {} '.format(person.full_name, room.room_type, room.room_name))
            room.insert_user(person)
            self.waiting_list_for_living_space.remove(person)

        # if person is in the waiting list for living space, allocate him/her to the new living space
        elif person in self.waiting_list_for_office and room.room_type == "Office":
            print(
                'reallocating {} from unallocated to {}: {} '.format(person.full_name, room.room_type, room.room_name))
            room.insert_user(person)
            self.waiting_list_for_office.remove(person)

        # remove the person in the current room and reallocate  person to the new room
        if room.room_type == 'LivingSpace':
            prev_room = [prev for prev in self.rooms['livingspace'] if person in prev.people]
            prev_room[0].people.remove(person)
            room.insert_user(person)

        else:
            prev_room = [prev for prev in self.rooms['office'] if person in prev.people]
            prev_room[0].people.remove(person)
            room.insert_user(person)
        print()

    def load_people(self, args):
        f = open('people.txt', 'r')
        while True:
            line = f.readline()
            if not line:
                break
            person = line.split()
            if len(person) > 3:
                self.add_person(person[0], person[1], person[2], person[3])
            else:
                self.add_person(person[0], person[1], person[2])

    # prints all the fellow and staff waiting for offices or living space
    def print_unallocated(self, file):

        if file is False:
            if not self.waiting_list_for_office:
                print()
                print('Waiting list for office is empty.')

            else:
                print()
                print("-----------------People Waiting For offices To Be Constructed----------------\n\n")
                count = 0
                for person in self.waiting_list_for_office:
                    count += 1
                    if count == 3:
                        print('\n')
                        sys.stdout.write('')
                        sys.stdout.write('\t-{}: {}'.format(person.person_type, person.full_name))
                        sys.stdout.flush()
                        time.sleep(0.2)
                        continue

                    if count == 5:
                        print('\n')
                        sys.stdout.write('')
                        sys.stdout.write('\t-{}: {}'.format(person.person_type, person.full_name))
                        sys.stdout.flush()
                        time.sleep(0.2)
                        continue

                    sys.stdout.write('\t')
                    sys.stdout.write('\t-{}: {}'.format(person.person_type, person.full_name))
                    sys.stdout.flush()
                    time.sleep(0.2)

            print()
            if len(self.waiting_list_for_living_space) == 0:
                print("-------------------------------------------------------------------------------")
                print()
                print('Waiting list for Living Space is empty.')
            else:
                print()
                print("-----------------People Waiting For living space To Be Constructed----------------\n\n")
                count = 0
                for person in self.waiting_list_for_living_space:
                    count += 1
                    if count == 4:
                        print('\n')
                        sys.stdout.write('')
                        sys.stdout.write('\t-{}: {}'.format(person.person_type, person.full_name))
                        sys.stdout.flush()
                        time.sleep(0.2)
                        continue

                    if count > 4:
                        print('\n')
                        sys.stdout.write('')
                        sys.stdout.write('\t-{}: {}'.format(person.person_type, person.full_name))
                        sys.stdout.flush()
                        time.sleep(0.2)
                        continue

                    sys.stdout.write('\t')
                    sys.stdout.write('\t-{}: {}'.format(person.person_type, person.full_name))
                    sys.stdout.flush()
                    time.sleep(0.2)

            print()
        return 'No one is in the unallocated' if not self.waiting_list_for_living_space + self.waiting_list_for_office else 'printed all the unallocated people successfully'

    # prints all the people in office and and living space
    def print_allocations(self, file):
        print()
        if not file:
            if self.rooms.values():

                for rooms in self.rooms.values():

                    for room in rooms:
                        os.system('say {}{}'.format(room.room_type, room.room_name))
                        print('hellow')
                        animate_string("{}: {}".format(room.room_type, room.room_name), room.room_name)
                        if not room.people:
                            print("--------------------------")
                            os.system('say The room is empty')
                            print('Empty room ')
                            print("--------------------------")
                            continue
                        print("--------------------------")
                        for person in room.people:
                            print("\t-{} {}".format(person.person_type, person.full_name))
                        print()
                    print()
        else:
            return 'No rooms'

    # saves data to the data base
    def save_state(self):
        rooms = pickle.dumps(self.rooms)
        people = pickle.dumps(self.employees)
        waiting_list_office = pickle.dumps(self.waiting_list_for_office)
        waiting_list_living = pickle.dumps(self.waiting_list_for_living_space)
        command = "CREATE TABLE IF NOT EXISTS amity (id INTEGER PRIMARY KEY, rooms TEXT, people TEXT, waiting_list_office TEXT, waiting_list_living TEXT);"
        conn = sqlite3.connect('data.db')

        cursor = conn.cursor()
        cursor.execute(command)
        conn.commit()

        insert_command = "INSERT OR REPLACE INTO amity (rooms, people, waiting_list_office, waiting_list_living) VALUES(?,?,?,?)"
        cursor.execute(insert_command, (rooms, people, waiting_list_office, waiting_list_living))
        conn.commit()

    # loads data from the data base
    def load_state(self):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM amity")
        data = cursor.fetchall().pop()
        self.rooms = pickle.loads(data[1])
        self.employees = pickle.loads(data[2])
        self.waiting_list_for_office = pickle.loads(data[3])
        self.waiting_list_for_living_space = pickle.loads(data[4])


# My function for animating strings
def animate_string(string, clr='magenta', t=0.10):
    a = len(string)
    color = {
        'RED': "\033[1;31m",
        'BLUE': "\033[1;34m",
        'CYAN': "\033[1;36m",
        'GREEN': "\033[22;32m",
        'YELLOW': "\033[1;33m",
        "GREY": "\033[1;30m",
        "MAGENTA": "\033[0;35m",
        "WHITE": "\033[1;37m",
        'RESET': "\033[0;0m",
        '': ''

    }
    if clr.upper() not in color:
        clr = ''
    for i in range(a):
        sys.stdout.write(color[clr.upper()])
        sys.stdout.write(string[i % len(string)])
        sys.stdout.flush()
        time.sleep(t)
    sys.stdout.write('\n')
    sys.stdout.write(color['RESET'])
    time.sleep(0.5)
    return ''
