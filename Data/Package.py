from Data.Location import Location
class Package():

    def __init__(self, package_id_number, delivery_location, delivery_deadline, delivery_weight, special_notes):
        self.package_id_number = package_id_number
        # self.delivery_address = None
        self.delivery_location = delivery_location
        self.delivery_deadline = delivery_deadline
        self.package_weight = delivery_weight
        self.special_notes = special_notes
        self.current_location = None
        # self.delivery_city = None
        # self.delivery_zip_code = None

        self.delivery_status = None

        self.pick_up_timestamp = None
        self.drop_off_timestamp = None
        self.truck = None
        self.truck_driver = None


        self.priority_number = None

    def __str__(self):
        string = "Package ID: {} | Delivery Location: {} | Delivery Deadline: {} | Package Weight: {} | Special Notes: {}"
        return string.format(self.package_id_number, self.delivery_location, self.delivery_deadline, self.package_weight, self.special_notes)

    def get_package_id_number(self):
        return self.package_id_number

    # def get_delivery_address(self):
    #     return self.delivery_address

    def get_delivery_deadline(self):
        return self.delivery_deadline

    # def get_delivery_city(self):
    #     return self.delivery_city

    # def get_delivery_zip_code(self):
    #     return self.delivery_zip_code

    def get_package_weight(self):
        return self.package_weight

    def get_delivery_status(self):
        return self.delivery_status

    def get_pickup_timestamp(self):
        return self.pick_up_timestamp

    def get_hashable(self):
        return self.delivery_location.get_zip_code()

    def get_priority_number(self):
        return self.priority_number

    def get_drop_off_timestamp(self):
        return self.drop_off_timestamp

    def get_truck(self):
        return self.truck

    def get_truck_driver(self):
        return self.truck_driver

    def get_current_location(self):
        return self.current_location

    def get_delivery_location(self):
        return self.delivery_location

    # def set_delivery_address(self, delivery_address):
    #     self.delivery_address = delivery_address
    #
    # def set_delivery_city(self, delivery_city):
    #     self.delivery_city = delivery_city

    def set_delivery_deadline(self, delivery_deadline):
        self.delivery_deadline = delivery_deadline

    def set_delivery_status(self, delivery_status):
        self.delivery_status = delivery_status

    # def set_delivery_zip_code(self, delivery_zip_code):
    #     self.delivery_zip_code = delivery_zip_code

    def set_delivery_location(self, delivery_location):
        self.delivery_location = delivery_location

    def set_package_weight(self, package_weight):
        self.package_weight = package_weight

    def set_package_id_number(self, package_id_number):
        self.package_id_number = package_id_number

    def set_pickup_timestamp(self, pickup_timestamp):
        self.pick_up_timestamp = pickup_timestamp

    def set_drop_off_timestamp(self, drop_off_timestamp):
        self.drop_off_timestamp = drop_off_timestamp

    def set_truck(self, truck):
        self.truck = truck

    def set_current_location(self, current_location):
        self.current_location = current_location

    def set_truck_driver(self, truck_driver):
        self.truck_driver = truck_driver

    def set_priority_number(self, priority_number):
        self.priority_number = priority_number





 # self.pick_up_timestamp = None
 # self.drop_off_timestamp = None
 # self.truck = None
 # self.current_location
