
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


def question1():
    printQuestionNumber(1)
    if "Naz" > "Yenny":
        print "My name is greater!"
    elif "Yenny" > "Naz":
        print "Their name is greater."
    else:
        print "Our name is equal!"
pass



printQuestionNumber(2);
today = 12
if (31/2) < today:
    print "oh, we're halfway there!"
else:
    print "The month is still young"


printQuestionNumber(3)
today = "Wednesday"
if today == "Monday":
    print "Yasss Monday! Here we go!!"
elif today == "Tuesday":
    print "Sigh, its only Tuesday!!"
elif today == "Wednesday":
    print "Humpday!"
elif today == "Thursday":
    print "#Almost there!!"    
elif today == "Friday":
    print "TGIF!"    
else :
    print "Yeah, it is the weekend!!"


printQuestionNumber(4)
age = 31
if age >= 18:
    print "Yay! I can vote!"
else:
    print "Awww, I cannt vote"


printQuestionNumber(6);
age = input("How old are you? ")
if (age >= 18) and (age >= 21):
    print "I can vote and go to a bar!"


printQuestionNumber(7)
age = input("How old are you? ")
if (age >= 21):
    print "I can go to a bar."
elif (age >= 18) and (age < 21):
    print "I can vote but I cannot go to a bar"
else:
    print "I cannot vote or go to a bar"


printQuestionNumber(8)
number = input("What number do you want to check: ")
if ((number % 2)==0):
    print "Number " + str(number) + " is even"
else:
    print "Number " + str(number) + " is odd"

printQuestionNumber(9)
number1 = input("What is the first number: ")
number2 = input("What is the second number: ")

if ((number1 % 2)==0) and ((number2 % 2)==0):
    print "Both numbers are even"
else:
    print "Both number are not even"

