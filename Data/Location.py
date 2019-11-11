class Location():
    def __init__(self, address, city, state, zip_code):
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __str__(self):
        string = "{}, {}, {}, {}"
        return string.format(self.address, self.city,self.state, self.zip_code)

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        self.state

    def get_zip_code(self):
        return self.zip_code


    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city

    def set_state(self,state):
        self.state = state

    def set_zip_code(self, zip_code):
        self.zip_code = zip_code