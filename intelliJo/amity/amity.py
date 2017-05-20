import random
import time
from intelliJo.person.person import Fellow
from intelliJo.person.person import Staff
from intelliJo.room.room import LivingSpace
from intelliJo.room.room import Office


class Amity:
    free_living_space = []
    filled_living_space = []

    free_office = []
    filled_office = []

    office_rooms = [Office('black'), Office('Yellow'), Office("Brown"), Office("Pink")]
    waiting_list = []
    rooms_with_people = {}
    data = {}

    # please do note that add_person and create_room are being called from intelli_dojo.py file

    # add_person method checks the docopt args <type> to see if the value is staff|fellow
    # and calls the appropriate method depending on the type value

    def add_person(self, args):
        toon_names = ["mickey mouse", "donald duck"]
        firstname_lastname = args['<first_name>'] + " " + args['<last_name>']

        if firstname_lastname in toon_names:
            print("TIA, maybe you're looking for Walt Disney")
            return "Invalid Name"

        elif not firstname_lastname.replace(' ', '').isalpha():
            return 'Name cannot contain digits or funny characters.'


        who = args["<type>"]
        # i just use who.lower() to make the string lowercase just to make my life easy
        if who.lower() == "staff":
            # if true call the add_staff method
            return self.add_staff(args)

        elif who.lower() == "fellow":
            # call the add_fellow method
            return self.add_fellow(args)
        else:
            return "TIA You can only be staff or fellow"

    # create_room method checks the docopt args <room_type> to see if the value is livingspace|office
    # and calls the appropriate method depending on the room_type value
    def create_room(self, args):
        # gets the room_type  value
        room_type = args["<room_type>"]

        # convert the string to lowercase because the user might enter something like this LivInGspAce
        if room_type.lower() == "livingspace":
            # if the room_type return the value livingspace call the create_living_space method
            self.create_living_space(args)

        # else call the create_office method
        elif room_type.lower() == 'office':
            self.create_office(args)

        else:
            return "We currently don't have {} that type of room".format(room_type)

    def print_room(self, name):
        if name in self.rooms_with_people:

            print("\t\t "+name)
            print('------------------')
            for occupants in self.rooms_with_people[name]:
                print(occupants)
            return 'those are all occupants'
        else:
            print('there is no room named ' + name)
            return 'there is no room named ' + name

    def reallocate_person(self, p_id, new_room):
        #query the database
        db = [1,2,4,5,6,7,8,9,10]
        if p_id in db:
            if new_room in self.free_living_space:
                p_id.living

    # this method will be responsible for for creating staff user when completed
    def add_staff(self, args):
        # create an instance of Staff by passing the values we got from docopt.
        staff = Staff(args['<first_name>'], args["<last_name>"])

        # gives a feedback to the user if the staff was created.
        print("Staff {} {} has been successfully added.".format(staff.first_name, staff.last_name))
        self.store_data(self.get_random_office(), "Office", staff)

        # gives a feedback to the user if the office was created.
        print("{} has been allocated the office {}".format(staff.first_name, self.get_random_office().room_name))

    # this method is responsible for creating a new fellow
    def add_fellow(self, args):

        # create an instance of class Fellow
        fellow = Fellow(args['<first_name>'], args["<last_name>"])


        self.store_data('black', "Office", fellow)

        if args["<accommodation>"] is None:
            # gives a feedback to the user if the fellow was created.
            office = self.get_random_office()
            print("Fellow {} {} has been successfully added.".format(fellow.first_name, fellow.last_name))

            if office is not None:
                if len(office._people) < 6:
                    office._people.append(fellow)
                    print("{} has been allocated the office {}".format(fellow.first_name, office.room_name))
                    self.rooms_with_people[office.room_name] = office._people
                    return "success"
                else:
                    print("The {} office is full ".format(office.room_name))
                    print("Chosing a random Office again..")



        # checks if the fellow wants accommodation
        elif args["<accommodation>"].lower() == "y":
            # if yes get a random room from the list
            space = self.get_random_living_space()
            if space is None:
                self.waiting_list.append(fellow)
            else:
                self.allocate_living_space(self.get_random_living_space().name, fellow)

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
            Amity.free_living_space.append(LivingSpace(args))
        else:
            for i in args["<room_name>"]:
                Amity.free_living_space.append(LivingSpace((i)))
                print("A LivingSpace called {} has been successfully created!".format(i))

    # this method allocates a living space
    def allocate_living_space(self, fellow):
        # gives a feedback to the user if the fellow was created.
        temp_living = self.get_random_living_space()
        if temp_living is None:
            return "No Living space"

        else:
            temp_living.people.append(fellow)
            if temp_living.is_full():
                self.free_living_space.remove(temp_living)


        print("Fellow {} {} has been successfully added.".format(fellow.first_name, fellow.last_name))
        print("{} has been allocated the office {} wow".format(fellow.first_name, self.query_office_data(fellow)))

       # print("{} has been allocated the LivingSpace {}".format(fellow.first_name)



    # When i call this function it will first check if there is a living space, if there is a living space,
    # It will return a random living space, else
    # It will call the create_living_space to
    def get_random_living_space(self):

        # Edge case for checking if there are rooms.
        if len(Amity.free_living_space) == 0:
            time.sleep(3)
            print("Hey Oscar, what's the big idea?")
            print()
            time.sleep(2)
            print("OOPS this is embarrassing, there is no Living Space")
            time.sleep(1)

            print("I have just added you to the waiting list.")

            return None
        # Returns a random room
        return random.choice(Amity.free_living_space)

    # Returns a random Office
    def get_random_office(self):
        if len(Amity.office_rooms) == 0:
            time.sleep(2)
            print("We are currently working on some offices now")
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
    def query_office_data(self, user):
        for key, value in self.data.items():
            for room, occupants in value.items():
                if user in occupants and room == "Office":
                    return key


    def query_living_space_data(self, user):
        for key, value in self.data.items():
            for room, occupants in value.items():
                if user in occupants and room == "free_living_space":
                    return key

