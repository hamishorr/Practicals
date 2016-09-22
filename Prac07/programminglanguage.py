class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection=False, year=""):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing.upper() == "DYNAMIC":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {}, Reflection = {}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    # def check_str(self):
    #     if self.reflection == self.is_dynamic():
    #         return "correct for language {}".format(self.name)
    #     else:
    #         return "incorrect for language {}".format(self.name)







