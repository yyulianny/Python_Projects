# This function prints options menu and
# finds out what user wants to do and returns 
# choice.
def get_user_choice():
    print "" #empty line
    print "OPTIONS"
    print "------------------"
    print "1) Calculate Tip"
    print "2) Split the bill"
    print "------------------"
    choice = input("Please enter your choice: ")
    return choice

# This function calculates the tip and prints
# the result
def calculate_tip():
    billAmount = input("enter bill amount ")
    tipPersentage = input("how much tip Persentage ")
    billAmount * tipPersentage /100
    print billAmount * tipPersentage /100

def split_the_bill():
    totalBillAmount = input("enter total bill ")
    numberofGuest = input("how many number of Guest? ")
    print totalBillAmount / numberofGuest
   


# ----------------------------------------------
def main():
    whatUserWants = get_user_choice()

    if (whatUserWants == 1):
        calculate_tip()

    else:
        split_the_bill()

if __name__ == "__main__":
    main()

