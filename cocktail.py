

def create_your_perfect_cocktail():
    my_base = raw_input("please choose your base ")
    if (my_base == ("vodka", "gin", "tequila", "rum", "whiskey")):
        print "sounds great!, lets go to the next step"
        
        my_brand = raw_input("any any brand preference? yes or no: ")
            if (my_brand == ("yes")):
                print "titos", "ketel one", "reyka"
                    
            elif my_brand == "no":
                print "sky is on the well"

    elif my_base != ("vodka", "gin", "tequila", "rum", "whiskey"):
        return "please try it again!"

print create_your_perfect_cocktail()
