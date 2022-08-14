


import random
import time


class User:
    def __init__(self,name,email,password) -> None:
        self.name:str = name
        self.email:str = email
        self.__password:str = password
        self.id = int(str(time.time()) + str(random.randrange(0,9)) + str(random.randrange(0,9)))#internal ID, unique for each event, random number is to guarantee uniqueness
        
    def set_password(self,password):
        self.__password = password

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

    def __str__(self):
        return f"{self.name} - {self.email}"
    
