# Name: Steven Holevas | ID: 001088230
class Location():
    """the location class takes in an address, city, state, and zip-code"""
    # constructor
    def __init__(self, address, city, state, zip_code):
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __repr__(self):
        string = " Address: {}, City: {}, State: {}, Zip: {}"
        return string.format(self.address, self.city, self.state,
                             self.zip_code)

    # the to string method, formats data into a readable string
    def __str__(self):
        string = "{}, {}, {}, {}"
        return string.format(self.address, self.city,self.state, self.zip_code)


    # returns the address
    def get_address(self):
        return self.address

    # returns the city
    def get_city(self):
        return self.city

    # returns the state
    def get_state(self):
        self.state

    # returns the zip code
    def get_zip_code(self):
        return self.zip_code

    # sets the address value
    def set_address(self, address):
        self.address = address

    # sets the city value
    def set_city(self, city):
        self.city = city

    # sets the state value
    def set_state(self,state):
        self.state = state

    # sets the zip code
    def set_zip_code(self, zip_code):
        self.zip_code = zip_code