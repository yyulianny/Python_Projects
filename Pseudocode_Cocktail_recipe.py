
def intro():
    print ("\n" * 50)
    print 'what is your name? ',
    name = raw_input()

    print "Welcome %r!" %(name)
    
    print 'would you like to play a game? [Y or N] ',
    play_or_no = raw_input()

    if (play_or_no.upper() == "Y") or (play_or_no.upper() == "YES") :
        start_game()
    else:
        print "goodbye %r" %(name)
    pass



def start_game():
    list_of_items = ['vodka', 'gin', 'tequila', 'rum', 'whiskey', 'lime', 'lemon', 
                    'pineapple', 'cranberry', 'ginger beer', 'grapefruit', 'orange juice', 
                    'sugar', 'syrup', 'sweet vermout', 'campari', 'bitters', 'mint', 
                    'cherry', 'sugar', 'salt', 'orange peel', 'olives', 'onions', 'coke',
                    'tonic', 'sprite', 'triplesec', 'sweet and sour']

    print ("\n" * 50)
    print "here the list of items"
    print "----------------------"
    
    count = 1
    for item in list_of_items:
        print count,
        print item
        count = count + 1
    
    get_user_items()    

    pass


def get_user_items():
    print ("\n")
    print "pick five items from the list"
    
    jack_and_coke = ['jack', 'coke']
    margarita = ['tequila', 'triplesec', 'limejuice', 'sweet and sour']


    print 'item #1: ',
    item1 = raw_input()

    print 'item #2: ',
    item2 = raw_input()

    print 'item #3: ',
    item3 = raw_input()

    print 'item #4: ',
    item4 = raw_input()

    print 'item #5: ',
    item5 = raw_input()

    for count in range(5)
        if(count == 0):
            # do something with item 1   
            
        elif(count == 1):
            # do something with item 2     



#intro()
start_game()