from Data.Location import Location


class Package:

    """this class is the package class, it stores all the values of the package"""
    # constructor
    def __init__(self, package_id_number, delivery_location, delivery_deadline, delivery_weight, special_notes):
        self.package_id_number = package_id_number
        self.delivery_location = delivery_location
        self.delivery_deadline = delivery_deadline
        self.package_weight = delivery_weight
        self.special_notes = special_notes
        if self.special_notes == "":
            self.special_notes = "No Special Note"
        self.delivery_status = "AT_HUB"
        self.drop_off_timestamp = "Not Delivered Yet"
        self.enroute_timestamp = None
        self.truck_number = None

    def __repr__(self):
        string = "Package({},{},{},{},{})"
        return string.format(self.package_id_number, self.delivery_location, self.delivery_deadline, self.package_weight, self.special_notes)
    # formats the package to readable string
    def __str__(self):
        string = "Package ID: {}, Truck ID: {}, Delivery Location: {}, Delivery Deadline: {}, Package Weight: {}, Special Notes: {}, Delivery Status: {}, Delivered At: {}"
        return string.format(self.package_id_number, self.truck_number, self.delivery_location, self.delivery_deadline,
                             self.package_weight, self.special_notes, self.delivery_status, self.drop_off_timestamp)

    #returns the special notes
    def get_special_notes(self):
        return self.special_notes

    # returns package id
    def get_package_id_number(self):
        return self.package_id_number

    # returns the delivery deadline
    def get_delivery_deadline(self):
        return self.delivery_deadline

    # returns the weight of the package
    def get_package_weight(self):
        return self.package_weight

    # gets the delivery status
    def get_delivery_status(self):
        return self.delivery_status

    def get_enroute_timestamp(self):
        return self.enroute_timestamp

    # returns the drop off timestamp
    def get_drop_off_timestamp(self):
        return self.drop_off_timestamp

    # gets the truck the package was on
    def get_truck_number(self):
        return self.truck

    # returns current location
    def get_current_location(self):
        return self.current_location

    # returns delivery location
    def get_delivery_location(self):
        return self.delivery_location

    # sets the delivery deadline
    def set_delivery_deadline(self, delivery_deadline):
        self.delivery_deadline = delivery_deadline

    # sets the delivery status
    def set_delivery_status(self, delivery_status):
        self.delivery_status = delivery_status

    # set delivery location
    def set_delivery_location(self, delivery_location):
        self.delivery_location = delivery_location

    # set package weight
    def set_package_weight(self, package_weight):
        self.package_weight = package_weight

    # set package id number
    def set_package_id_number(self, package_id_number):
        self.package_id_number = package_id_number

    def set_enroute_timestamp(self, enroute_timestamp):
        self.enroute_timestamp = enroute_timestamp

    # sets the drop off time stamp
    def set_drop_off_timestamp(self, drop_off_timestamp):
        self.drop_off_timestamp = drop_off_timestamp

    # sets the truck it was on
    def set_truck_number(self, truck_number):
        self.truck_number = truck_number

    # sets the current location
    def set_current_location(self, current_location):
        self.current_location = current_location