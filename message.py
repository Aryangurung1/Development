#function to create first login interface
def login_interface():
    """This function, prints a login interface for an admin panel of the Origin Store
    it includes a header displaying the name of the store this function doesnot take any parameters
    and it also doesnot Return any value"""
    print("\n")
    print("-"*184)
    print(" ")
    print("\t\t\t\t\t\t\t\t\t\t**The Origin Store**\n \t\t\t\t\t\t\t   Enter Correct User name and Password to enter into admin panel")
    print(" ")
    print("-"*184)


#create function to create a invalid login message
def invalid_login_interface():
    """This function prints an interface to indicate that the login credentials entered by the
    user are invalid and prompts the user to enter the correct login details. it doesnot have any parameters and doesnot return any value"""
    print("-"*184)
    print(" ")
    print("\t\t\t\t\t\t\t  !Sorry Invalid User name or Password. Please enter correct value")
    print(" ")
    print("-"*184)


#function to create main interface
def interface():
    """This function prints an interface for the admin panel of the Origin Store. it inclues a header displaying the name of the store, its slogan,
    contact information and location. it also includes a welcome message for the user and a brief description of the privileges thta come with being an admin 
    of the store. it doesnot have any parameter and doesnt return any value."""
    print("\n")
    print("-"*184)
    print(" ")
    print("\t\t\tThe Origin Store  \t\t\t Dream.Dare.Inspire \t\t\tContact: 98421233 \t\t\t Kathmandu")
    print(" ")
    print("-"*184)
    print(" ")
    print("\t\t\t\t\t\t\tWelcome to the admin panel of our store! As an admin, you have the privilege of\n \t\t\t\t\t\tbeing able to operateat every level of our business,from sourcing and purchasing products to\n \t\t\t\t\t\t\t\t           managing inventory and processing orders.")
    print(" ")
    print("\t\t\t\t OUR SERVICES: \t\t Laptop & Desktops \t\t PC Components \t\t Accessories \t\t PC Builder")
    print(" ")
    print("."*184)


def ask_user():
    """This function prints a prompt for the user to select from the available options. it inclues three options to choose from by entering 1,2,3 to operate the buy system, 
    sell system or exit from the system repectively. it doesnot have any parameter and it doesnot return any value"""
    print(" ")
    print(" -> Enter 1 to Operate Sell System.\n -> Enter 2 to operate Buy System.\n -> Enter 3 to Exit from the system.")
    print(" ")
    print("-"*184)


#create a funtion for invalid input
def invalid_value():
    """This function prints an interface to indicate that the user has entered an invalid value. it includes a message that the user has entered an invalid input and prompt the user to enter the correct input.
    it doesnot have parameters and it doesnot return any value"""
    print("\n")
    print("\t\t\t\t\t\t\t\t************************************************************")
    print(" ")
    print("\t\t\t\t\t\t\t\t     Sorry! Invalid Input, please enter correct value")
    print(" ")
    print("\t\t\t\t\t\t\t\t************************************************************")
    print("\n")

#create a function to show message for exit system
def exit_system():
    """This function prints an interface to indicate that the user has exited the sytem. it includes a message thanking the admin for using the system and wishing them a good day.
    it doesnot have any paramters and doesnot return any vlaue"""
    print("-"*184)
    print(" ")
    print("\t\t\t\t\t\t\t\t\tThank you for using the system. Have a good day!\n \t\t\t\t\t\t\t          If you experience any problem please contact us at 92732343")
    print(" ")
    print("-"*184)



