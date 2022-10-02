
from dataclasses import dataclass
from sre_parse import State

@dataclass
class Address:
    #in DB id is the first attribute
    street:str
    house_number:int
    city:str
    state:str  
    zip_code :int 
    complement:str = None
    id:int = None
    def __post_init__(self):
        if self.id is None:
            self.id = int(str(self.zip_code) + str(self.house_number)) #id is unique for each address (zip_code + house_number)

    def get_street(self):
        return self.street

    def set_street(self,street):
        self.street = street

    def get_house_number(self):
        return self.house_number

    def set_house_number(self,house_number):
        self.house_number = house_number


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