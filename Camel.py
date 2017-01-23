
# This function prints given question number
# and also a line underneath.
def printQuestionNumber(questionNumber):
    print ("\n")
    if questionNumber == 4:
        print ("This is Question #" + str(questionNumber) + " and #" + str(questionNumber+1))
    else :
        print ("This is Question #" + str(questionNumber))
    print("------------------------")
pass


def firstQuestion():
    printQuestionNumber(1)
    if "Naz" > "Yenny":
        print "My name is greater!"
    elif "Yenny" > "Naz":
        print "Their name is greater."
    else:
        print "Our name is equal!"
pass


def lastQuestion():
    printQuestionNumber(13)
    favoriteColor = raw_input("what is your favorite color: ")
    if (favoriteColor.upper() == "BLUE"):   
        print "My color is primary color"
    elif (favoriteColor.upper() == "YELLOW"): 
        print "My color is primary color"
    elif (favoriteColor.upper() == "RED"): 
        print "My color is primary color"
    else:
        print "My favorite color is a secondary color"
pass

def secondQuestion():
    printQuestionNumber(2);
    today = 12
    if (31/2) < today:
        print "oh, we're halfway there!"
    else:
        print "The month is still young"
pass 







userQuestionNumber = input("Which question do you want to see? [1, 2 or 3]")

if (userQuestionNumber == 1):
    firstQuestion()

elif (userQuestionNumber == 2):
    secondQuestion()

else :
    lastQuestion()
