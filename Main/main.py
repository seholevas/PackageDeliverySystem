from Algorithms.PackagePlacer import PackageSort
from CSV.DataReader import DataReader
from Data.Location import Location
from Data.Package import Package
from Data.Truck import Truck


class main:

    # constructor
    def __init__(self):
        data_reader = DataReader()
        self.hashtable = data_reader.load_package_data_into_hash_table("../CSV/WGUPSPackageFile.csv")
        self.graph = data_reader.load_distance_data_into_graph("../CSV/WGUPSDeliveries.csv")

    # prompts the user for their first option
    def prompt_options(self):
        # local variable
        user_input = ""
        # while the user did not enter an acceptable input [1,2,3,4, or no]
        while user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4 and user_input.upper() != "no".upper():
            # prints out prompt for user to choose from
            print()
            print("welcome to the wgups services!".upper())
            print()
            print("please choose from the following options: ".upper())
            print("1. Look up package data".upper())
            print("2. insert new package".upper())
            print("3. print all package data, truck routes, and mileage data for a specific time".upper())
            print("4. quit program".upper())

            # attempts to get valid input from user.
            try:
                print()
                user_input = int(input("Select an option: ".upper()))
            # if it is not a number, throw exception and loop again
            except ValueError:
                print()
                print("what you entered is not a valid option, please type in a number corresponding to the option "
                      "you would like to perform".upper())
                continue
            # if it is a number, but not a given number, alert user and loop again
            if user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
                print()
                print("please choose a valid number that corresponds to an option".upper())
                continue
            # if user chooses a propper input, intiate new prompt
            self.perform_action(user_input)
            # if the user didn't want to quit the program, ask if they would
            # like to re-run the program.
            if user_input != 4:
                user_input = self.prompt_for_main_menu()

    # prompts user for input on whether or not they want to go back to the main menu
    def prompt_for_main_menu(self):
        # local variable for response
        valid = False

        # loops until user response is valid
        while not valid:
            print()
            # gets response
            yes_or_no = input("would you like to do something else (type: yes or no): ".upper())
            # warns user that they did not enter a valid response
            if (yes_or_no.upper() != "yes".upper() and yes_or_no.upper() != "no".upper()):
                print()
                print("user input is incorrect, please type in yes or no".upper())
                continue
            # else response is valid
            else:
                valid = True

        return yes_or_no
    # prompts user for input based on what option they chose [1,2,3]
    def perform_action(self, the_input):
        # gives user all package info
        if the_input == 1:
            self.prompt_look_up_package_data()
        # prompts user to insert a package
        elif the_input == 2:
            self.prompt_insert_package()
        # prompts user to input time for deliveries
        elif the_input == 3:
            self.prompt_for_deliveries()

    # prints out all package data in the order of package number
    def prompt_look_up_package_data(self):
        print()
        print("here is the data for all the packages:".upper())
        print()
        for i in range(self.hashtable.get_number_of_elements()):
            package_id = str(i+1)
            print(self.hashtable[package_id])

    # prompts user to insert info about new package
    def prompt_insert_package(self):
        # local variables
        user_input_delivery_street_address = None
        user_input_delivery_city = None
        user_input_delivery_state = None
        user_input_delivery_zip_code = None
        user_input_delivery_deadline = None
        user_input_delivery_weight = None
        user_input_delivery_special_notes = None
        # boolean local variable
        need_more_information = True

        while (need_more_information):

            print()
            print("before we insert a package, we need to know a few things about the package first".upper())

            # tries to get valid information to insert into a package
            try:
                user_input_delivery_street_address = input("what is the delivery street address: ".upper())
                user_input_delivery_city = input("what is the delivery city: ".upper())
                user_input_delivery_state = input("what is the delivery state abbreviation: ".upper())
                user_input_delivery_zip_code = int(input("what is the delivery street zip_code: ".upper()))
                user_input_delivery_deadline = input(
                    "what is the delivery deadline (write eod if there is no deadline): ".upper())
                user_input_delivery_weight = float(input("what is the mass of the package: ".upper()))
                user_input_delivery_special_notes = input(
                    "what special note would you like to attach to the package: ".upper())
            # if there is a value error, continues loop
            except ValueError:
                print("some of your input was not able to be computed, please try again".upper())
                continue

            # otherwise, got all information needed
            need_more_information = False

        # inserts package into hashtable
        string_package_id = "{}".format(self.hashtable.get_number_of_elements() + 1)
        package_delivery_location = Location(user_input_delivery_street_address, user_input_delivery_city,
                                             user_input_delivery_state, user_input_delivery_zip_code)

        self.hashtable[string_package_id] = Package(string_package_id, package_delivery_location,
                                                    user_input_delivery_deadline, user_input_delivery_weight,
                                                    user_input_delivery_special_notes)
        # prints package, to confirm to user they their package is in.
        print("package inserting complete, check out the information about the new package below".upper())
        print(self.hashtable[string_package_id])

    # this function prompts for a delivery cycle to occur
    def prompt_for_deliveries(self):
        # local boolean
        valid = False
        # local user input variable
        user_input_time = ""

        while not valid:
            # prompts user for time
            print()
            user_input_time = input("please enter a time in military time format (format example: 13:00): ".upper())
            hours = None
            minutes = None
            # if len != 5 [00:00]
            if (len(user_input_time) != 5):
                print()
                print("user input is not valid, there should be four numbers with a colon in between the numbers".upper())
                continue

            # attempts to get the value as ints
            try:
                time = user_input_time.split(':')
                hours = int(time[0])
                minutes = int(time[1])

                valid = True
            # throws error, if not ints and loops again
            except ValueError:
                print()
                print("please type in only integers in the hour and minute slots of your text".upper())
                continue

            # gets max distance
            Truck.calculate_max_truck_distance(hours, minutes)
            # adds trucks to the program to drive
            self.add_trucks()
            # sorts packages on each truck
            self.prompt_for_sorting_packages()
            # starts driving trucks
            self.prompt_for_driving()

            # prompts user with all truck infromation
            self.prompt_for_truck_information()
            # prompts user with all package data after driving
            self.prompt_look_up_package_data()
            # clears the information from csv file
            self.clear_information()

    # adds trucks and sets them up for the program
    def add_trucks(self):
        # sets default location
        home_location = Location("4001 South 700 East", "Salt Lake City", "UT", "84107")
        truck1 = Truck("AT_HUB", home_location, None, self.graph)
        truck2 = Truck("AT_HUB", home_location, None, self.graph)
        truck3 = Truck("AT_HUB", home_location, None, self.graph)
        # adds trucks to the list of trucks
        Truck.add_truck(truck1)
        Truck.add_truck(truck2)
        Truck.add_truck(truck3)

    # lets the user know that packages are being sorted,
    #  and sorts the packages
    def prompt_for_sorting_packages(self):
        print()
        print("Sorting Packages...".upper())
        psort = PackageSort()
        psort.package_sort(self.hashtable, Truck.get_trucks()[0], Truck.get_trucks()[1], Truck.get_trucks()[2])
        Truck.get_trucks()[0].prioritize_packages()
        Truck.get_trucks()[1].prioritize_packages()
        Truck.get_trucks()[2].prioritize_packages()
        print("packages sorted!".upper())

    # performs and lets the user know that the program is driving
    def prompt_for_driving(self):
        print()
        print("here is the truck information before driving: ".upper())
        print(Truck.trucks[0])
        print(Truck.trucks[1])
        print(Truck.trucks[2])
        print()
        print("Driving...".upper())
        Truck.control_driving()
        print("Driving Complete!".upper())

    # gives the user all the truck information needed
    def prompt_for_truck_information(self):
        print()
        print("Here is the Truck information after driving: ".upper())
        print()
        print("time that trucks are allowed to drive until: ".upper(), Truck.calculate_end_time())
        print()
        print(Truck.trucks[0])
        print(Truck.trucks[1])
        print(Truck.trucks[2])
        print("total amount of mileage driven: ".upper(), Truck.get_total_truck_mileage())

    # clears the information by recalling csv file for packages
    def clear_information(self):
        self.hashtable = DataReader.load_package_data("../CSV/WGUPSPackageFile.csv")


main = main()

main.prompt_options()
