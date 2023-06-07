import message
import operation

message.login_interface()
check = True
while check == True:
    user_name = input("Enter a User name: ")
    password = input(" Enter a Password: ")
    print("\n\n\n")
    if user_name == "Aryan" and password == "Aryan123":
        #call made to fucntion of message file to show main interface
        message.interface()
        start = True
        while start == True:
            message.ask_user()
            print("\n")
            #write code here
            condition = True

            while condition == True:
                #use try and except to hadle Number Format Exception
                try:
                    admin_value = int(input("Dear Admin, Please Enter your Choice: "))
                    print("\n")
                    if admin_value <= 0 or admin_value > 3:
                        print("......................................................................")
                        print(" ")
                        print("                       Please Input 1, 2 or 3 !!                      ")
                        print(" ")
                        print(".......................................................................")
                        condition = True
                    else:
                        condition = False
                        break

                except:
                    message.invalid_value()
            #check the admin value
            if admin_value == 1:
                #call made to function of message file
                operation.sell_process()
                
            elif admin_value == 2:
                #call made to function of message file
                operation.buy_process()
            elif admin_value == 3:
                #call made to function of message file
                message.exit_system()
                start = False
                check = False
            else:
                #call made to funciton of message file
                message.invalid_value()
                start = True

    else:
        #call made to function of messsage file to show invalid message
        message.invalid_login_interface()
            

