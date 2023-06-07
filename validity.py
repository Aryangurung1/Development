import read
import message
import write
def valid_sn():
    """This function checks if a user-provided serial number for a laptop is valid or not. it does this by calling the read.laptop_deatils() funtion,
    which likely reads in details about laptops from source. it then prompts the user to enter a SN number and checks if the number is between 1 and the length of the list returned by read.add_details()
    if the user-provided SN is not valid, it prints an error message and prompts the user to enter another value. if the user provides an invalid user , it calls message.invalid_value function to display error messagae.
    once a valid SN is provided, it prints a success message and retruns the valid SN."""
    read.laptop_details()
    print("\n")
    sn_check = True
    while sn_check == True:
        try:
            valid_serial_number = int(input("Please enter a SN number of Laptop: "))
            if valid_serial_number <= 0 or valid_serial_number > len(read.add_details()):
                print("\n")
                print("\t\t\t\t\t\t\t\t  *******************************************************")
                print(" ")
                print("\t\t\t\t\t\t\t\t    Error:\n \t\t\t\t\t\t\t\t           Your provided SN",valid_serial_number, "is not valid")
                print(" ")
                print("\t\t\t\t\t\t\t\t  *******************************************************")
                print("\n")
            else:
                print("\t\t\t\t\t\t\t\t ***********************************************************")
                print(" ")
                print("\t\t\t\t\t\t\t\t\t   ",valid_serial_number, "is a valid Serial Number of Laptop")
                print(" ")
                print("\t\t\t\t\t\t\t\t ***********************************************************")
                sn_check = False
        except:
            message.invalid_value()
    read.laptop_details()
    return valid_serial_number

def valid_quantity(valid_serial_number, laptop_dictionary):
    """This function takes in two parameters valid_serial_number and laptop_dictionary. the first parameter is the valid serial number of a laptop, and the second parameter is a dictionary containing details about laptops.
    it prompts the user to enter a quantity of laptops to sell and checks if the quantity entered is valid or not. if the user provided quantity is not vaid, it prints an error message and prompts the user to enter antother value.
    once a valid quantity is provided, it prints a success message, updates the sell details for the laptop in the laptop_dictionary using the write.sell_details_update() function, and returns the quantity"""
    available_quantity = int(laptop_dictionary[valid_serial_number][3])
    quantity_check = True
    while quantity_check == True:
        try:
            quantity = int(input("Enter a valid quantity of laptop to sell: "))
            print("\n")
            if quantity > available_quantity or quantity <= 0:
                print("\n")
                print("\t\t\t\t\t\t\t\t   *********************************************************")
                print(" ")
                print("\t\t\t\t\t\t\t\t     Error:\n \t\t\t\t\t\t\t             The quantity you provided",quantity, "is not valid.")
                print(" ")
                print("\t\t\t\t\t\t\t\t   *********************************************************")
                print("\n")
            else:
                print("\t\t\t\t\t\t\t\t   ********************************************************")
                print(" ")
                print("\t\t\t\t\t\t\t\t\t            ",quantity, "quantity is available")
                print(" ")
                print("\t\t\t\t\t\t\t\t   *********************************************************")
                print("\n")
                quantity_check = False
        except:
            message.invalid_value()
    write.sell_details_update(laptop_dictionary, valid_serial_number, quantity)
    return quantity

def valid_buy_quantity(valid_serial_number, laptop_dictionary):
    """This function prompts the user to enter a valid quantity of laptops to buy and updates the details of the purchase in the laptop_dictionary. it takes in two parameters
    valid_symbol_number, laptop_dictionary. The function first checks if the entered quantity is valid or not. if the quantity is less than or equal to zero, an error message is displayed, and the user is prompted to
    enter a valid quantity. if the quantity is valid, it is added to the system and the function calls another function write.buy_details_update() to update the laptop_dictionary with the purchase details.
    if the user enters an invalid value, the function calls another function message.invalid_value() to display an appropriate error message.
    the funtion retruns the valid quantity entered by the user."""
    quantity_check = True
    while quantity_check == True:
        try:
            quantity = int(input("Enter a valid quantity of laptop to buy: "))
            print("\n")
            if quantity <= 0:
                print("\n")
                print("\t\t\t\t\t\t\t\t  *******************************************************")
                print(" ")
                print("\t\t\t\t\t\t\t\t    Error:\n \t\t\t\t\t\t\t\t           Quantity you provided",quantity, "is not valid")
                print(" ")
                print("\t\t\t\t\t\t\t\t  *******************************************************")
                print("\n")
            else:
                print("\t\t\t\t\t\t\t\t **********************************************************")
                print(" ")
                print("\t\t\t\t\t\t\t\t\t        ",quantity, "quantity is available")
                print(" ")
                print("\t\t\t\t\t\t\t\t ***********************************************************")
                print("\n")
                quantity_check = False
        except:
            message.invalid_value()
    write.buy_details_update(laptop_dictionary, valid_serial_number, quantity)
    return quantity

