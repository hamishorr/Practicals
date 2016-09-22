from programminglanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [ruby,python,vb]

for i in range(len(languages)):
    if languages[i].is_dynamic():
        print("{} is dynamic".format(languages[i].name))
    else:
        print("{} is not dynamic".format(languages[i].name))
