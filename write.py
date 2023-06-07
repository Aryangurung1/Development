import datetime

def sell_details_update(laptop_dictionary, valid_sn, quantity):
    """This function update the quantity of laptops sold by reducing the value of the fourth element of the dictionary
    corresponding to the given serial number by the specified quantity. then write an updated details of all laptops to a 
    file named laptop_detail.txt in the format. write each line represents the details of a single laptop, finally, close the file. 
    it contains 3 parameters laptop_dictionary, valid_sn, quantity. it doesnot return any value"""
    laptop_dictionary[valid_sn][3] = int(laptop_dictionary[valid_sn][3]) - int(quantity)
    laptop_file = open("laptop_detail.txt", "w")
    for each in laptop_dictionary.values():
        laptop_file.write(str(each[0]) + "," + str(each[1]) + "," + str(each[2]) + "," + str(each[3]) + "," + str(each[4]) + "," + str(each[5]))
        laptop_file.write("\n")
    laptop_file.close()

def create_sell_bill(customer_name, laptop_sell_details, shipping_cost):
    """This function print an invoice for the laptops sold to the customer, along with the total cost including shipping.
    it has 3 parameters : customer_name, laptop_sell_details: a list of list containing the details of laptops sold, with 
    each sublist containing the laptop name, brand name, price, quantity, and total price, shipping_cost and it doesnot return any value."""
    datetime_obj = datetime.datetime.now()
    print("-"*184)
    print("\t\t\t\t               Origin Store Pvt.Ltd.\n")
    print("\t\t\t\t          Kamalpokhari ,Kathmandu, Nepal\n")
    print("\t\t\t\t                     Invoice\n")
    print("."*184)
    print("\t\t\tCutomer Name: "+ customer_name+ "             Time: ",datetime_obj)
    print("-"*184)
    print(" SN.  \tLaptop Name     \tBrand Name        \tPrice   \tQuantity      \tTotal Price   ")
    print("-"*184)

    for i in range(len(laptop_sell_details)):
        laptop_name = laptop_sell_details[i][0]
        brand_name = laptop_sell_details[i][1]
        price = laptop_sell_details[i][2]
        quantity = laptop_sell_details[i][3]
        total_price = laptop_sell_details[i][4]
        print(" "+str(i+1)+  "\t"+laptop_name+ "\t        "+brand_name+ "\t       "+str(price)+ "\t           "+str(quantity)+ "\t         "+str(total_price) )
        print("\n")
    
    total_price_without = 0
    for i in range(len(laptop_sell_details)):
        total_price_without = total_price_without + int(laptop_sell_details[i][4])
    total_price_with = shipping_cost + total_price_without

    print("-"*184)
    print("\t\t\t\t\t\t    Total Price without shipping cost: $"+str(total_price_without))
    print("\t\t\t\t\t\t                        Shipping Cost: $"+str(shipping_cost))
    print("\t\t\t\t\t\t       Total price with shipping cost: $"+str(total_price_with))
    print("-"*184)
    print("\t\t\t\t         After Invoice cannot be refunded.")
    print("\t\t\t\tLost, stolen or damaged bill will not be replaced")
    print("\t\t\t\t              Thankyou for shopping")
    print("-"*184)



def write_sell_bill(customer, laptop_sell_details, shipping_cost):
    """The function takes in customer name, laptop sell details and shipping cost as parameter and generates an invoice in a text file. it writes
    the invoice details line by line in the file including the customer name, laptop details, total price without and with shipping cost and
    a thank you messsage."""
    datetime_obj = datetime.datetime.now()

    file_name = f"sell_invoice_{customer}_{str(datetime_obj).replace(':', '_')}.txt"
    
    laptop_file = open(file_name, "w")

    laptop_file.write("-"*184)
    laptop_file.write("\n")
    laptop_file.write("\t\t\t\t              Origin Store Pvt.Ltd.\n")
    laptop_file.write("\t\t\t\t          Kamalpokhari, Kathmandu, Nepal\n")
    laptop_file.write("\t\t\t\t                     Invoice\n")
    laptop_file.write("."*184)
    laptop_file.write("\n")
    laptop_file.write("\t\t\t\tCutomer Name: "+ customer + "         Time: "+ str(datetime_obj) + " ")
    laptop_file.write("\n")
    laptop_file.write("-"*184)
    laptop_file.write("\n")

    laptop_file.write("SN.  \tLaptop Name     \tBrand Name        \tPrice   \tQuantity      \tTotal Price   ")
    laptop_file.write("\n")
    laptop_file.write("-"*184)
    laptop_file.write("\n")

    for i in range(len(laptop_sell_details)):
        laptop_name = laptop_sell_details[i][0]
        brand_name = laptop_sell_details[i][1]
        price = laptop_sell_details[i][2]
        quantity = laptop_sell_details[i][3]
        total_price = laptop_sell_details[i][4]
        laptop_file.write( str(i+1)+  "\t "+laptop_name+     "\t"+brand_name+        "\t            "+str(price)+   "\t         "+str(quantity)+      "\t             "+str(total_price) )
        laptop_file.write("\n")
    
    total_price_without = 0
    for i in range(len(laptop_sell_details)):
        total_price_without = total_price_without + int(laptop_sell_details[i][4])
    total_price_with = shipping_cost + total_price_without

    laptop_file.write("-"*184)
    laptop_file.write("\n")
    laptop_file.write("\t\t\t\t\t\t       Total Price without shipping cost: $" +str(total_price_without))
    laptop_file.write("\n")
    laptop_file.write("\t\t\t\t\t\t                           Shipping Cost: $" +str(shipping_cost))
    laptop_file.write("\n")
    laptop_file.write("\t\t\t\t\t\t          Total price with shipping cost: $" +str(total_price_with))
    laptop_file.write("\n")
    laptop_file.write("-"*184)
    laptop_file.write("\n")
    laptop_file.write("\t\t\t\t         After Invoice cannot be refunded.\n")
    laptop_file.write("\t\t\t\tLost, stolen or damaged bill will not be replaced.\n")
    laptop_file.write("\t\t\t\t              Thankyou for shopping\n")
    laptop_file.write("-"*184)

    laptop_file.close()

def buy_details_update(laptop_dictionary, valid_sn, quantity):
    """The function takes in a dictionary containg laptop details, a valid serial number and the quantity of laptops being bought as 
    inpu. it updates the quantity of laptops in the dictionary. writes the updated laptop details to a text file and then closes the file"""
    laptop_dictionary[valid_sn][3] = int(laptop_dictionary[valid_sn][3]) + int(quantity)
    laptop_file = open("laptop_detail.txt", "w")

    for each in laptop_dictionary.values():
        laptop_file.write(str(each[0]) + "," + str(each[1]) + "," + str(each[2]) + "," + str(each[3]) + "," + str(each[4]) + "," + str(each[5]))
        laptop_file.write("\n")
    laptop_file.close()


def create_buy_bill(distributor, laptop_buy_details):
    datetime_obj = datetime.datetime.now()
    print("-"*184)
    print("\t\t\t\t               Origin Store Pvt.Ltd.\n")
    print("\t\t\t\t          Kamalpokhari ,Kathmandu, Nepal\n")
    print("\t\t\t\t                     Invoice\n")
    print("."*184)
    print("\t\t\ttManufacture Name: "+ distributor+ "             Time: ",datetime_obj)
    print("-"*184)

    print(" SN.  \tLaptop Name     \tBrand Name        \tPrice   \tQuantity      \tTotal Price   ")
    print("-"*184)

    for i in range(len(laptop_buy_details)):
        laptop_name = laptop_buy_details[i][0]
        brand_name = laptop_buy_details[i][1]
        price = laptop_buy_details[i][2]
        quantity = laptop_buy_details[i][3]
        total_price = laptop_buy_details[i][4]

        print(" "+str(i+1)+  "\t"+laptop_name+ "\t        "+brand_name+ "\t         "+str(price)+ "\t          "+str(quantity)+ "\t         "+str(total_price) )
        print("\n")
    
    total_price_without = 0
    for i in range(len(laptop_buy_details)):
        total_price_without = total_price_without + int(laptop_buy_details[i][4])
    vat_amount = total_price_without * 13/100
    total_price_with = vat_amount + total_price_without

    print("-"*184)
    print("\t\t\t\t\t\t       Total Price without Vat amount: $"+str(total_price_without))
    print("\t\t\t\t\t\t                          VAt Percent: 13%")
    print("\t\t\t\t\t\t                           Vat amount: $"+str(vat_amount))
    print("\t\t\t\t\t\t          Total price with Vat amount: $"+str(total_price_with))
    print("-"*184)
    print("\t\t\t\t         After Invoice cannot be refunded.")
    print("\t\t\t\tLost, stolen or damaged bill will not be replaced")
    print("\t\t\t\t              Thankyou for shopping")
    print("-"*184)

def write_buy_bill(distributor, laptop_buy_details):
    datetime_obj = datetime.datetime.now()
    file_name = f"buy_invoice_{distributor}_{str(datetime_obj).replace(':', '_')}.txt"
    
    laptop_file = open(file_name, "w")

    laptop_file.write("-"*184)
    laptop_file.write("\n")
    laptop_file.write("\t\t\t\t               Origin Store Pvt.Ltd.\n")
    laptop_file.write("\t\t\t\t          Kamalpokhari ,Kathmandu, Nepal\n")
    laptop_file.write("\t\t\t\t                     Invoice\n")
    laptop_file.write("."*184)
    laptop_file.write("\n")
    laptop_file.write("\t\t\tDistributor Name: "+ distributor + "             Time: "+str(datetime_obj))
    laptop_file.write("\n")
    laptop_file.write("-"*184)
    laptop_file.write("\n")
    laptop_file.write("SN.  \tLaptop Name     \tBrand Name        \tPrice   \tQuantity      \tTotal Price   ")
    laptop_file.write("\n")
    laptop_file.write("-"*184)
    laptop_file.write("\n")

    for i in range(len(laptop_buy_details)):
        laptop_name = laptop_buy_details[i][0]
        brand_name = laptop_buy_details[i][1]
        price = laptop_buy_details[i][2]
        quantity = laptop_buy_details[i][3]
        total_price = laptop_buy_details[i][4]
        laptop_file.write( str(i+1)+  "\t "+laptop_name+     "\t"+brand_name+        "\t            "+str(price)+   "\t         "+str(quantity)+      "\t         "+str(total_price) )
        laptop_file.write("\n")
    
    total_price_without = 0
    for i in range(len(laptop_buy_details)):
        total_price_without = total_price_without + int(laptop_buy_details[i][4])
    vat_amount = total_price_without * 13/100
    total_price_with = vat_amount + total_price_without

    laptop_file.write("-"*184)
    laptop_file.write("\n")
    laptop_file.write("\t\t\t\t\t\t       Total Price without VAT amount: $"+str(total_price_without))
    laptop_file.write("\n")
    laptop_file.write("\t\t\t\t\t\t                          VAt Percent: 13%")
    laptop_file.write("\n")
    laptop_file.write("\t\t\t\t\t\t                           VAT amount: $"+str(vat_amount))
    laptop_file.write("\n")
    laptop_file.write("\t\t\t\t\t\t          Total price with VAT amount: $"+str(total_price_with))
    laptop_file.write("\n")
    laptop_file.write("-"*184)
    laptop_file.write("\n")
    laptop_file.write("\t\t\t\t         After Invoice cannot be refunded.\n")
    laptop_file.write("\t\t\t\tLost, stolen or damaged bill will not be replaced.\n")
    laptop_file.write("\t\t\t\t              Thankyou for shopping\n")
    laptop_file.write("-"*184)
