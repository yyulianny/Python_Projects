
#part 2 for loops
#question number 1:
'''
for item in range(0,21):
    print item

#question number 2:
for item in range(0,21):
    if item == 13:
        print "hello"
    else:
        print item,


#part 3 for loops
#question number 1:
list_fruits = ("apples", "oranges", "bananas")
for fruits in list_fruits:
    print list_fruits,


#question number 2:
list_fruits = ("apples", "oranges", "bananas")
for fruits in range(len(list_fruits)):
    print list_fruits[fruits],

'''
# function starts here
def sum_nums(bunch_of_numbers):
    sum = 0
    # for loop starts here
    for item in bunch_of_numbers:
        sum = sum + item
    # for loop ends here
    print sum
# function ends here


#part 4 for loops
#question number 1:
my_list = [1,3,6,12,10,23]

sum_nums(my_list)




