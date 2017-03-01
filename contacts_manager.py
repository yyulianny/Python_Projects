import contact

def main():
    contact_list = []
    
    print "Add new contact_list:"
    first = raw_input("What is the first name? ")
    last = raw_input("What is the last name? ")
    mobile = raw_input("What is your cell number? ")
    email = raw_input("What is your email? ")

    new_contact = contact.Contact("first_name", "last_name", "mobile_number", "work_number", "email")
    contacts_list.append(new_contact)

    for new_contact in contacts_list:
        print new_contact.first_name
        print new_contact.last_name
        print new_contact.mobile_phone
        print new_contact.email


if __name__ == "__main__":
    main()