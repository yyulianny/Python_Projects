
def intro():
    print ("\n" * 50)
    print "What is your name? ",
    name = raw_input()

    print "Welcome %r!" %(name)
    
    print "would you like to play a game? [Y or N] ",
    play_or_no = raw_input()

    if (play_or_no.upper() == "Y") or (play_or_no.upper() == "YES") : 
        start_game(name)
    else:
        print "goodbye %r" %(name)
    pass





def start_game(userName):
    list_of_items = ['vodka', 'gin', 'tequila', 'rum', 'whiskey', 'lime', 'coke',
                    'lemon','pineapple juice', 'cranberry juice', 'ginger beer', 
                    'sugar', 'syrup', 'sweet vermout', 'campari', 'bitters', 'mint',
                    'cherry', 'sugar', 'salt', 'orange peel', 'olives juice', 'onions', 
                    'sprite', 'triple sec', 'sweet and sour', 'orange', 'orange juice',
                    'tonic', 'grapefruit juice', 'dry vermout', 'lime juice',
                    'soda water']


    print ("\n" * 50)
    print "here the list of items"
    print "----------------------"
    
    count = 1
    for item in list_of_items:
        print count,
        print item
        count = count + 1
    
    get_user_items(userName)   

    pass






def get_user_items(userName):
    print ("\n")

    print "pick five items from the list"

    drinks = {
        "jack_and_coke": ["whiskey", "coke"], 
        "vodka_cranberry": ["vodka", "cranberry juice"],
        "greyhound" : ["vodka", "grapefruit juice"],
        "lemon_drop" : ["vodka", "triplesec", "sweet and sour"],
        "cosmopolitan" : ["vodka", "triple sec", "lime juice", "cranberry juice"],
        "kamikaze" : ["vodka", "triple sec", "lime juice"],
        "moscow_mule" : ["vodka", "ginger beer", "lime juice"],
        "tom_collins" : ["gin", "sweet and sour", "soda water"],
        "john_collins" : ["whiskey", "sweet and sour", "soda water"],
        "gimlet" : ["gin", "lime juice"],
        "negroni" : ["gin", "sweet vermout", "campari"],
        "bay_breeze" : ["vodka", "pineapple juice", "cranberry juice"],
        "sea_breeze" : ["vodka", "grapfruit juice", "cranberry juice"],
        "martini" : ["gin", "dry vermout"],
        "dirty_martini" : ["gin", "dry vermout", "olive juice"],
        "margarita" : ["tequila", "triple sec", "limejuice", "sweet and sour"],
        "dark_and_stormy" : ["rum", "lime juice", "ginger beer"],
        "mojito" : ["rum", "mint", "sugar", "lime juice", "soda water"],
        "manhattan" : ["whiskey", "sweet vermout", "bitters"],
        "dry_manhattan" : ["whiskey", "dry vermout", "bitters"],
        "perfect_manhattan" : ["whiskey", "dry vermout", "sweet vermout", "bitters"],
        "old_fashion" : ["cherry", "sugar", "orange", "whiskey"]
    }


    print "item #1: ",
    item1 = raw_input()

    print "item #2: ",
    item2 = raw_input()

    print "item #3: ",
    item3 = raw_input()

    print "item #4: ",
    item4 = raw_input()

    print "item #5: ",
    item5 = raw_input()

    my_ingredients = [item1, item2, item3, item4, item5]

    # for count in range(5):
    #     if(count == 0):
    #         # do something with item 1 
    #         print count,
    #         print item
    #         count = count + 1 

        
    #     elif(count == 1):
    #         # do something with item 2
    #         pass


    print ""
    for key, value in dict.items(drinks):
        match = list(set(my_ingredients) & set(value))
    
        if(len(match) == len(value)):
            print "Good job " + userName + ", you found this drink: -->  " + key 
            print value


intro()
