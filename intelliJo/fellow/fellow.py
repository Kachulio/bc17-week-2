from intelliJo.person.person import Person


class Fellow(Person):
    def __init__(self, first_name, last_name, wants_accommodation ):
        self.which_office = ''
        super().__init__(
            first_name,
            last_name,
        )

        if wants_accommodation == "y":
            self.living_space = ""

