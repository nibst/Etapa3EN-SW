


from dataclasses import dataclass
import random
import time

@dataclass
class User:

    name:str 
    email:str
    password:str
    def __post_init__(self):
        self.id = int(str(int(time.time()*10)) + str(random.randint(0,9)) + str(random.randint(0,9)))#internal ID, unique for each event, random number is to guarantee uniqueness
        
    def set_password(self,password):
        self.password = password
        
    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def set_email(self,email):
        self.email = email
        
    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def get_id(self):
        return self.id
        
    def set_id(self,id):
        self.id = id
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    