#create a function to read laptop details file and show in terminal
def laptop_details():
    """This funtion prints the details of the laptops availabel in store. it includes the header 
    displaying the name of the store. the details of the laptops availabel in the store are displayed in tabular form, including the serial Number, laptop name
    Brand Name, Price, Quantity, Processor, and Graphics Card. this funtion opens a text file named laptop_details.txt to retrieve the details of the laptops and
    prints them in the desired format. it doesnot have any parameters and doesnot return any value."""
    print("."*184)
    print("\t\t\t\t\t\t    The Origin Store")
    print("-"*184)
    print("SN.  \tLaptop Name     \tBrand Name        \tPrice   \tQuantity      \tProcessor        \tGraphics Card  ")
    print("-"*184)
    laptop_file = open("laptop_detail.txt", "r")
    number = 1
    for laptop in laptop_file:
        print(number, "\t" + laptop.replace(",", "\t\t"))
        number = number +  1
        print("-"*184)
    laptop_file.close()


#create a function to store all the file details in dictionary
def add_details():
    """This funciton read the details of the laptops from a .txt file named laptop_detail.txt and creates a dictinary containing the details.
    the funtion reads each line of the file, which contains the details of a laptop, and removes the newline character at the end. it then splits the using the comman 
    as a delimiter to obtain a list of valuees for the different values of the laptop. these values stored in a dictionary with a unique Id as the key, and the laptop values as the value, finally, the funtion returns a
    dictionary containing the details of the laptops but it doesnot have any parameters."""
    laptop_file = open("laptop_detail.txt", "r")
    laptop_dictionary = {}
    unique_id = 1
    for laptop in laptop_file:
        laptop = laptop.replace("\n", "")
        laptop_dictionary.update({unique_id: laptop.split(",")})
        unique_id = unique_id + 1
    print("\n")
    laptop_file.close()
    return laptop_dictionary



