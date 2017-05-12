import random
import time
from intelliJo.fellow.fellow import Fellow
from intelliJo.staff.staff import Staff
from intelliJo.living_space.living_space import LivingSpace
from intelliJo.office.office import Office


class Amity:
    living_spaces = []
    office_rooms = []
    fellows = []
    staff = []
    data = {}

    # please do note that add_person and add_room are being called from intelli_dojo.py file

    # add_person method checks the docopt args <type> to see if the value is staff|fellow
    # and calls the appropriate method depending on the type value

    def add_person(self, args):
        # the "who variable will be assigned the value of fellow or staff"
        who = args["<type>"]

        # i just use who.lower() to make the string lowercase just to make my life easy
        if who.lower() == "staff":
            # if true call the add_staff method
            self.add_staff(args)
        # an else because i don't need to check if the "who" is a fellow
        else:
            # call the add_fellow method
            self.add_fellow(args)

    # add_room method checks the docopt args <room_type> to see if the value is livingspace|office
    # and calls the appropriate method depending on the room_type value
    def add_room(self, args):
        # gets the room_type  value
        room_type = args["<room_type>"]

        # convert the string to lowercase because the user might enter something like this LivInGspAce
        if room_type.lower() == "livingspace":
            # if the room_type return the value livingspace call the create_living_space method
            self.create_living_space(args)

        # else call the create_office method
        else:
            self.create_office(args)

    # this method will be responsible for for creating staff user when completed
    def add_staff(self, args):
        # create an instance of Staff by passing the values we got from docopt.
        staff = Staff(args['<first_name>'], args["<last_name>"])

        # gives a feedback to the user if the staff was created.
        print("Staff {} {} has been successfully added.".format(staff.first_name, staff.last_name))
        self.store_data(self.give_me_an_office(), "Office", staff)

        # gives a feedback to the user if the office was created.
        print("{} has been allocated the office {}".format(staff.first_name, self.give_me_an_office().room_name))

    # this method is responsible for creating a new fellow
    def add_fellow(self, args):

        toon_names = ["mickey mouse", "donald duck"]
        firstname_lastname = args['<first_name>'] + " " + args['<first_name>']
        print(firstname_lastname)

        if firstname_lastname in toon_names:
            print("TIA, maybe you're looking for Walt Disney")
            return
        # create an instance of class Fellow
        fellow = Fellow(args['<first_name>'], args["<last_name>"], args["<accommodation>"])
        office = self.give_me_an_office()

        self.store_data(office.room_name, "Office", fellow)

        if args["<accommodation>"] is None:

            self.store_data(office.room_name, "Office", fellow)
            # gives a feedback to the user if the fellow was created.
            print("Fellow {} {} has been successfully added.".format(fellow.first_name, fellow.last_name))
            print("{} has been allocated the office {}".format(fellow.first_name, office.room_name))

        # checks if the fellow wants accommodation
        elif args["<accommodation>"].lower() == "y":
            # if yes get a random room from the list

            # and call the allocate_a_living_space method passing it a room and a fellow object
            self.store_data(office.room_name, "Office", fellow)

            self.allocate_a_living_space(self.give_me_a_living_space().room_name, fellow, True)

    # this method is responsible for creating a new offices.
    def create_office(self, args):
        # loop over all the office or offices the user entered
        if isinstance(args, str):
            Amity.office_rooms.append(Office(args))

        else:
            for i in args["<room_name>"]:
                # create some instance of Office class and append them to the temp_office list variable
                Amity.office_rooms.append(Office(i))
                print("An office called {} has been successfully created!".format(i))

    # this method creates a new livingspace.
    def create_living_space(self, args):
        if isinstance(args, str):
            Amity.living_spaces.append(LivingSpace(args))
        else:
            for i in args["<room_name>"]:
                Amity.living_spaces.append(LivingSpace((i)))
                print("A LivingSpace called {} has been successfully created!".format(i))

    # this method allocates a living space
    def allocate_a_living_space(self, room_name, fellow, want_living_space=False):
        # gives a feedback to the user if the fellow was created.
        print("Fellow {} {} has been successfully added.".format(fellow.first_name, fellow.last_name))
        print("{} has been allocated the office {}".format(fellow.first_name, self.query_data(fellow)))
        if isinstance(fellow, Fellow) and want_living_space:
            print("{} has been allocated the LivingSpace {}".format(fellow.first_name, room_name))

    # When i call this function it will first check if there is a living space, if there is a living space,
    # It will return a random living space, else
    # It will call the create_living_space to
    def give_me_a_living_space(self):

        # Edge case for checking if there are rooms.
        if len(Amity.living_spaces) == 0:
            time.sleep(4)
            print("Hey Amity, what's the big idea?")
            print()
            time.sleep(2)
            print("OOPS this is embarrassing there is no Living Space")
            print("just enter the name room you want: ")
            print()
            time.sleep(3)
            print("oh and since your are the first person you get to chose the top deck")
            print()
            time.sleep(2)
            name = input("Enter living space name: ")
            self.create_living_space(name)
            return Amity.living_spaces[0]
        # Returns a random room
        return random.choice(Amity.living_spaces)

    # Returns a random Office
    def give_me_an_office(self):
        if len(Amity.office_rooms) == 0:
            time.sleep(2)
            print("What now ?")
            print()
            time.sleep(2)
            print("OOPS this is embarrassing there are no office rooms")
            print("just enter the office name you want: ")
            print()
            time.sleep(2)
            print("oh and since your are the first person you get to chose the corner you want")
            print()
            time.sleep(2)
            name = input("Enter Office name: ")
            self.create_office(name)
            return Amity.office_rooms[0]

        return random.choice(Amity.office_rooms)

    # Stores Data to a Dictionary
    def store_data(self, room_name, room_type, person_type):
        if room_name in Amity.data:

            Amity.data[room_name][room_type].append(person_type)
        else:
            Amity.data[room_name] = {room_type: []}
            Amity.data[room_name][room_type].append([person_type])

    # Gets Data from a Dictionary
    def query_data(self, user):
        for key, value in self.data.items():
            for room, occupants in value.items():
                if user in occupants and room == "Office":
                    return key


