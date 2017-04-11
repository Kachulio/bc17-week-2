from intelliJo.class_fellow.fellow import Fellow
from intelliJo.class_staff.staff import Staff
from intelliJo.class_living_space.living_space import LivingSpace
from intelliJo.class_office.office import Office


class Dojo:
    #check instance type
    def add_person(self, who):
        #if instance type is Staff
        if isinstance(who) is Staff:
            #call the add_staff method
            self.add_staff(args)
        #if instance is not
        else:
            self.add_fellow(args)

    def add_room(self, room_type):
        if isinstance(room_type) is LivingSpace:
            self.create_living_space(args)
        else:
            self.create_office(args)


    def add_staff(self,args):
        pass


    def add_fellow(self,args):
        pass


    def create_office(self, args):
        pass


    def create_living_space(self,args):
        pass
