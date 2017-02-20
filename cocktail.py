"""
how to make a perfect cocktail
pick up your base ('vodka', 'gin', 'tequila', 'rum', 'whiskey')
pick your base brand ('titos', 'ketel one', 'reyka')
othewise on well ('sky', 'beafeater', 'plantation 3', 'altos blanco', 'rittenhouse')
pick or choose your base measument (0.25oz, 0.5oz, 0.75oz, 1oz, 1.5oz, 2oz, 3oz)
choose what kind a juice would you like? ('lime', 'lemon', 'pineapple', 'cranberry', 'ginger beer', 'grapefruit', 'orange juice,')
do you like a sweetener ('sugar', 'syrup', 'sweet vermout', 'campari', 'bitters')
what kind of glass would you like ('low ball', 'high ball', 'cocktail', 'copper', 'flute')
what kind of method would you like to use? ('stir', 'shake', 'up', 'neat', 'chill', 'on the rock')
choose your garnish ('lime', 'lemon', 'mint', 'cherry', 'sugar', 'salt', 'orange peel', 'olives', 'onions')
the out put('good drink', 'perfect cocktail', 'no bad', 'you can try again')
"""

# This function prompts the user to choose a
# base for cocktail, such as whiskey or gin
# --------------------------------------------
def choose_base():
    my_base = raw_input("please choose your base ")
    
    if my_base in ["vodka", "gin", "tequila", "rum", "whiskey"]:
        print "sounds great!, lets go to the next step"
             
    elif my_base not in ["vodka", "gin", "tequila", "rum", "whiskey"]:
        print "please try it again!"

    return my_base


# This function prompts the user for the brand 
# name of the particular drink
# --------------------------------------------
def choose_brand(base):
    vodka = ["titos", "ketel one", "reyka"]
    gin = ["Bombay", "Tanqueray", "Botanist"]
    rum = ["appleton", "plantation 3", "Bacardi"]
    tequila = ["jose cuervo", "patron", "sauza"]
    whiskey = ["Jack Daniels", "Johnie Walker", "McCallan", "Hibiki", "Jura", "Glendfiddich", "Chivas Regal"]
    
    my_brand = raw_input("any brand preference? yes or no: ")
    
    if my_brand == "yes":
        if (base == "vodka"):
            print vodka
        elif (base == "gin"): 
            print gin 
        elif (base == "rum"):
            print rum
        elif (base == "tequila"):
            print tequila
        elif (base == whiskey):
            print whiskey 

    elif my_brand == "no":
        print "the well it is"


def create_your_perfect_cocktail():
    base = choose_base()
    brand = choose_brand()




print create_your_perfect_cocktail()



if __name__ == "main":
    create_your_perfect_cocktail()