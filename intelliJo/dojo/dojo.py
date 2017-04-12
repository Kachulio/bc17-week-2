import random

from intelliJo.fellow.fellow import Fellow
from intelliJo.staff.staff import Staff
from intelliJo.living_space.living_space import LivingSpace
from intelliJo.office.office import Office


class Dojo(list):
    # check instance type




    def add_person(self, args):
        who = args["<type>"]
        # if instance type is Staff
        if who.lower() == "staff":
            # call the add_staff method
            self.add_staff(args)

        else:
            self.add_fellow(args)

    def add_room(self, args):
        room_type = args["<room_type>"]
        if room_type.lower() == "livingspace":
            self.create_living_space(args)
        else:
            self.create_office(args)

    def add_staff(self, args):
        staff = Staff(args['<first_name>'], args["<last_name>"])
        print("Staff {} {} has been successfully added.".format(args['<first_name>'], args["<last_name>"]))
        give_me_an_office = random.choice(["blue", "black", "red", "yellow"])
        print("{} has been allocated the office {}".format(staff.first_name, give_me_an_office))




    def add_fellow(self, args):
        print("Fellow {} {} has been successfully added.".format(args['<first_name>'], args["<last_name>"]))
        fellow = Fellow(args['<first_name>'], args["<last_name>"])
        if args["<accommodation>"]:
            give_me_living_space = random.choice(["blue","black","red","yellow"])
            self.allocate_a_living_space(give_me_living_space, fellow, True)

    def create_office(self, args):

        temp_instance = []
        for i in args["<room_name>"]:

             temp_instance.append(Office(i))
             print("An office called {} has been successfully created!".format(i))




    def create_living_space(self, args):
        living_spaces = []
        for i in args["<room_name>"]:
            living_spaces.append(LivingSpace((i)))

            print("A LivingSpace called {} has been successfully created!".format(i))

    def allocate_a_living_space(self,room_name, person_type, want_living_space=False):
        print("{} has been allocated the office {}".format(person_type.first_name, room_name))
        if isinstance(person_type,Fellow) and want_living_space:
            print("{} has been allocated the livingspace {}".format(person_type.first_name, room_name))





