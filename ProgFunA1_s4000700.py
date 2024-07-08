

# Name - Dhanesh Gaikwad
# Student - 4000700


'''
# References - 1: https://docs.python.org/3/
               2: Exception Handling (Try-Except):https://realpython.com/python-exceptions/
               3: For sys module i have referred : https://www.geeksforgeeks.org/sys-module-python/
Customer: List of all registered customer names.
Location: List of possible departures and  destinations.
RAte Type: A dictionary containing the different types of fares and the costs associated with them.
Basic fare for a ride.
Trips of customer : A list containing information about each booked trip.

Functions used in this code::

1: Calc_Total(): calculates the total fare for a journey depending on distance, rate type, and customer loyalty (10% discount for current customers).
2: History(): Retrieves and displays a specific customer's booking history.
3: book_trip(): This function books the trip. Collects the customer's name, departure, destination(s), and pricing type.
            and gives a booking receipt at the end.
4: New_Rate_type(): Allows users to either create new rate kinds or update existing ones.
5: Get_Customers(): Displays the list of registered customers.
6: Get_Locations(): Returns a list of available locations.
7: Get_Rates(): Displays the existing rate categories and their costs.
8: Add_Location(): Allows you to add new locations to the existing list.
9: Valuable_Customer(): Identifies and presents the most valuable customer(s) based on their total spending.
10:main(): This is the entry point function where the code starts from

Flow of the code:-

The program begins with a primary loop that allows users to select several functionalities from a menu.
The system assists in booking a trip, viewing client histories, creating new rate types, adding new locations, and identifying the most valued customers.
Input is received from the user via standard input (sys.stdin.readline()), and output is shown using sys.stdout.write().

'''

import sys

# Initialize the data
Customers = ['Dhanesh', 'Dhumal','Shivani','Harshada','Omkar','Yukta','Shraddha']  # List of customer
Locations = ['Melbourne','Clayton','Calton','Kilda','Pakrvill','Chadstone']        # List of Locations 
Rate_Type = {'standard': 1.5,'peak': 1.8,'weekends': 2.0,'holiday': 2.5}           # Dict of rate type which holds rate type and their values
Basic_Fee = 4.2
Trips_of_Customer = [] # An empty list for trips of customer





# It determines how much a ride will cost.
# If the consumer has already taken a ride, there will be a discount of 10%.

def Calc_Total(distance, rate_type, is_existing_customer):
    distance_fee = distance * Rate_Type[rate_type]
    
    discount = 0
    if is_existing_customer:            ## if the customer is existing customer the he will get discount
        discount = 0.10 * distance_fee
    
    total_cost = Basic_Fee + distance_fee - discount         ## Making the calculation   
    return distance_fee, discount, total_cost


# This function displays a certain customer's booking history.
# When the customer's name is input, all of their previous travels are shown.

def History():
    sys.stdout.write("Please enter the customer's name: \n")
    customer_name = sys.stdin.readline().strip()

    found_bookings = False      # Initializing the found_booking variable to False
    sys.stdout.write(f"This is the booking history of {customer_name}:\n")
    sys.stdout.write("{:<30} {:<30} {:<30} {:<30}\n".format("Departure", "Destinations", "Total Cost", "Rate Type"))

    for trip in Trips_of_Customer:         # this for loop checks the trip in customer list
        if customer_name == trip[0]:        
            found_bookings = True
            departure = trip[1]
            destinations = ", ".join(trip[2])
            total_cost = trip[3]
            rate_type = trip[4]
            sys.stdout.write("{:<30} {:<30} {:<30} {:<30}\n".format(departure, destinations, total_cost, rate_type))
    
    if not found_bookings:          # this if statement will run if there are no bookings
        sys.stdout.write("No booking history found for the customer.\n")



# This function Book_trip is to book a trip
# Name, location of departure, destination, and rate type (such as peak or holiday rate) are all requested from the consumer.
# After getting the data, it calculates the trip's cost and creates a receipt.

def book_trip():
    
    # Getting the customer's name and checking if it's an existing customer
    
    # While loop is used until the user enters a valid name. 
    # If the entered data is not alphabetic then it will display an error and the while loop will run again
    while True:                                                         
        sys.stdout.write("Please enter the customer's name:\n")
        
        customer_name = sys.stdin.readline().strip()
        if customer_name.isalpha():
            break
        else:
            sys.stdout.write("ERROR: The customer name can only contain alphabetic characters..\n")

    is_existing_customer = customer_name in Customers

    # If the customer is new then it will be added to the customer list
    if not is_existing_customer:
        Customers.append(customer_name)

    # In this part users has to enter the departure location and it checks if the location is available in the location list
    # If not then the while loop will rerun again
    # This while loop is used until the user enters a valid destination.
    
    while True:
        sys.stdout.write("Please enter the departure location: \n")
        departure = sys.stdin.readline().strip()
        if departure in Locations:
            break
        else:
            sys.stdout.write("Error: Departure location is not valid.\n")

    destinations = []
    distances = []

    # In this part users has to enter the destination location and it checks if the location is available in the location list
    # There is a if and else statement to check 
    # If not then the while loop will rerun again
    # This while loop is used until the user enters a valid destination.
    while True:
        # Getting the destination location it runs in a while loop until the users enter a valid destination
        while True:
            sys.stdout.write("Please enter the destination location: \n")
            
            destination = sys.stdin.readline().strip()          # storing the destination in the variable called 'destination'

            if destination in Locations and destination != departure and destination not in destinations:
                break
            else:
                sys.stdout.write("Error: Destination location is not valid or same as departure or already added.\n")

        # Getting the distance to the destination it runs in a while loop until the users enter a valid destination
        while True:
            try:                                    # I have used try and catch here to avoid error
                sys.stdout.write(f"Please enter the distance (in km) between {departure} and {destination}: \n")
                distance = float(sys.stdin.readline().strip())
                if distance > 0:
                    break
                else:
                    sys.stdout.write("ERROR!!: Distance should be a positive number\n.")
            except ValueError:
                sys.stdout.write("ERROR!!: Invalid distance input\n.")
        
        destinations.append(destination) #Entered destination gets add to the list
        distances.append(distance)       #Entered Distance gets add to the list   

        sys.stdout.write("Would you like to add another destination? (yes/no): \n")
        another_destination = sys.stdin.readline().strip()

        if another_destination.lower() != 'yes':
            break

    total_distance = sum(distances)

    # Getting the rate type
    while True:

        sys.stdout.write("Please enter the rate type (standard, peak, weekends, holiday): \n")
        rate_type = sys.stdin.readline().strip()
        if rate_type in Rate_Type:
            break
        else:
            print("Error: Rate type is not valid.\n")

    distance_fee, discount, total_cost = Calc_Total(total_distance, rate_type, is_existing_customer) #initializing the variables

    # Adding trip to customer_trips list using append function
    Trips_of_Customer.append((customer_name, departure, destinations, total_cost, rate_type))  # Update with departure, destinations, total_cost, and rate_type


    # Print the receipt
    sys.stdout.write("-" * 57 + "\n")
    sys.stdout.write("Taxi Receipt\n")
    sys.stdout.write("-" * 57 + "\n")
    sys.stdout.write(f"Name: {customer_name}\n")
    sys.stdout.write(f"Departure: {departure}\n")
    for i in range(len(destinations)):
        sys.stdout.write(f"Destination: {destinations[i]}\n")
        sys.stdout.write(f"Distance: {distances[i]:.2f} (km)\n")
    sys.stdout.write("-" * 57 + "\n")
    sys.stdout.write(f"Rate: {Rate_Type[rate_type]:.2f} (AUD per km)\n")
    sys.stdout.write(f"Total Distance: {total_distance:.2f} (km)\n")
    sys.stdout.write("-" * 57 + "\n")
    sys.stdout.write(f"Basic fee: {Basic_Fee:.2f} (AUD)\n")
    sys.stdout.write(f"Distance fee: {distance_fee:.2f} (AUD)\n")
    sys.stdout.write(f"Discount: {discount:.2f} (AUD)\n")
    sys.stdout.write("-" * 57 + "\n")
    sys.stdout.write(f"Total cost: {total_cost:.2f} (AUD)\n")


# Function to add new rate type
def New_Rate_type():
    while True:  # using while loop to rerun until the user enters a vaild input
        sys.stdout.write("Choose an operation:\n")
        sys.stdout.write("1. Add new rate types\n")
        sys.stdout.write("2. Update existing rate types\n")
        
        choice = None           # initializing the variable choice to None
        while choice not in [1, 2]:  # Loop to make sure a valid choice is made
            
            # Handling exception error
            try:            
                choice = int(sys.stdin.readline().strip())
                if choice not in [1, 2]:
                    raise ValueError
            except ValueError:
                sys.stdout.write("Invalid choice. Please enter 1 or 2.\n")

        if choice == 1: 
            sys.stdout.write("Enter new rate types : \n")
            rate_type_input = sys.stdin.readline().strip()
            new_rate_types = [rate.strip() for rate in rate_type_input.split(',')]

            sys.stdout.write("Enter cost for the new rate types: \n")
            price_input = sys.stdin.readline().strip()
            new_prices = [float(price.strip()) for price in price_input.split(',')]

            if len(new_rate_types) != len(new_prices):
                sys.stdout.write("Error: Number of rate types and prices do not match.\n")
                continue

            valid_prices = True
            for price in new_prices:
                if price <= 0:
                    valid_prices = False
                    sys.stdout.write("Error: Input must be positive numbers.\n")
                    break

            if valid_prices:
                for i in range(len(new_rate_types)):
                    Rate_Type[new_rate_types[i]] = new_prices[i]
                sys.stdout.write("New rate types and prices added successfully.\n")

        elif choice == 2:
            sys.stdout.write("Enter the rate type to be updated (comma-separated): \n")
            rate_type_input = sys.stdin.readline().strip()
            existing_rate_types = [rate.strip() for rate in rate_type_input.split(',')]

            sys.stdout.write("Enter new prices for the existing rate types (comma-separated): \n")
            price_input = sys.stdin.readline().strip()
            new_prices = [float(price.strip()) for price in price_input.split(',')]

            if len(existing_rate_types) != len(new_prices):
                sys.stdout.write("Error: Number of rate types and prices do not match.\n")
                continue

            valid_prices = True
            for price in new_prices:
                if price <= 0:
                    valid_prices = False
                    sys.stdout.write("Error: Prices must be positive numbers.\n")
                    break

            if valid_prices:
                for i in range(len(existing_rate_types)):
                    rate_type = existing_rate_types[i]
                    if rate_type in Rate_Type:
                        Rate_Type[rate_type] = new_prices[i]
                sys.stdout.write("Rate types and prices updated successfully.\n")

        # Asking user if they want to run the code again or exit
        while True:
            sys.stdout.write("Do you want to run the operation again? (yes/no) \n")
            answer = sys.stdin.readline().strip().lower()
            if answer == 'yes':
                main()
            elif answer == 'no':
                sys.stdout.write("Exiting the system...\n")
            else:
                sys.stdout.write("Invalid input entered, please try again.\n")

# Function to display list of the customers
def Get_Customers():
    sys.stdout.write("Existing Customers  :\n")
    # for loop runs through customers list and prints every customer name
    for customer in Customers:
        sys.stdout.write(customer +"\n")

# Function to display locations from the list
def Get_Locations():
    sys.stdout.write("Existing Locations:\n")
    #for loop runs through Location list and prints every Locations in the list
    for location in Locations:
        sys.stdout.write(location +" \n")

def Get_Rates():
    sys.stdout.write("Existing Rate Types:\n")
    for rate_type, price in Rate_Type.items():
        sys.stdout.write(f"{rate_type}: {price:.2f} (AUD per km)\n")


# This function is used to add a new location to the location list
def Add_Location():
    sys.stdout.write("Enter new locations (comma-separated): \n")
    location_input = sys.stdin.readline().strip()
    new_locations = [location.strip() for location in location_input.split(',')]

    added_locations = []

    for new_location in new_locations:
        if new_location not in Locations and new_location not in added_locations:
            Locations.append(new_location)
            added_locations.append(new_location)
            sys.stdout.write(f"Location '{new_location}' added successfully.\n")
        elif new_location in added_locations:
            sys.stdout.write(f"Location '{new_location}' has already been added in this session.\n")
        else:
            sys.stdout.write(f"Location '{new_location}' already exists. Not added.\n")


# This function gives the most valuable customer based on the booking history
def Valuable_Customer():
    customer_spending = {}  # Dictionary to store total spending for each customer

    for trip in Trips_of_Customer:  # this for loop check the list of Trips_of_Customer
        customer = trip[0]
        total_cost = trip[3]
        if customer in customer_spending:   
            customer_spending[customer] += total_cost
        else:
            customer_spending[customer] = total_cost

    most_valuable_customers = []        # Created an empty list to store the values
    max_spending = 0                    # Initializing a variable to zero to store the spending

    for customer, spending in customer_spending.items():    # this for loop check the most valuable customer
        if spending > max_spending:
            max_spending = spending
            most_valuable_customers = [customer]
        elif spending == max_spending:
            most_valuable_customers.append(customer)

    if most_valuable_customers:
        sys.stdout.write("Most Valuable Customer(s): \n")
        for customer in most_valuable_customers:
            sys.stdout.write(f"{customer}: {customer_spending[customer]:.2f} (AUD) \n")
    else:
        sys.stdout.write("No customer has made any trips. \n")


# Main loop
def main():
    while True:
        print("")
        sys.stdout.write("############################## Welcome to RMIT taxi management system ##############################")
        #sys.stdout.write("##########################################################################################\n")
        sys.stdout.write("\nMenu:\n")
        sys.stdout.write("1. Book a trip\n")
        sys.stdout.write("2. Add/update rate types and prices\n")
        sys.stdout.write("3. Display existing customers\n")
        sys.stdout.write("4. Display existing locations\n")
        sys.stdout.write("5. Display existing rate types\n")
        sys.stdout.write("6. Add new locations\n")
        sys.stdout.write("7. Display the most valuable customer\n")
        sys.stdout.write("8. Display customer booking history\n")
        sys.stdout.write("9. Exit the program\n\n")
        sys.stdout.write("##########################################################################################\n\n")


        

        sys.stdout.write("Select an option: \n")
        choice = sys.stdin.readline().strip()

        if choice == '1':
            book_trip()

        elif choice == '2':
            New_Rate_type()

        elif choice == '3':
            Get_Customers()

        elif choice == '4':
            Get_Locations()

        elif choice == '5':
            Get_Rates()

        elif choice == '6':
            Add_Location()

        elif choice == '7':
            Valuable_Customer()

        elif choice == '8':
            History()    

        elif choice == '8':
            sys.stdout.write("Exiting the program.\n")
            break

        else:
            sys.stdout.write("Invalid selection. Select the correct option from the menu.\n")

        sys.stdout.write("Would you like to continue using the system? (yes/no): \n")
        continue_option = sys.stdin.readline().strip()

        if continue_option.lower() != 'yes':
            sys.stdout.write("Exiting the program.\n")
            break
        
if __name__ == '__main__':
    main()