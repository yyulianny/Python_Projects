# from pdb import set_trace
# set_trace()

#quetion 4 and 1
def parser(text,tax):
    split_data = text.split(",")
    quantity = int(split_data[1].split(":")[1])
    price = float(split_data[2].strip().split(":")[1])
    item = str(split_data[0]).strip().split(":")[1]
    #print "The item is " + item
    subtotal = price * quantity
    total = subtotal * tax
    return total
    #print "the total price is " + str(total)


# # PART 2
# #quetion 1
# my_name = "yenny"
# new_name = list(my_name)
# print new_name


# #quetion 2
# #turning string into a list of integers using. split() method
# string = "1,2,3,4,5"
# new_string = string.split(",")
# print new_string


# #question 2,a
# print "".join(['s', 't', 'r', 'i', 'n', 'g'])

# # string = "1","2","3","4","5"
# print "".join(['1', '2', '3', '4', '5', '6'])


# #quetion 3
# string_fish = "One fish two fish red fish blue fish"
# replace_fish = string_fish.replace(" fish","")
# print replace_fish
# split_fish = replace_fish.split(" ")
# print split_fish


#quetion 3,a
# string_yo = "One fish two fish red fish blue fish"
# replace_yo = int(string_yo.replace(" one", "two", ""))
# print replace_yo
# split_yo = replace_yosplit(" ")
# print split_yo


#quetion 4
# grocery_string = "item:apples,quantity:4,price:1.50\n"
# split_data = grocery_string.split(",")

# quantity = int(split_data[1].split(":")[1])
# price = float(split_data[2].strip().split(":")[1])
# item = str(split_data[0]).strip().split(":")[0]
# print "The bill is " + str(quantity * price)



# #quetion 5
# grocery_list = ["item:apples,quantity:4,price:1.50\n",
#                 "item:pears,quantity:5,price:2.00\n",
#                 "item:cereal,quantity:1,price:4.49\n"]

# total = 0
# for thing in grocery_list:
#     name = thing.split(',')
#     list_q = name[1].split(':')
#     quantity = int(list_q[1])
#     list_p = name[2].split(':')
#     price = float(list_p[1])
#     total +=  quantity*price
# print total


#grocery_string = "item:oranges,quantity:42,price:2.70\n"
#sales_tax = 1.0875
#total_price = parser(grocery_string, sales_tax)
#print total_price

blah = "blah blah blah"
# print blah
print "blah blah blah"

