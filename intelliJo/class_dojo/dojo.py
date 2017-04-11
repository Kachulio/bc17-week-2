from class_fellow.fellow import Fellow
from class_staff.staff import Staff
from class_living_space.living_space import LivingSpace
from class_office.office import Office


class Dojo:
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
        print(room_type)
        if room_type.lower() == "livingspace":
            self.create_living_space(args)
        else:
            self.create_office(args)

    def add_staff(self, args):
        print("Staff {} {} has been successfully added.".format(args['<first_name>'],args["<last_name>"]))


    def add_fellow(self, args):
        print("Fellow {} {} has been successfully added.".format(args['<first_name>'], args["<last_name>"]))

    def create_office(self, args):
        for i in args["<room_name>"]:
             print("An office called {} has been successfully created!".format(args["<room_name>"]))


    def create_living_space(self, args):
        for i in args["<room_name>"]:
            print("A LivingSpace called {} has been successfully created!".format(i))
