customer = {}  # dictionary for customer
item = {}  # dictionary for item
sales = {}  # dictionary for sales
sale_id = [1]


def main_menu():  # define main menu
    print("=" * 45)  # to print a separating line
    print(" \U0001F49A", " WELCOME TO BAKERY MANAGEMENT SYSTEM ", "\U0001F49A")  # welcome message to user
    print("=" * 45)  # to print a separating line
    choice = 0  # so the loop executes
    while choice != 4:  # loop to execute until choice=4
        while True:  # exceptional handling
            try:
                choice = eval(input("Enter your Choice: \n 1.Item Record 2.Customer Record 3.Sales Record 4.Exit: "))
                # input for choice
            except:
                print("Invalid Input")
                continue  # to continue loop so that invalid input isn't printed twice
            if choice == 1:
                item_menu()  # calling item menu
                print("=" * 85)
            elif choice == 2:
                customer_menu()  # calling customer menu
                print("=" * 85)
            elif choice == 3:
                sales_menu()  # calling sales menu
                print("=" * 85)
            elif choice == 4:
                break  # to exit loop
            if choice > 4 or choice < 0:  # for any invalid inputs
                print("Invalid Input")
    print("*" * 40)
    print("\U0001F49A", "  BAKERY MANAGEMENT SYSTEM EXITED ", "\U0001F49A")  # exiting message for the user
    print("*" * 40)

def item_menu():  # defining item menu function
    print("=" * 85)
    print("ITEM MENU SECTION")  # message to show which menu user is on
    print("." * 20)
    choice = 0
    while choice != 6:  # loop to run until choice=6
        while True:  # exceptional handling
            try:
                choice = eval(input("Enter Your Choice: \n 1.Add Record 2.View Record 3.Edit Record 4.Search Record 5. Delete Record 6.Exit: "))  # input for choice
                break  # to exit loop
            except:
                print("Invalid Input")
                continue  # to continue loop so that invalid input isn't printed twice
        if choice == 1:
            add(1)  # calling add function with y=1
        elif choice == 2:
            view(1)  # calling view function with y=1
        elif choice == 3:
            edit(1)  # calling edit function with y=1
        elif choice == 4:
            search(1)  # calling search function with y=1
        elif choice == 5:
            delete(1)  # calling delete function with y=1
        elif choice > 6 or choice < 0:  # for any invalid inputs
            print("Invalid Input")


def customer_menu():  # defining customer menu
    print("=" * 85)
    print("CUSTOMER MENU SECTION")  # message to show which menu user is on
    print("." * 25)
    choice = 0
    while choice != 6:  #loop to run until choice=6
        while True:  # exceptional handling
            try:
                choice = eval(input("Enter Your Choice: \n 1.Add record 2.View Record 3.Edit Record 4.Search Record 5.Delete Record 6.Exit: "))  # input for choice
                break  # to exit loop
            except:
                print("Invalid Input")
                continue  # to continue in loop
        if choice == 1:
            add(2)  # calling add function with y=2
        elif choice == 2:
            view(2)  # calling view function with y=2
        elif choice == 3:
            edit(2)  # calling edit function with y=2
        elif choice == 4:
            search(2)  # calling search function with y=2
        elif choice == 5:
            delete(2)  # calling delete function with y=2
        elif choice > 6 or choice < 0:  # for any invalid input
            print("Invalid Input")


def sales_menu():  # defining sales menu function
    print("=" * 85)
    print("SALES MENU SECTION")  # to show which section the user is on
    print("." * 20)
    choice = 0
    while choice != 3:  # loop to execute until choice=3
        while True:  # exceptional handling
            try:
                choice = eval(input("Enter your Choice: \n 1.Add sales record 2.View sales Record 3.Exit: "))
                # input for choice
                break  # to exit loop
            except:
                print("Invalid Input")
                continue  # to continue loop
        if choice == 1:
            add(3)  # calling add function with y=3
        elif choice == 2:
            view(3)  # calling view function with y=3
        elif choice > 3 or choice < 0:  # for any invalid input
            print("Invalid Input")


def add(y):  # defining add function
    print("=" * 85)
    print("ADD RECORD SECTION")  # to show which section the user is on
    if y == 1:  # add function for bakery item
        print("." * 40)
        while True:  # exceptional handling
            try:
                item_id = eval(input("Enter Item ID: "))  # input for item ID
                break  # to exit loop
            except:
                print("Enter Numbers Only")
        if item_id in item:  # to check if ID already exists
            print("ID already exist")
        else:  # if ID is not present else would run
            while True:  # exceptional handling
                name = input("Enter Item Name: ")  # input for item name
                n = name.isalpha()  # exceptional handling
                if n == True:  # checking if the name is in alphabets
                    break
                else:  # else statement
                    print("Enter Alphabets Only")
            while True:  # exceptional handling
                brand = input("Enter Item Brand: ")  # input for item name
                n = brand.isalpha()  # exceptional handling
                if n == True:  # checking if the name is in alphabets
                    break
                else:  # else statement
                    print("Enter Alphabets Only")

            while True:  # exceptional handling
                try:
                    quantity = eval(input("Enter Item Quantity: "))
                    break
                except:
                    print("Enter Number Only")
            while True:  # exceptional handling
                try:
                    price = eval(input("Enter Item Price: "))
                    break
                except:
                    print("Enter Number Only")
            print("." * 40)

            item[item_id] = [name, brand, quantity, price]  # adding in item dictionary

    if y == 2:  # add function for bakery item
        print("." * 40)
        while True:  # exceptional handling
            try:
                customer_id = eval(input("Enter Customer ID: "))  # input for customer ID
                break
            except:
                print("Enter numbers only")
        if customer_id in customer:  # to check if ID already exists
            print("ID already exist")
        else:
            while True:  # exceptional handling
                name = input("Enter Customer Name: ")  # input for name
                x = name.isalpha()  # exceptional handling
                if x == True:  # to check if name is given in alphabets
                    break
                else:
                    print("Enter Alphabets Only")
            while True:  # exceptional handling
                try:
                    age = eval(input("Enter Customer Age: "))  # input for age
                    break
                except:
                        print("Invalid Input")
            while True:
                try:
                    number = eval(input("Enter Customer Number: "))  # input for mobile number
                    break
                except:
                    print("Invalid Input")
            print("." * 40)
            customer[customer_id] = [name, age, number]  # adding in customer dictionary

    if y == 3:  # add function for sales item
        print("." * 40)
        if len(item) == 0 or len(customer) == 0:  # to check if any record is empty
            print("Records are empty")
        else:  # else statement
            while True:  # exceptional handling
                try:
                    sales_id = eval(input("Enter Customer ID: "))  # input for customer ID
                    break
                except:
                    print("Invalid Input")
            if sales_id in customer:  # to check if ID is present in item dictionary
                while True:  # exceptional handling
                    try:
                        sales_id2 = eval(input("Enter Bakery Item ID: "))  # input for item ID
                        break
                    except:
                        print("Invalid Input")
                if sales_id2 in item:  # to check if ID is present in customer dictionary
                    while True:  # exceptional handling
                        try:
                            quantity = eval(input("Enter Quantity Of Item Purchased: "))  # input for quantity to buy
                            break
                        except:
                            print("Invalid Input")
                    if quantity < item[sales_id2][2]:  # checking if quantity is in stock
                        item[sales_id2][2] = item[sales_id2][2] - quantity  # updating quantity in item dictionary
                        bill = item[sales_id2][3] * quantity  # calculating bill
                        name1 = customer[sales_id][0]
                        name2 = item[sales_id2][0]
                        sales[len(sale_id)] = [sales_id, name1, sales_id2, name2, quantity, bill]
                        # adding it on sales dictionary

                        print("Your bill equals:", bill)
                        sale_id.append(1)

                    else:  # else statement
                        print("quantity required is not in stock")
                else:  # else statement
                    print("invalid ID")
            else:  # else statement
                print("invalid ID")
        print("." * 40)


def view(y):  # defining view function
    print("=" * 85)  # separation line
    print("VIEW RECORD SECTION")
    if y == 1:  # view function for item dictionary
        print("." * 45)
        if len(item.keys()) > 0:  # to check if records are full or empty
            for i in item.keys():  # loop for keys in item dictionary
                var = item[i]  # var set as key
                print("Item Id \tName\tBrand\tQuantity\tPrice")
                print(i, "  \t", var[0], "\t", var[1], " \t", var[2], "     \t", var[3])
                # printing keys along with its value
        else:
            print("Records are empty")
        print("." * 45)

    if y == 2:  # view function for customer
        print("." * 45)
        if len(customer.keys()) > 0:  # to check if records are full or empty
            for i in customer.keys():  # loop for keys in customer dictionary
                var = customer[i]  # var set as key
                print("Customer_Id \tName\tAge \tNumber")
                print(i, "          \t", var[0], "\t", var[1], "\t", var[2])  # printing keys along with its value
        else:
            print("Records are empty")
        print("." * 45)

    if y == 3:  # add function for sales item
        print("." * 85)
        if len(sales.keys()) > 0:  # to check if records are full or empty
            print("Sales_ID\tCustomer_ID \tCustomer_Name\tItem_ID \tItem_Name\tQuantity\tBill")

            for i in sales.keys():  # loop for keys in sales dictionary
                var = sales[i]  # var set as key

                print(i, "           \t", var[0], "      \t  ", var[1], "      \t", var[2], "    \t", var[3], "   \t", var[4], "      \t",
                      var[5])  # printing keys along with its value
        else:
            print("Records are empty")
        print("." * 85)

def edit(y):  # defining edit function
    print("=" * 85)  # separation line
    print("EDIT RECORD SECTION")  # to show which section the user is on
    print("." * 45)
    if y == 1:  # edit function for item
        if len(item.keys()) > 0:  # to check if records are full or empty
            while True:  # exceptional handling
                try:
                    idd = eval(input("Enter Item ID To Edit it's Info: "))  # input for ID info to edit
                    break
                except:
                    print("Invalid Input")
            if idd in item:
                while True:  # exceptional handling
                    name = input("Enter Item Name: ")  # input for new name
                    x = name.isalpha()  # exceptional handling
                    if x == True:  # if name is in alphabet
                        break
                    else:
                        print("Invalid Input")
                        continue
                while True:  # exceptional handling
                    brand = input("Enter Item Brand: ")  # input for new name
                    x = brand.isalpha()  # exceptional handling
                    if x == True:  # if name is in alphabet
                        break
                    else:
                        print("Invalid Input")
                        continue

                while True:  # exceptional handling
                    try:
                        quantity = eval(input("Enter Item Quantity: "))  # input for new quantity
                        break
                    except:
                            print("Invalid Input")
                while True:  # exceptional handling
                    try:
                        price = eval(input("Enter Item Price: "))  # input for new price
                        break
                    except:
                        print("Invalid Input")
                item[idd] = [name, brand, quantity, price]  # updating item dictionary
            else:
                print("invalid ID")
        else:
            print("Records are empty")
        print("." * 45)
    if y == 2:  # edit function for customer
        if len(customer) > 0:  # to check if records are full or empty
            while True:  # exceptional handling
                try:
                    idd = eval(input("Enter Customer ID To Edit it's Info: "))  # input for ID to search
                    break
                except:
                    print("Invalid Input")
            if idd in customer:  # check if ID is present
                while True:  # exceptional handling
                    name = input("Enter Customer Name: ")  # input for new customer name
                    x = name.isalpha()  # exceptional handling
                    if x == True:  # to check if name is in alphabet
                        break
                    else:
                        print("Invalid Input")
                        continue
                while True:  # exceptional handling
                    try:
                        age = eval(input("Enter Customer Age: "))  # input for new age
                        break
                    except:
                            print("Invalid Input")
                while True:  # exceptional handling
                    try:
                        number = eval(input("Enter Customer Number: "))  # input for new mobile number
                        break
                    except:
                        print("Invalid Input")
                customer[idd] = [name, age, number]  # updating customer dictionary
            else:
                print("Invalid ID")
        else:
            print("Records are Empty")
        print("." * 45)


def search(y):
    print("=" * 85)  # separation line
    print("SEARCH RECORD SECTION")  # to show which section the user is on
    print("." * 45)
    if y == 1:  # search for item
        if len(item.keys()) > 0:  # to check if records are full or empty
            while True:  # exceptional handling
                try:
                    idd = eval(input("Enter ID To Display it's Info: "))  # input for ID to display its info
                    break
                except:
                    print("Invalid Input")

            if idd in item:  # to check if item ID is present
                print("Item Name:", item[idd][0])  # printing item name
                print("Item Brand:", item[idd][1])  # printing item brand
                print("Item Quantity:", item[idd][2])  # printing item quantity
                print("Item Price:", item[idd][3])  # printing item price
            else:
                print("invalid ID")
        else:
            print("Records are Empty")
        print("." * 45)
    if y == 2:  # search for customer
        if len(customer.keys()) > 0:  # to check if records are full or empty
            while True:  # exceptional handling
                try:

                    idd = eval(input("Enter ID To Display it's Info: "))  # input for ID to display its info
                    break
                except:
                    print("Invalid Input")
            if idd in customer:  # to check if customer ID is present
                print("Customer Name:", customer[idd][0])  # printing customer name
                print("Customer Age:", customer[idd][1])  # printing customer age
                print("Customer Number:", customer[idd][2])  # printing customer number
            else:
                print("invalid ID")
        else:
            print("Records are Empty")
        print("." * 45)

def delete(y):
    print("=" * 85)
    print("DELETE RECORD SECTION")  # to show which section the user is on
    print("." * 45)
    if y == 1:  # delete function for item
        if len(item.keys()) > 0:  # to check if records are full or empty
            while True:  # exceptional handling
                try:
                    idd = eval(input("Enter ID That Needs to be Deleted: "))
                    # input for ID whose record is to be deleted
                    break
                except:
                    print("Invalid Input")
            if idd in item:  # to check if item ID is present
                del (item[idd])  # deleting record
                print("RECORD DELETED")
            else:
                print("invalid ID")
        else:
            print("Records are empty")
        print("." * 45)
    if y == 2:  # delete function for customer
        if len(customer) > 0:  # to check if records are full or empty
            while True:  # exceptional handling
                try:
                    idd = eval(input("Enter ID That Needs to be Deleted: "))
                    # input for ID whose record is to be deleted
                    break
                except:
                    print("Invalid Input")

            if idd in customer:  # to check if item ID is present
                del (customer[idd])  # deleting record
                print("RECORD DELETED")
            else:
                print("invalid ID")
        else:
            print("Records are empty")
        print("." * 45)


main_menu()  # calling main menu function



