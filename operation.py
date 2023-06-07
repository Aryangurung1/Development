import read
import write
import message
import validity

def sell_process():
    """This function allows the user to sell laptops by taking details of the laptop from the use, calculating the total cost, and generating an invoice for the customer. the 
    function ueses while loop to keep asking the user if htey want to sell more laptops until the user chooses to exit. it then prompts the user for their name, genrates an invoice using create_sell_bill and write the invoice to a file using write_sell_bill
    it doesnot take any parameter and doesnot return any value."""
    laptop_sell_details = []
    shipping_cost = 1000
    #use while loop

    check = True
    while check == True:
        print("\t\t\t\t\t\t\t\t\t       You are in Sell mode sytem")
        print("\t\t\t\t\t\t\t\t\t     -----------------------------")
        valid_serial_number = validity.valid_sn()
        laptop_dictionary = read.add_details()
        valid_quantity = validity.valid_quantity(valid_serial_number, laptop_dictionary)
        laptop = laptop_dictionary[valid_serial_number][0]
        brand = laptop_dictionary[valid_serial_number][1]
        price = laptop_dictionary[valid_serial_number][2]
        new_price = price.replace("$", "")
        total_price = float(new_price) * valid_quantity
        laptop_used = False
        if len(laptop_sell_details) > 0:
            for i in range(len(laptop_sell_details)):
                if laptop in laptop_sell_details[i]:
                    
                    laptop_used = True
                    break

        if laptop_used == False:
            laptop_sell_details.append([laptop, brand, price, valid_quantity, total_price])
        else:
            laptop_sell_details[i][3] = valid_quantity + laptop_sell_details[i][3]
        
        again = True
        while again == True:
            user_choice = input("Do you want to sell any more please enter 'Y' for yes and 'N' for no: ")
            if user_choice == 'Y':
                check=True
                break

            elif user_choice == 'N':
                #ask customer name
                customer = input("May I have the pleasure of knowing customer name?: ").upper()
                    
                print("\n")
                print("Thank you so much Mr/Mrs. "+ customer + " for purchasing the laptop. The invoice is provided below.")
                write.create_sell_bill(customer, laptop_sell_details, shipping_cost)
                write.write_sell_bill(customer, laptop_sell_details, shipping_cost)
                again = False
                check = False
                
            else:
                message.invalid_value()

def buy_process():
    """This function allows the user to buy laptops by taking details of the laptop from the user, calculating the total cost, and generating an invoice for the distributor.
    it uses a while loop to keep asking the user if they wnat to buy more laptops until the user chooses to exit. it then prompts the user for the distributor name, generates an invoice using create_buy_bill and writes the invoice to file using write_buy_bill. it doesnot have any paramter 
    and deosnot return any value."""
    laptop_buy_details = []
    #use while loop
    check = True
    while check == True:
        print("\t\t\t\t\t\t\t\t\t       You are in Buy mode sytem")
        print("\t\t\t\t\t\t\t\t\t     -----------------------------")
        valid_serial_number = validity.valid_sn()
        laptop_dictionary = read.add_details()
        valid_quantity = validity.valid_buy_quantity(valid_serial_number, laptop_dictionary)

        laptop = laptop_dictionary[valid_serial_number][0]
        brand = laptop_dictionary[valid_serial_number][1]
        price = laptop_dictionary[valid_serial_number][2]
        new_price = price.replace("$", "")
        total_price = float(new_price) * valid_quantity
        
        laptop_used = False
        if len(laptop_buy_details) > 0:
            for i in range(len(laptop_buy_details)):
                if laptop in laptop_buy_details[i]:
                    
                    laptop_used = True
                    break

        if laptop_used == False:
            laptop_buy_details.append([laptop, brand, price, valid_quantity, total_price])
        else:
            laptop_buy_details[i][3] = valid_quantity + laptop_buy_details[i][3]

        again = True
        while again == True:
            user_choice = input("Do you want to buy any more please enter 'Y' for yes and 'N' for no: ")
            if user_choice == 'Y':
                check=True
                break

            elif user_choice == 'N':
                
                #ask distributor name
                distributor = input("May I have the pleasure of knowing the name of Distributor?: ").upper()

                print("\n")
                print("Thank you so much Mr/Mrs. "+ distributor + " for selling the laptop.\n \t\t\t the invoice is provided below.")
                write.create_buy_bill(distributor, laptop_buy_details)
                write.write_buy_bill(distributor, laptop_buy_details)
                again = False
                check = False
                            
            else:
                message.invalid_value()
        

            

            



