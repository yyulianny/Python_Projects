# Exercises part 1
class Contact(object):
        def __init__(self, first_name, last_name, mobile_number, work_number, email):
                self.first_name = first_name
                self.last_name = last_name
                self.mobile_number = mobile_number
                self.work_number = work_number
                self.email = email
        

        def send_text(self, message):
            if self.mobile_number != "":
                print "To: %s - %s" % (self.mobile_number.message)
            else:
                print "no mobile_number"


contact_Yenny = Contact("Yenny", "Yulianny", 4155332131, 666666666, "yyulianny@yahoo.com")
new_contact = Contact("Heracleo", "Franco", 4157283367, 999999999, "franco@blahblah.com")
print contact_Yenny
print contact_Yenny.last_name
print contact_Yenny.mobile_number
print contact_Yenny.send_text
print new_contact.email
print new_contact.last_name


# Exercises part 2
def main():
    contact_list = []

    contact_one = Contact("Yenny", "Yulianny", "" , 666666666, "yyulianny@yahoo.com")
    contact_two = Contact("Kyoko", "Takashima", 4155332131, 666666666, "test@test.com")
    contact_three = Contact("Pumpkin", "Pie", 4155332131, 666666666, "Pumpkin@blahblah.com")

    contact_list.append(contact_one)
    contact_list.append(contact_two)
    contact_list.append(contact_three)

    #to print the contact list
    for contact in contact_list:
        print contact.first_name.last_name.mobile_number.work_number.email

    #send text to contact_list
    for contact in contact_list:
        contact_list.send_text("how are you?")



if __name__ == "__main__":
    main()