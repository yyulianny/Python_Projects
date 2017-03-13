def intro():
    import os
    os.system('clear')

    name = raw_input("What is your name? ")

    again = False
    print "Welcome %r!" % name
    
    print "Would you like to play a game? [Y or N] ",
    play_or_no = raw_input()
    if (play_or_no.upper() == "Y") or (play_or_no.upper() == "YES") : 
        again = True
    else:
        print "goodbye %r" % name
    


    while (again == True):
        start_game(name)

        print "Would you like to play a game? [Y or N] ",
        play_or_no = raw_input()

        if (play_or_no.upper() == "Y") or (play_or_no.upper() == "YES") : 
            again = True
        else :
            again = False
            print "goodbye %r" % name








def start_game(user_name):
    list_of_items = ['vodka', 'gin', 'tequila', 'rum', 'whiskey', 'lime', 'coke',
                    'lemon','pineapple juice', 'cranberry juice', 'ginger beer', 
                    'syrup', 'sweet vermouth', 'campari', 'bitters', 'mint',
                    'cherry', 'sugar', 'salt', 'orange peel', 'olives juice', 'onions', 
                    'sprite', 'triple sec', 'sweet and sour', 'orange', 'orange juice',
                    'tonic', 'grapefruit juice', 'dry vermouth', 'lime juice',
                    'soda water']

    print
    print "here the list of items"
    print "----------------------"
    
    #for index in range(len(list_of_items)):
    #for index, items in 1(list_of_items):
    
    
    for x in range(len(list_of_items)):
        print str(x+1) + ". " + list_of_items[x]
    
    get_user_items(user_name, list_of_items)   

    pass






def convert_int_to_string(number):
        if(number == 0):
            return "zero"
        elif(number == 1):
            return "one"
        elif(number == 2):
            return "two"
        elif(number == 3):
            return "three"
        elif(number == 4):
            return "four"
        else:
            pass







def get_user_items(user_name, list_of_drinks):
    print ("\n")

    print "pick five items from the list and create at least four drinks"

    drinks = {
        "jack and coke": ["whiskey", "coke"], 
        "rum and coke": ["rum", "coke"], 
        "vodka cranberry": ["vodka", "cranberry juice"],
        "greyhound" : ["vodka", "grapefruit juice"],
        "lemon drop" : ["vodka", "triple sec", "sweet and sour"],
        "cosmopolitan" : ["vodka", "triple sec", "lime juice", "cranberry juice"],
        "kamikaze" : ["vodka", "triple sec", "lime juice"],
        "moscow mule" : ["vodka", "ginger beer", "lime juice"],
        "tom collins" : ["gin", "sweet and sour", "soda water"],
        "john collins" : ["whiskey", "sweet and sour", "soda water"],
        "gimlet" : ["gin", "lime juice"],
        "negroni" : ["gin", "sweet vermouth", "campari"],
        "bay breeze" : ["vodka", "pineapple juice", "cranberry juice"],
        "sea breeze" : ["vodka", "grapefruit juice", "cranberry juice"],
        "martini" : ["gin", "dry vermouth"],
        "dirty martini" : ["gin", "dry vermouth", "olive juice"],
        "margarita" : ["tequila", "triple sec", "lime juice", "sweet and sour"],
        "dark and stormy" : ["rum", "lime juice", "ginger beer"],
        "mojito" : ["rum", "mint", "sugar", "lime juice", "soda water"],
        "manhattan" : ["whiskey", "sweet vermouth", "bitters"],
        "dry manhattan" : ["whiskey", "dry vermouth", "bitters"],
        "perfect manhattan" : ["whiskey", "dry vermouth", "sweet vermouth", "bitters"],
        "old fashion" : ["cherry", "sugar", "orange", "whiskey"],
        "fruit punch" : ["orange juice", "pineapple juice", "cranberry juice"],
    }

    my_ingredients = []

    for x in range(5):
        print "item #" + str(x+1),
        some_items = raw_input().lower()

        try: 
            index = int(some_items) - 1
            my_ingredients.insert(x, list_of_drinks[index])
        except ValueError:
            my_ingredients.insert(x, some_items)
        
    
    match_key = []
    match_value = []

    count = 0

    print
    for key, value in drinks.items():  
    # for key, value in dict.drinks.items():
        match = list(set(my_ingredients) & set(value))
    
        if len(match) == len(value):
            count = count + 1
            match_key.append(key)        
            match_value.append(value)

    if len(match_key) != 0:
        print "Good job " + user_name + ", you can make " + convert_int_to_string(count) + " drinks"
    else:
        print "you can try it again!"

    for index in range(len(match_key)):
        print "-------------------------"
        print "Drink: " + match_key[index] 
        print "Ingredients: ", 
        print match_value[index]
        print "-------------------------"
        print "\n"


     

intro()
