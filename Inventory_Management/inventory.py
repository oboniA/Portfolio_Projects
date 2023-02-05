# ----------------------------------------------------------------------------------------
# Author: Oboni Anower (oboni.anower@gmail.com)
#
# inventory.py (c) 2023
#
# Description:   A stock-taking and inventory management program for Nike
#                warehouse that reads text file which contains data of country,
#                code, product, cost, quantity. the program lows user to perform
#                a range of functions such as searching for a product using code,
#                finding the product with the lowest quantity to restock, determining
#                the product with the highest quantity with is for sale and calculating
#                the total price value of each product stocked.
#
# Created:  05 February 2023 00:45:19
# Modified:
# -----------------------------------------------------------------------------------------


# Imported Library
from tabulate import tabulate

# -----------------------------------------------------------------------------------------
# Defining Parent class
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    # str representation
    def __str__(self):
        return f"Country  : {self.country} " \
               f"\nCode     : {self.code} " \
               f"\nProduct  : {self.product} " \
               f"\nCost     : {self.cost}" \
               f"\nQuantity : {self.quantity}"


# -----------------------------------------------------------------------------------------
# Defining Functions


# list of objects
shoe_list = []


# make object from text data
# create list of objects
def read_shoes_data():
    try:
        # reads inventory.txt file
        # create object from  text lines
        # adds objects to empty list called shoe_list
        with open('inventory.txt', 'r') as inventory_file:
            read_inventory = inventory_file.readlines()[1:]
            for line in read_inventory:
                row = line.split(',')

                # make object from data and add to list
                country, code, product, cost, quantity = [i.strip() for i in row]
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)

    except FileNotFoundError:
        print("File 'inventory.txt not available")


def capture_shoes():
    # user input for object details
    user_country = input("Enter Country: ")
    user_code = input("Enter Code: ")
    user_product = input("Enter Product: ")
    user_cost = int(input("Enter Cost: "))
    user_quantity = int(input("Enter Quantity: "))

    # write it to inventory.txt file
    with open('inventory.txt', 'a+') as write_file:
        write_file.write('\n' + user_country)
        write_file.write(',' + user_code)
        write_file.write(',' + user_product)
        write_file.write(',' + str(user_cost))
        write_file.write(',' + str(user_quantity))


# views data
# in table format
def view_all():
    # empty list to store updated text in inventory.txt file
    s_list = []

    with open('inventory.txt', 'r') as inventory_file:
        read_inventory = inventory_file.readlines()
        for line in read_inventory:
            d = line.split(',')
            s_list.append(d)

    # imported library
    print(tabulate(s_list, headers="firstrow"))


# finds lowest quantity
# adds to the quantity
# reference:
# https://github.com/tnaccarato/hyperion-dev-L1-capstone-IV/blob/5d270f6f2163cb82b10e7bf57237ef2c08317293/inventory.py#L425
# https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/
def re_stock():
    global lowest_index

    # stores quantities to find lowest
    shoe_quantity = [sh.get_quantity() for sh in shoe_list]

    # Finds lowest value stock
    lowest_in_stock = min(shoe_quantity)

    # Finds index of lowest value stock
    for shoe in shoe_list:
        if lowest_in_stock == shoe.quantity:
            lowest_index = shoe_list.index(shoe)

    # stores detail of lowest stocked product
    lowest_product = shoe_list[lowest_index]
    print(f"\nLOWEST STOCKED PRODUCT:\n{lowest_product}")

    # ask user to restock
    restock_option = input("\nRESTOCK? : Yes/No\n>>").lower()
    if restock_option == "yes":
        restock_amount = int(input("Enter amount to add: "))

        # updating new quantity
        new_quantity = lowest_product.quantity + restock_amount

        s_data_string = " "
        # reads file to replace the quantity
        with open('inventory.txt', 'r') as f:

            # writes shoes_list to a new string by line
            for line in f:
                s_data_string += line

            # each line to a list
            s_data_string = s_data_string.split("\n")

            # create variable for lowest quantity shoe data using it's index
            # splits shoe data into a list of words
            # updates amount
            # joins the restocked shoe list back together
            restocked_shoe = s_data_string[lowest_index + 1]
            restocked_shoe = restocked_shoe.split(",")
            restocked_shoe[4] = str(new_quantity)
            restocked_shoe = ",".join(restocked_shoe)

            # replaces entire old line with a new line
            s_data_string[lowest_index + 1] = restocked_shoe
            s_data_string = "\n".join(s_data_string)

        # updates text file
        with open("inventory.txt", "w") as shoes_f:
            shoes_f.writelines(s_data_string)

    elif restock_option == "no":
        print("\nReturn to main menu")

    else:
        print("invalid selection")


# finds particular shoe data with shoe code
def search_shoe():
    shoe_code = input("\nEnter Shoe Code: ")
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            print(shoe)
    print("\nReturn to main menu")


# total price of each product
def value_per_item():
    print("\nTOTAL VALUE OF EACH PRODUCT IN STOCK")
    for shoe in shoe_list:
        total_val = shoe.get_quantity() * shoe.get_cost()
        print(f"{shoe.product}: {total_val}")

    print("\nReturn to main menu")


# product with largest quantity
def highest_qty():
    global highest_index

    shoe_quantity = [sh.get_quantity() for sh in shoe_list]

    # Finds highest value stock
    high_in_stock = max(shoe_quantity)

    # Finds index of highest value stock
    for shoe in shoe_list:
        if high_in_stock == shoe.quantity:
            highest_index = shoe_list.index(shoe)

    # stores detail of highest stocked product
    highest_product = shoe_list[highest_index]
    print(f"\nFOR SALE:\n{highest_product}")
    print("\nReturn to main menu")


# ==========Main Menu=============
if __name__ == "__main__":

    read_shoes_data()

    user_choice = ""  # initiated outside while loop
    while user_choice != 'q':
        user_choice = input("\nSELECT AN OPTION: "
                            "\nvd - View data"
                            "\ne  - New Entry"
                            "\nr  - Restock"
                            "\nsr - Search"
                            "\npv - product value"
                            "\nsl - Product on sale"
                            "\nq  - quit"
                            "\n>>")

        if user_choice == 'vd':
            view_all()

        elif user_choice == 'e':
            capture_shoes()

        elif user_choice == 'r':
            re_stock()

        elif user_choice == 'sr':
            search_shoe()

        elif user_choice == 'pv':
            value_per_item()

        elif user_choice == 'sl':
            highest_qty()

        elif user_choice == 'q':
            print("------Goodbye------")

        else:
            print("INCORRECT SELECTION")
