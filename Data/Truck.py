# Name: Steven Holevas | ID: 001088230

from DataStructures.HashTable import HashTable
from Algorithms.Dijkstra import Dijkstra
from DataStructures.PriorityQueue import PriorityQueue

from collections import namedtuple


class Truck:
    """this is the truck class, it keeps track of the mileage and the packages on the truck"""
    # static variables to keep track of certain known variables
    total_truck_mileage = 0
    total_amount_of_mileage_allowed_to_drive = 0
    average_miles_per_hour = 18
    trucks = []

    # constructor
    # takes in the status, the list of packages, and the current location of the truck
    # average miles per hour is set to 18 because it is a known factor
    def __init__(self, status=None, current_location=None, packages=None, graph=None):
        self.status = status
        self.packages = packages
        self.current_location = current_location
        self.weight_hash_table = HashTable()
        self.current_mileage = 0
        self.destination_location = None
        self.home_location = self.current_location
        self.graph = graph
        self.departure_time = "HAS NOT DEPARTED YET"
        self.finished_time = "HAS NOT FINISHED YET"

    # to string method reveals all information about truck.
    def __str__(self):
        string_truck_status = "Status : {}, Departure Time: {}, Finished Time: {}, Location: {}," \
                 " Next Destination: {}, Miles Allowed to Drive: {}, Miles Driven: {} \n\nPACKAGES LEFT ON THIS TRUCK: {}\n"

        string_packages = ""
        for package in self.packages:
            string_packages += "\n{}".format(package)

        if string_packages == "":
            string_packages = "There are no packages left on this truck."


        return string_truck_status.format(self.status, self.departure_time, self.finished_time, self.current_location,
                             self.destination_location, self.total_amount_of_mileage_allowed_to_drive,
                             self.current_mileage, string_packages)

    # adds to the total truck mileage and the current mileage of this specific truck
    def add_truck_mileage(self, number_of_miles):
        self.current_mileage += float(number_of_miles)
        Truck.total_truck_mileage += float(number_of_miles)

    # adds package to list
    def add_package(self, package):
        self.packages.append(package)

    # adds truck to the static list of trucks
    @staticmethod
    def add_truck(truck):
        return Truck.trucks.append(truck)

    # changes the time_stamp of the package given, to the timestamp given
    def change_drop_off_time_stamp(self, package, time_stamp):
        package.set_drop_off_timestamp(time_stamp)

    # changes the time_stamp of the package given, to the timestamp given
    def change_enroute_time_stamp(self, package, time_stamp):
        package.set_enroute_timestamp(time_stamp)

    # changes the package status to delivered
    def change_package_status_to_delivered(self, package):
        package.set_delivery_status("DELIVERED")

    # changes package status to in transit
    def change_package_status_to_in_transit(self, package):
        package.set_delivery_status("IN_TRANSIT")

    @staticmethod
    # calculates the end time of the app. This method calculates the end time by
    # taking the amount of total amount of mileage allowed to drive and
    # using the time = distance/speed to obtain the mileage returns string
    def calculate_end_time():
        max_mileage = Truck.get_total_amount_of_mileage_allowed_to_drive()
        speed = float(Truck.average_miles_per_hour)
        distance = max_mileage
        speed = float(Truck.average_miles_per_hour)
        distance = max_mileage
        time = float(distance / speed)
        string_time = "{}".format(time)
        string_time = string_time.split(".")
        hours, minutes = string_time
        minutes = "." + minutes
        hours = 8 + int(hours)
        minutes = int(60 * float(minutes))
        if (minutes < 10):
            minutes = "{}{}".format(0, minutes)
        time = "{}:{}".format(hours, minutes)
        return time

    # calculates the current time by taking the miles per hour of each truck
    #  and the distance of the point to achieve the time (time = distance/speed)
    #  then adds 8 to the value for hours (which is the start point) and multiplies the minutes by 60
    #  to achieve the approximate minutes gone by.
    def calculate_time(self):
        speed = float(Truck.average_miles_per_hour)
        distance = self.current_mileage
        time = float(distance/speed)
        string_time = "{}".format(time)
        string_time = string_time.split(".")
        hours, minutes = string_time
        minutes = "." + minutes
        hours = 8 + int(hours)
        minutes = int(60 * float(minutes))
        if(minutes < 10):
            minutes = "{}{}".format(0, minutes)
        time = "{}:{}".format(hours, minutes)
        return time

    @staticmethod
    # calculates the trucks max distance by getting the hours and minutes
    def calculate_max_truck_distance(hours, minutes):
        max_distance_allowed_per_truck = ((hours - 8) * 18) + (float(minutes / 60) * 18)
        Truck.set_total_amount_of_mileage_allowed_to_drive(max_distance_allowed_per_truck)

    # this method performs all the actions that are needed to deliver a package
    def deliver_package(self, package):
        # changes package to delivered
        self.change_package_status_to_delivered(package)
        # calculates the current time
        time = self.calculate_time()
        # changes the drop_off_time
        self.change_drop_off_time_stamp(package, time)
        # removes package from list.
        self.packages.remove(package)

    # This class performs all the actions that are needed to enroute a package.
    def enroute_package(self, package):
        # changes package status to in transit
        self.change_package_status_to_in_transit(package)
        # # sets enroute time
        # self.change_enroute_time_stamp(package, "")
        # self.add_package(package)

    # returns average miles per hour
    def get_average_miles_per_hour(self):
        return self.average_miles_per_hour

    # returns the current location
    def get_current_location(self):
        return self.current_location

    # gets the instance's current mileage
    def get_current_mileage(self):
        return self.current_mileage

    def get_destination_location(self):
        return self.destination_location

    # gets statics total mileage
    @staticmethod
    def get_total_truck_mileage():
        return Truck.total_truck_mileage

    # returns the packages
    def get_packages(self):
        return self.packages

    # returns the status of the truck
    def get_status(self):
        return self.status

    # gets list of trucks
    @staticmethod
    def get_trucks():
        return Truck.trucks

    # returns true or false if the truck has a package that goes to the address given in the parameter
    def has_package(self, address, package_hash_table):
        for package_number in range(package_hash_table.get_number_of_elements()):

            package_address = str(package_hash_table[str(package_number + 1)].get_delivery_location().get_address())

            current_package = package_hash_table[str(package_number + 1)]

            if package_address == address and self.packages.__contains__(current_package):
                return True, current_package
        return False, None
        # self.deliver_package(current_package)

    # sets the current location
    def set_current_location(self, current_location):
        self.current_location = current_location

    # sets the packages
    def set_packages(self, packages):
        self.packages = packages

    # sets the status
    def set_status(self, status):
        self.status = status
    # sets destination location
    def set_destination_location(self, destination_location):
        self.destination_location = destination_location

    # sets amount of miles allowed to drive
    @staticmethod
    def set_total_amount_of_mileage_allowed_to_drive(total_mileage):
        Truck.total_amount_of_mileage_allowed_to_drive = total_mileage

    # gets total amount of mileage allowed to drive
    @staticmethod
    def get_total_amount_of_mileage_allowed_to_drive():
        return Truck.total_amount_of_mileage_allowed_to_drive

    # this algorithm takes the list of packages and orders them based on the nearest neighboring location
    # starting from the hub's location.

    # B1: ALGORITHM PSUEDOCODE
    # 1. current address = starting location
    #
    # 2. while # of packages in truck != 0
    #
    # 3. set lowest weight = infinity
    #
    # 4. for packages in package list
    #
    #  5. set destination =  package destination
    #
    #  6. perform dijkstra's algorithm to obtain the path weight of the package
    #
    #  7. if path weight < lowest weight then lowest weight = weight and get index of package
    #
    #  8. else, repeat for loop (steps 4-8)
    #
    #  9. pop package with index of lowest weight
    #
    #  10. add popped package in new list
    #
    #  11. package[weight] = lowest weight
    #
    #  12. current address = popped packages address
    #
    #  13. repeat while loop (steps 2-13)
    #
    #  14. sets trucks list of packages = new package list
    #
    # B3: SPACE TIME AND BIG-O
    # WORST CASE TIME COMPLEXITY: O(N2 + (|E| + |V|log|V|)) WHERE N IS # OF PACKAGES, E IS # EDGES, V IS # OF VERTICIES
    # WORST CASE SPACE COMPLEXITY: O(N) WHERE N IS THE NUMBER OF PACKAGES
    def prioritize_packages(self):
        """puts packages in order of closest neighbor order"""
        # declare variables
        list_of_packages = []
        dijkstra = Dijkstra()
        current_address = self.get_current_location().__str__()

        while len(self.packages) != 0:
            # lowest weight = infintity
            lowest_weight = float("infinity")
            # abritrary index to start off with that will throw error
            index = -1

            for package in self.packages:
                # new destination address
                destination_address = package.get_delivery_location().__str__()
                # performs dijkstra's to grab path and total weight of path weight of a package
                result = dijkstra.dijkstra_shortest_path_with_endpoints(self.graph, current_address, destination_address)
                places, path_weight = result

                # if this packages path weight is the smallest, take note of it and set the lowest value to it's weight
                if path_weight < lowest_weight:
                    lowest_weight = path_weight
                    index = self.packages.index(package)

            # grab package element from the lowest packages index given above
            package = self.packages.pop(index)
            # add package to new list
            list_of_packages.append(package)
            # grab hashtable package_id
            package_id = "{}".format(package.get_package_id_number())
            # weight for package is stored
            self.weight_hash_table[package_id] = lowest_weight
            # current address = packages delivery location [successful delivery]
            current_address = package.get_delivery_location().__str__()
        # reset instance variable
        self.packages = list_of_packages

        for package in self.packages:
            self.enroute_package(package)

    # this method performs a simulated drive to the addresses
    def drive(self):

        truck_has_mileage_left = True

        # while the the truck still has mileage and the truck still has packages
        while truck_has_mileage_left and len(self.packages) > 0:
            # set truck status
            self.set_status("IN_TRANSIT")
            # get's first package on the truck [closest package enroute]
            package_id_number = self.packages[0].get_package_id_number()
            # gets the weight based on the package_id
            weight = self.weight_hash_table[package_id_number]
            # sets the destination location to the packages delivery location
            self.set_destination_location(self.set_destination_location(self.packages[0].get_delivery_location()))

            # if total mileage > max_mileage
            if self.get_current_mileage() + weight <= Truck.get_total_amount_of_mileage_allowed_to_drive():

                # if the departure time of truck is has not departed
                # calculate time and set it.
                if self.departure_time == "HAS NOT DEPARTED YET":
                    time = self.calculate_time()
                    self.departure_time = time

                # current location becomes package location
                self.set_current_location(self.packages[0].get_delivery_location())
                #  add mileage to current mileage
                self.add_truck_mileage(weight)
                # delivers closest package
                self.deliver_package(self.packages[0])

            # if the mileage > max_mileage break
            elif self.get_current_mileage() + weight > Truck.get_total_amount_of_mileage_allowed_to_drive():
                truck_has_mileage_left = False

        # performs dijkstra to calculate how far home location is
        dijkstra = Dijkstra()
        addresses, weight = dijkstra.dijkstra_shortest_path_with_endpoints(self.graph,
                                                                           self.get_current_location().__str__(),
                                                                           self.home_location.__str__())
        #  if location distance < max_mileage go home
        if(truck_has_mileage_left and len(self.packages) == 0
        and Truck.get_total_amount_of_mileage_allowed_to_drive() >= self.current_mileage + weight):
            self.add_truck_mileage(weight)
            self.set_current_location(self.home_location)
            self.set_destination_location(self.get_current_location())
            self.status = "AT_HUB"
            time = self.calculate_time()
            self.finished_time = time

    @staticmethod
    # manually controls driving and wait times
    def control_driving():
        trucks = Truck.get_trucks()

        trucks[0].drive()
        # truck 2 waits until 9:05 to depart
        trucks[1].current_mileage = 19.8
        trucks[1].drive()
        #  subtract because it did not actually travel 19.8 miles, it used the 19.8 miles to get acccurate times
        # for packages
        trucks[1].current_mileage -=19.8

        # if truck one made it back, drive truck 3
        if trucks[0].status == "AT_HUB" or trucks[1].status == "AT_HUB":
            trucks[2].current_mileage = trucks[0].current_mileage
            trucks[2].drive()
            trucks[2].current_mileage -= trucks[0].current_mileage

            # these if ... else if statements compare both other trucks [truck 1 and truck 2]
            # and if both are at the hub [meaning route finished], compare mileage,
            # and send truck 3 out with lowest mileage from truck 1 or truck 2

            # if trucks[0].status == "AT_HUB" and trucks[1].status =="AT_HUB" and trucks[2].status =="AT_HUB" \
            #         and trucks[0].current_mileage < trucks[1].current_mileage:
            #     trucks[2].current_mileage = trucks[0].current_mileage
            #     trucks[2].drive()
            #     trucks[2].current_mileage -= trucks[0].current_mileage
            #
            # elif trucks[0].status == "AT_HUB" and trucks[1].status =="AT_HUB" and trucks[2].status =="AT_HUB" \
            #         and trucks[0].current_mileage > trucks[1].current_mileage:
            #     trucks[2].current_mileage = trucks[1].current_mileage
            #     trucks[2].drive()
            #     trucks[2].current_mileage -= trucks[1].current_mileage

    # has mileage left to drive returns bool based on if it has mileage left to drive
    def has_mileage_left_to_drive(self, weight):
        return self.get_current_mileage() + weight <= Truck.get_total_amount_of_mileage_allowed_to_drive()