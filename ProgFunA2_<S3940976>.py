# SUKHUM BOONDECHARAK (S3940976)
# The Highest Part Attempted: HD LEVEL (Only display the most frequent customer)

# Problems:
# 1. Cannot not figure out the proper logic of most requirements in HD level
# 2. Don't know how to keep the code neat, so ended up having a spaghetti code
# 3. For a beginner like me, the complexity of the requirements is totally not fundamental
# 4. I understand the logic for most part, but am lack of imagination to connecting dots
# 5. Other assignments make it hard to focus on coding since this must take time

# In conclusion, I still find coding fun and enjoyable though I cannot make this program complete
# Thank you for the advice throughout the semester for both lecturers
# It has been a whole new world for me!

# EXCEPTIONS
# Defined custom exceptions for future errors
class NotFound(Exception):
    pass

class IncorrectInput(Exception):
    pass

class InvalidResponse(Exception):
    pass

class InvalidSelection(Exception):
    pass


# CUSTOMERS
class Customer:

    def __init__(self, cid, name):
        self.__cid = cid
        self.__name = name.strip()
        self.__type = "C"

    @property
    def cid(self):
        return self.__cid

    @cid.setter
    def cid(self, cid):
        self.__cid = cid

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def type(self):
        return self.__type

    def get_service_fee(self, cost):
        pass

    def get_discount(self, cost):
        pass

    def display_info(self):
        print("ID: {}\tType: {}\tName: {}\n".format(self.cid, self.type, self.name))

# Customer class as a parent class
# The lower tier of customers with default service fee at 10%
class BronzeCustomer(Customer):

    service_fee_rate = 0.1

    def __init__(self, cid, name):
        super().__init__(cid, name)
        self.__type = "B"
        self.service_fee_rate = BronzeCustomer.service_fee_rate

    @property
    def type(self):
        return self.__type

    def get_service_fee(self, cost):
        return self.service_fee_rate * cost

    def get_discount(self, cost):
        return 0

    # A method to display object attributes for Bronze members
    def display_info(self):
        print("ID: {:<3}\tType: {:<3}\tName: {:<10}\tService Fee: {:>5}%".format(self.cid,
                                                                                 self.type,
                                                                                 self.name,
                                                                                 self.service_fee_rate * 100))

    # A method to apply the new service fee for the class
    @staticmethod
    def set_service_fee_rate(rate):
        BronzeCustomer.service_fee_rate = rate

# Customer class as a parent class
# The middle tier of customers with no service fee
class SilverCustomer(Customer):

    service_fee_rate = 0

    def __init__(self, cid, name):
        super().__init__(cid, name)
        self.__type = "S"
        self.service_fee_rate = SilverCustomer.service_fee_rate

    @property
    def type(self):
        return self.__type

    def get_service_fee(self, cost):
        return 0

    def get_discount(self, cost):
        return 0

    # A method to display object attributes for Silver members
    def display_info(self):
        print("ID: {:<3}\tType: {:<3}\tName: {:<10}\tService Fee: {:>5}%".format(self.cid,
                                                                                 self.type,
                                                                                 self.name,
                                                                                 self.service_fee_rate * 100))

# Customer class as a parent class
# The highest tier of customers with no service fee and a default discount rate at 8%
class GoldCustomer(Customer):

    service_fee_rate = 0
    discount_rate = 0.08

    def __init__(self, cid, name):
        super().__init__(cid, name)
        self.__type = "G"
        self.service_fee_rate = GoldCustomer.service_fee_rate
        self.discount_rate = GoldCustomer.discount_rate

    @property
    def type(self):
        return self.__type

    def get_service_fee(self, cost):
        return 0

    def get_discount(self, cost):
        return self.discount_rate * cost

    # A method to display object attributes for Gold members
    def display_info(self):
        print("ID: {:<3}\tType: {:<3}\tName: {:<10}\tService Fee: {:>5}%\t\tDiscount: {:>5}%".format(self.cid,
                                                                                                     self.type,
                                                                                                     self.name,
                                                                                                     self.service_fee_rate * 100,
                                                                                                     self.discount_rate * 100))


# ITEMS
class Item:

    def __init__(self, iid, name, price):
        self.__iid = iid
        self.__name = name
        self.__price = price

    @property
    def iid(self):
        return self.__iid

    @iid.setter
    def iid(self, iid):
        self.__iid = iid

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def display_info(self):
        print("Item ID: {} "
              "\nItem Name: {}"
              "\nItem Price: {}\n".format(self.iid,
                                          self.name,
                                          self.price))

# Item class as a parent class
# Categorised as food
class FoodDish(Item):

    def __init__(self, iid, name, price):
        super().__init__(iid, name, price)
        self.__type = "F"

    @property
    def type(self):
        return self.__type

    # A method to display object attributes for food
    def display_info(self):
        print("ID: {:<3}\tType: {:<3}\tName: {:<15}\tPrice: {:>5}".format(self.iid, self.type, self.name, self.price))

# Item class as a parent class
# Categorised as drink
class Drink(Item):

    def __init__(self, iid, name, price):
        super().__init__(iid, name, price)
        self.__type = "D"

    @property
    def type(self):
        return self.__type

    # A method to display object attributes for drink
    def display_info(self):
        print("ID: {:<3}\tType: {:<3}\tName: {:<15}\tPrice: {:>5}".format(self.iid, self.type, self.name, self.price))

# Categorised as Banquet
# Consists of multiple items
# With at least one food and one drink as a minimum requirement
class Banquet:
    def __init__(self, iid, name, component):
        self.__iid = iid
        self.__name = name
        self.__component = component
        self.__type = "B"

    @property
    def iid(self):
        return self.__iid

    @property
    def name(self):
        return self.__name

    @property
    def component(self):
        return self.__component

    @property
    def type(self):
        return self.__type

    @property
    def price(self):
        price = 0
        for i in self.component:
            if i.type == "F":
                price += i.price
        return price

    # A method to display object attributes for banquet
    # Component items will have to be joined by a space before being displayed
    def display_info(self):
        component_name_list = []
        for c in self.component:
            component_name_list.append(c.name)
        print("ID: {:<3}\tType: {:<3}\tName: {:<15}\tComponent: {:>5}".format(self.iid, self.type, self.name,
                                                                              " ".join(component_name_list)))


# ORDERS
# Contains order information
# Includes information of customers, items purchased, and amount purchased
class Order:

    def __init__(self, customer, item, quantity):
        self.__customer = customer
        self.__item = item
        self.__quantity = quantity

    @property
    def customer(self):
        return self.__customer

    @property
    def item(self):
        return self.__item

    @property
    def quantity(self):
        return self.__quantity

    # A method to compute cost of order
    # Sums up the original cost and calculate service fee and discount amount
    def compute_cost(self):
        original_cost = self.quantity * self.item.price
        service_fee = self.customer.get_service_fee(original_cost)
        discount = self.customer.get_discount(original_cost)
        return original_cost, service_fee, discount


# RECORDS
# Stores information of customers and items
class Records:
    list_of_existing_customers = []
    list_of_existing_items = []

    # A method to open and translate information of customers from a specific formatted file
    # The method extracts information according to each type of member
    # It then updates the extracted information to the list
    def read_customers(self, file_name):
        file = open(file_name, "r")
        line = file.readline()
        while line:
            field_from_line = line.strip().split(",")
            cid = int(field_from_line[0].strip().split(":")[1].strip())
            customer_type = field_from_line[1].strip().split(":")[1].strip()
            name = field_from_line[2].strip().split(":")[1].strip()
            if customer_type == "B":
                new_customer = BronzeCustomer(cid=cid,
                                              name=name)
                self.list_of_existing_customers.append(new_customer)
            elif customer_type == "S":
                new_customer = SilverCustomer(cid=cid,
                                              name=name)
                self.list_of_existing_customers.append(new_customer)
            elif customer_type == "G":
                discount = float(field_from_line[3].strip().split(":")[1].strip())
                new_customer = GoldCustomer(cid=cid,
                                            name=name)
                new_customer.discount_rate = discount
                self.list_of_existing_customers.append(new_customer)
            line = file.readline()

    # A method to open and translate information of items from a specific formatted file
    # The method extracts information according to each type of item
    # It then updates the extracted information to the list
    def read_items(self, file_name):
        file = open(file_name, "r")
        line = file.readline()
        while line:
            field_from_line = line.strip().split(",")
            iid = field_from_line[0].strip().split(":")[1].strip()
            item_type = field_from_line[1].strip().split(":")[1].strip()
            name = field_from_line[2].strip().split(":")[1].strip()
            if item_type == "F":
                price = float(field_from_line[3].strip().split(":")[1].strip())
                new_item = FoodDish(iid=iid,
                                    name=name,
                                    price=price)
                self.list_of_existing_items.append(new_item)
            elif item_type == "D":
                price = float(field_from_line[3].strip().split(":")[1].strip())
                new_item = Drink(iid=iid,
                                 name=name,
                                 price=price)
                self.list_of_existing_items.append(new_item)

            # An extra extraction for banquets
            # Have to extract each component and append to a list
            elif item_type == "B":
                component_from_field = field_from_line[3].strip().split(":")[1]
                component_list = []
                component_name_list = component_from_field.strip().split(" ")
                for component_name in component_name_list:
                    component = self.find_item(component_name)
                    if component is not None:
                        component_list.append(component)

                # This is to check if the banquet contains at least one food and one drink
                num_food = 0
                num_drink = 0
                for i in component_list:
                    if i.type == "F":
                        num_food += 1
                    if i.type == "D":
                        num_drink += 1
                if num_food > 0 and num_drink > 0:
                    new_item = Banquet(iid=iid,
                                       name=name,
                                       component=component_list)
                    self.list_of_existing_items.append(new_item)

                # If condition is not fulfilled, tell user and skip
                else:
                    print("\nBanquet " + iid + " is not valid!"
                                               "\nEach banquet needs at least one food and one drink!")
            line = file.readline()

    # A method to check if search value for a customer is in the database
    # The method can check for both ID and name
    # If not found, raises an exception
    def find_customer(self, search_value):
        for customer in self.list_of_existing_customers:
            if search_value.strip() == customer.name:
                return customer
            elif search_value.strip() == str(customer.cid):
                return customer
        raise NotFound("Customer not found!")

    # A method to check if search value for an item is in the database
    # The method can check for both ID and name
    # If not found, raises an exception
    def find_item(self, search_value):
        for item in self.list_of_existing_items:
            if search_value.strip() == item.name:
                return item
            elif search_value.strip() == str(item.iid):
                return item
        raise NotFound("Item not found!")

    # A method to display all customers' information in the database
    def display_customers(self):
        for customer in self.list_of_existing_customers:
            customer.display_info()

    # A method to display all items' information in the database
    def display_items(self):
        for item in self.list_of_existing_items:
            item.display_info()

    # A method to add customer's information to the database
    def add_customer(self, customer):
        self.list_of_existing_customers.append(customer)

    # A method to automatically generate a new id from the current highest number for a customer
    def generate_next_id(self):
        max_cid = 0
        for customer in self.list_of_existing_customers:
            if customer.cid > max_cid:
                max_cid = customer.cid
        return max_cid + 1


# OPERATIONS
# Contains major executions for the entire program
class Operations:

    list_of_orders = []

    # Defines files as attributes in the instructor, not in a method
    # The reason is to only load the file once when opening the program
    def __init__(self, customers_file, items_file):
        self.list_of_orders = []
        self.record = Records()
        self.record.read_customers(customers_file)
        self.record.read_items(items_file)

    # A method containing a variety of functions to be executed
    def main_menu(self):

        # Define a registration fee to be used later
        reg_fee = 0

        # Print the welcome message
        self.print_welcome()

        # Users can only enter a specific number
        # Enforce users to input a valid number using a while loop and exceptions
        # If the valid input is entered, proceed next
        # Otherwise, let them try again
        while True:
            try:
                user_option = int(input("\nPlease enter your option [0-8]:\n"))
                if user_option in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                    break
                else:
                    print("\nNumber is not in range!")
            except Exception as e:
                print("\nNot an integer!")

        # Execute the ordering process if 1 is entered
        # Start with asking for a name or ID
        if user_option == 1:
            customer_name = input("\nPlease enter your name or ID:\n").strip()

            # Attaches the list of items so there is a reference to enter a valid name or ID in the next action
            print("#" * 19 + " List of Items " + "#" * 19)
            self.record.display_items()

            # Users can only enter name or ID valid in the existing list of items
            # Enforce users to input a valid name or ID using a while loop and exceptions
            # If the valid input is entered, proceed next
            # Otherwise, let them try again
            while True:
                try:
                    item_option = input("\nPlease select your preferred item from the list above"
                                        "\nYou can enter by item name or ID:\n").strip()
                    item = self.record.find_item(item_option)
                    break
                except NotFound as e:
                    print(e)

            # Users can only enter a valid number
            # Enforce users to input a valid number using a while loop and exceptions
            # If the valid input is entered, proceed next
            # Otherwise, let them try again
            while True:
                try:
                    item_amount = input("\nPlease enter the amount (number only): \n").strip()
                    if int(item_amount) <= 0:
                        raise IncorrectInput("Cannot be 0 or negative!")
                    break
                except IncorrectInput as e:
                    print(e)
                except ValueError:
                    print("Have to be a number!")

            # Check if the name is in the database
            # If not, ask if they want to register for a membership
            customer = None
            try:
                customer = self.record.find_customer(customer_name)
            except NotFound:

                # Users can only enter a specific letter
                # Enforce users to input a valid letter using a while loop and exceptions
                # If the valid input is entered, proceed next
                # Otherwise, let them try again
                while True:
                    try:
                        reg_option = input("\nYou are a new customer!"
                                           "\nDo you want to register for a membership?"
                                           "\n(enter 'y' to proceed or 'n' to decline):\n")
                        if reg_option not in ["y", "n"]:
                            raise InvalidResponse("PLease enter only 'y' or 'n'")
                        break
                    except InvalidResponse as e:
                        print(e)

                # If they want to register, ask which level they want to register for
                if reg_option == "y":

                    # Users can only enter a specific letter
                    # Enforce users to input a valid letter using a while loop and exceptions
                    # If the valid input is entered, proceed next
                    # Otherwise, let them try again
                    while True:
                        try:
                            type_option = input("\nWhich level do you prefer?"
                                                "\n(enter 'S' for Silver and 'G' for Gold):\n")
                            if type_option not in ["S", "G"]:
                                raise InvalidSelection("Please enter only 'S' or 'G'")
                            break
                        except InvalidSelection as e:
                            print(e)

                    # if Silver is chosen, 100 service fee is recorded
                    # The customer become a Silver member immediately
                    # The ID is automatically generated with [the current highest ID +1]
                    # In this case, if they entered a number, the number becomes a name
                    if type_option == "S":
                        reg_fee = 100
                        customer = SilverCustomer(self.record.generate_next_id(), customer_name)
                        print("\nYou have been registered!\n")

                    # if Gold is chosen, 300 service fee is recorded
                    # The customer become a Gold member immediately
                    # The ID is automatically generated with [the current highest ID +1]
                    # In this case, if they entered a number, the number becomes a name
                    elif type_option == "G":
                        reg_fee = 300
                        customer = GoldCustomer(self.record.generate_next_id(), customer_name)
                        print("\nYou have been registered!\n")

                # If they don't want to register, automatically becomes a Bronze member
                else:
                    customer = BronzeCustomer(self.record.generate_next_id(), customer_name)

                # The new customer's information is stored to the database
                self.record.add_customer(customer)

            # If already a member, tell them the level
            else:
                print("\nYou member type is {}".format(customer.type))

            # Create an object order to store the order information
            order = Order(customer, item, int(item_amount))

            # Calculate significant costs and extract them to each variable
            costs = order.compute_cost()
            item_cost = costs[0]
            service_fee = costs[1]
            discount = costs[2]

            # Set condition to include registration fee
            if reg_fee != 0:
                total_cost = item_cost + service_fee - discount + reg_fee
            else:
                total_cost = item_cost + service_fee - discount

            # Print the receipt
            print(("*" * 50) + "\n" + "Receipt of Customer " + customer.name + "\n" + ("*" * 50))
            print(f"{item.name + ':':<20}{str(item.price) + ' (AUD) x ' + str(item_amount):>30}")
            print(f"{'Service fee:':<20}{service_fee:>24.1f}{' (AUD)':>6}")
            if customer.type == "G":
                print(f"{'Discount:':<20}{discount:>24.1f}{' (AUD)':>6}")
            if reg_fee != 0:
                print(f"{'Registration fee:':<20}{reg_fee:>24.1f}{' (AUD)':>6}")
            print(f"{'Total cost:':<20}{total_cost:>24.1f}{' (AUD)':>6}\n")

            # Create a new order and store it to the list of orders
            customer_name_record = customer.name
            item_name_record = item.name
            new_order = Order(customer=customer_name_record,
                              item=item_name_record,
                              quantity=item_amount)
            self.list_of_orders.append(new_order)
            self.continue_to_browse()

        # Show the list of customers if 2 is entered
        elif user_option == 2:
            print("#" * 31 + " List of Customers " + "#" * 31)
            self.record.display_customers()
            self.continue_to_browse()

        # Show the list of items if 3 is entered
        elif user_option == 3:
            print("#" * 30 + " List of Items " + "#" * 30)
            self.record.display_items()
            self.continue_to_browse()

        # Execute the reading orders process if 4 is entered
        # Check if the file can be loaded.
        # If yes, showing the result.
        # Otherwise, inform them and proceed next
        elif user_option == 4:
            try:
                file_name = input("\nPlease enter your order file: \n")
                self.order_meals_via_a_file(file_name)
                print("Successfully placing the orders!")
                self.continue_to_browse()
            except Exception as e:
                print("Cannot load the order file!")
                self.continue_to_browse()

        # Execute service fee adjustment for all Bronze members if 5 is entered
        elif user_option == 5:

            # Users can only enter a specific types of number
            # Enforce users to input a valid number using a while loop and exceptions
            # If the valid input is entered, proceed next
            # Otherwise, let them try again
            while True:
                try:
                    new_rate = float(input("\nPlease enter a new rate:\n"))
                    if float(new_rate) <= 0:
                        raise IncorrectInput("Cannot be 0 or negative!")

                    # Check for the current member in Bronze members and apply the new rate for them
                    # Otherwise, the new rate will only be applied with the newcomers
                    for customer in self.record.list_of_existing_customers:
                        if customer.type == "B":
                            customer.service_fee_rate = new_rate

                    # Apply the new rate to the class
                    BronzeCustomer.set_service_fee_rate(new_rate)
                    self.continue_to_browse()
                    break
                except IncorrectInput as e:
                    print(e)
                except ValueError as e:
                    print("Have to be a number!")

        # Execute discount adjustment for a specific Gold member if 6 is entered
        elif user_option == 6:

            # Users can only enter an existing Gold member name or ID
            # Enforce users to input a valid name or ID using a while loop and exceptions
            # If the valid input is entered, proceed next
            # Otherwise, let them try again
            while True:
                try:
                    search_value = input("Please enter a Gold member's name or ID: \n")
                    customer = self.record.find_customer(search_value)
                    if customer.type != "G":
                        raise IncorrectInput("Must be a gold member!")

                    new_rate = float(input("\nPlease enter a new rate:\n"))

                    # Users can only enter a specific types of number
                    # Enforce users to input a valid number using a while loop and exceptions
                    # If the valid input is entered, proceed next
                    # Otherwise, let them try again
                    if new_rate <= 0:
                        raise IncorrectInput("Cannot be 0 or negative!")

                    # IF the rate and name or ID is valid, adjust the discount for that particular customer
                    customer.discount_rate = new_rate
                    break
                except NotFound as e:
                    print(e)
                except ValueError as e:
                    print(e)
                except IncorrectInput as e:
                    print(e)
            self.continue_to_browse()

        # Show list of orders if 7 is entered
        # Check first if the list is not empty
        # If it is, inform that there is no record to show
        elif user_option == 7:
            if not self.list_of_orders:
                print("There is no record at the moment!")
                self.continue_to_browse()
            else:
                self.display_all_orders()
                self.continue_to_browse()

        # Show the most frequent customer if 8 is entered
        elif user_option == 8:
            self.most_frequent_customer()
            self.continue_to_browse()

        # Exit the program if 0 is entered
        elif user_option == 0:
            self.exit_program()

    # An actual method to open and translate information of orders from a specific formatted file
    # It then updates the extracted information to the list
    def read_orders(self, file_name):
        file = open(file_name, "r")
        line = file.readline()
        while line:
            field_from_line = line.strip().split(",")

            customer_text = field_from_line[0]
            item_text = field_from_line[1]

            customer_parts = customer_text.strip().split(":")
            item_parts = item_text.strip().split(":")
            item_and_quantity = item_parts[1].strip().split(" ")

            customer_name_or_id = customer_parts[1]
            find_customer_name = self.record.find_customer(customer_name_or_id)
            customer_name = find_customer_name.name

            item_name_or_id = item_and_quantity[0]
            find_item_name = self.record.find_item(item_name_or_id)
            item_name = find_item_name.name

            item_quantity = item_and_quantity[1]

            new_order = Order(customer = customer_name,
                              item = item_name,
                              quantity = item_quantity)
            self.list_of_orders.append(new_order)
            line = file.readline()

    # A method to show all orders in the list
    def display_all_orders(self):
        print("#" * 22 + " List of Orders " + "#" * 22)
        for order in self.list_of_orders:
            print("Name: {:<10}\tItem: {:<20}\tAmount: {:<5}".format(str(order.customer), str(order.item), str(order.quantity)))

    # A method to order using the information from a file
    def order_meals_via_a_file(self, orders_file):
        self.read_orders(orders_file)

    # A method to show the most frequent user
    def most_frequent_customer(self):
        try:

            # Create a temporary list and use for loop to extract only names from the list of orders
            frequent_customer = []
            for order in self.list_of_orders:
                frequent_customer.append(order.customer)

            # Start counting every name in the temporary list
            # Then print the most counted name with the number of counts
            count = 0
            name = frequent_customer[0]
            for i in range(len(frequent_customer)):
                target = frequent_customer.count(i)
                if target > count:
                    count = target
                    name = frequent_customer[i]
            print("\nThe most frequent customer is " + name + " with " + str(frequent_customer.count(name)) + " order(s)!")

        # If there is no order, inform that there is nothing to show
        except IndexError:
            print("Sorry, there is still no order in the list.")

        # freq = dict()
        # for order in self.list_of_orders:
        #     try:
        #         freq[order.customer.id] += 1
        #     except KeyError:
        #         freq[order.customer.id] = 1
        #
        # most_frequent_customer_id =

    # A static method containing the welcome message.
    @staticmethod
    def print_welcome():
        print("\nWelcome to the RMIT restaurant ordering system!\n")
        print("#" * 60)
        print("You can choose from the following options:")
        print("[1] Order a meal")
        print("[2] Display existing customers information")
        print("[3] Display existing dishes information")
        print("[4] Order meals via file")
        print("[5] Adjust the service fee rate of all bronze customers")
        print("[6] Adjust the discount rate of a gold customer")
        print("[7] Display all orders")
        print("[8] The most frequent customer")
        print("[0] Exit the program")
        print("#" * 60)

    # A method to go back to main menu
    def continue_to_browse(self):
        input("\nPress enter to go back to main menu:")
        self.main_menu()

    # A static method showing farewell message and exit the program
    @staticmethod
    def exit_program():

        print("\nThank you for coming!\nHave a good day!")


# set an object to have an Operation class, then run the main_menu()
operation = Operations("customers.txt", "items.txt")
operation.main_menu()
