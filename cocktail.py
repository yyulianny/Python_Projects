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
def choose_base():
    my_base = raw_input("please choose your base ")
    if my_base in ["vodka", "gin", "tequila", "rum", "whiskey"]:
        print "sounds great!, lets go to the next step"
             
    elif my_base not in ["vodka", "gin", "tequila", "rum", "whiskey"]:
        return "please try it again!"

def choose_brand():

    my_brand = raw_input("any any brand preference? yes or no: ")
    if my_brand == "yes":
        print "titos, ketel one,reyka"
                    
    elif my_brand == "no":
        print "sky is on the well"


def create_your_perfect_cocktail():
    base = choose_base()
    brand = choose_brand()




print create_your_perfect_cocktail()



if __name__ == "main":
    create_your_perfect_cocktail()