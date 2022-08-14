
from sre_parse import State


class Address:
    def __init__(self,street,city,state,house_number,zip_code,apartment = None,complement = None) -> None:
        self.id :int = int(str(zip_code) + str(house_number)) #id is unique for each address (zip_code + house_number),do not diferrentiate between same addresses with different apartment numbers
        self.street:str = street
        self.city:str = city
        self.state:str = state
        self.house_number:int = house_number
        self.zip_code :int = zip_code
        self.apartment:int = apartment
        self.complement:str = complement

    def get_street(self):
        return self.street

    def set_street(self,street):
        self.street = street

    def get_house_number(self):
        return self.house_number

    def set_house_number(self,house_number):
        self.house_number = house_number
    
    def get_apartment(self):
        return self.apartment
    
    def set_apartment(self,apartment):
        self.apartment = apartment
    
    def get_complement(self):
        return self.complement

    def set_complement(self,complement):
        self.complement = complement
    
    def get_city(self):
        return self.city
    
    def set_city(self,city):
        self.city = city
    
    def get_state(self):
        return self.state
    
    def set_state(self,state):
        self.state = state
    
    def get_zip_code(self):
        return self.zip_code
    
    def set_zip_code(self,zip_code):
        self.zip_code = zip_code
    
    def get_id(self):
        return self.id

    def __str__(self):
        return f"{self.street}, {self.house_number} - {self.city}, {self.state}"