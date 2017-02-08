Homework Challenges

Lists Practice - Solution

def should_you_eat_the_bacon():
        angels_question = raw_input("do you wnat to feel like angels are frolicking on your taste buds? Y or N:")
        if angels_question == "Y":
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
Loops Practice - Solution

3 ways to add two items to a list of two
class_room.append("PCs")
class_room.append("snacks")
class_room + ["PCs"]
class_room + ["snacks"]
class_room.insert(2, "PCs")
class_room.insert(3, "snacks")
Remove the item located at index 1 (Can you find 3 different ways?)
class_room.remove("projector")
Remove the item 'snacks'
class_room.remove("snacks")
More Loops problems

Set 1 - solutions

Write a program that will ask the user for a message and the number of times they want that message displayed. Then output the message that number of times.
def message_multiplyer():
        message = raw_input("what is your message?")
        multiplyer = int(raw_input("how many times would you like to see your message?"))
        return message*multiplyer


print message_multiplyer()
Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
def seven_and_five():
        for num in range(1500, 2701):
                if num%7==0 and num%5==0:
                        print num

print seven_and_five()
Given: Two positive integers a and b (a<b<15000). [you could probably change the number here]
def sum_numbers(a, b):
        sum = 0
        for number in range(a, b+1):
                sum = sum + number
        return sum

print sum_numbers(3, 5)
mega challenges:
write program that validates that a user has input a valid email address, and doesn't let a person continue until a valid email address is entered
for example :" melissa@hackbrightacademy.com" is valid and "melissa@hackbrightacademy" or" @hackbrightacademy.com" is not valid.
def check_email():
        check_valid = True
        while check_valid:
                addressToVerify = raw_input("what is your email address?")
                match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

                if match == None:
                        print "invalid email address, try again!"
                else:
                        print "congrats, you're address is correct!"
                        check_valid = False

print check_email()
Extra Challenge - no solution yet

Good luck!