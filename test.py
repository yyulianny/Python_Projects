def should_you_eat_the_bacon():
        angels_question = raw_input("do you wnat to feel like angels are frolicking on your taste buds? Y or N:")
        if (angels_question == ("Y")):
                return "eat it!"
        elif angels_question == "N":
                return "You've clearly never tasted bacon, eat it!"
        else:
                coward_question = raw_input("are you a coward? Y or N:")
                if coward_question == "N":
                        return "Then eat it!"
                else:
                        return "Bacon will turn you into a true warrior"


print should_you_eat_the_bacon()
