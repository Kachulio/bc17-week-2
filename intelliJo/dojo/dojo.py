import random

from intelliJo.fellow.fellow import Fellow
from intelliJo.staff.staff import Staff
from intelliJo.living_space.living_space import LivingSpace
from intelliJo.office.office import Office


class Dojo(list):
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
        print("Staff {} {} has been successfully added.".format(args['<first_name>'], args["<last_name>"]))

        # i use random package to get a random office, for now am just passing a list.
        give_me_an_office = random.choice(["blue", "black", "red", "yellow"])

        # gives a feedback to the user if the office was created.
        print("{} has been allocated the office {}".format(staff.first_name, give_me_an_office))

    # this method is responsible for creating a new fellow
    def add_fellow(self, args):
        # create an instance of class Fellow
        fellow = Fellow(args['<first_name>'], args["<last_name>"])

        # gives a feedback to the user if the staff was created.
        print("Fellow {} {} has been successfully added.".format(args['<first_name>'], args["<last_name>"]))

        # checks if the fellow wants accommodation
        if args["<accommodation>"]:
            # if yes get a random room from the list
            give_me_living_space = random.choice(["blue", "black", "red", "yellow"])
            # and call the allocate_a_living_space method passing it a room and a fellow object
            self.allocate_a_living_space(give_me_living_space, fellow, True)

    # this method is responsible for creating a new offices.
    def create_office(self, args):
        # this time just using a temporary list to hold the arguments the user passed
        temp_offices = []

        # loop over all the office or offices the user entered
        for i in args["<room_name>"]:
            # create some instance of Office class and append them to the temp_office list variable
            temp_offices.append(Office(i))
            print("An office called {} has been successfully created!".format(i))

    def create_living_space(self, args):
        living_spaces = []
        for i in args["<room_name>"]:
            living_spaces.append(LivingSpace((i)))

            print("A LivingSpace called {} has been successfully created!".format(i))

    def allocate_a_living_space(self, room_name, person_type, want_living_space=False):
        print("{} has been allocated the office {}".format(person_type.first_name, room_name))
        if isinstance(person_type, Fellow) and want_living_space:
            print("{} has been allocated the livingspace {}".format(person_type.first_name, room_name))

    # just for unittests
    def create_room(self, room_name, room_type):
        if room_type.lower() == "livingspace":
            return LivingSpace(room_name)

        elif room_type.lower() == "office":
            return Office(room_name)
        else:
            print("TIA")
