
import time
from typing import List
from datetime import date
from src.data.User import User
from src.data.Address import Address
import random
class Event:
    def __init__(self,host,name,address,start_date,end_date,event_visibility, check_in,check_out, event_parent = None, list_of_participants_ids = []) -> None:
        self.host:User = host
        self.name:str = name
        self.address:Address = address
        self.start_date:date = start_date
        self.end_date:date = end_date
        self.visibility:bool = event_visibility #True if public, False if private
        self.check_in:time = check_in
        self.check_out:time = check_out
        self.event_parent:Event = event_parent #one event can be a child of another event (sub-event)
        self.list_of_participants_ids:List[int] = list_of_participants_ids #external ID from user
        self.id = int(str(time.time()) + str(random.randrange(0,9)) + str(random.randrange(0,9))) #internal ID, unique for each event, random number is to guarantee uniqueness

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def set_address(self,address):
        self.address = address

    def get_address(self):
        #TODO careful, returning not a copy of the object
        return self.address

    def set_start_date(self,date):
        self.start_date = date
    
    def get_start_date(self):
        #TODO careful, returning not a copy of the object
        return self.start_date
    
    def set_end_date(self,date):
        self.end_date = date
    
    def get_end_date(self):
        #TODO careful, returning not a copy of the object
        return self.end_date

    def get_visibility(self):
        return self.visibility

    def get_list_of_participants(self):
        #TODO careful, returning not a copy of the object
        return self.list_of_participants_ids

    def add_participant(self,user_id):
        self.list_of_participants_ids.append(user_id)

    def remove_participant(self,user_id):
        self.list_of_participants_ids.remove(user_id)

    def get_host(self):
        #TODO careful, returning not a copy of the object
        return self.host

    def get_id(self):
        return self.id

    def get_event_parent(self):
        #TODO careful, returning not a copy of the object
        return self.event_parent

    def set_event_parent(self,event_parent):
        self.event_parent = event_parent

    def get_check_in(self):
        #TODO careful, returning not a copy of the object
        return self.check_in

    def set_check_in(self,check_in):
        self.check_in = check_in

    def get_check_out(self):
        #TODO careful, returning not a copy of the object
        return self.check_out

    def set_check_out(self,check_out):
        self.check_out = check_out

    def __str__(self) -> str:
        return f"""
host: {self.host} 
name: {self.name}
address: {self.address}
date: {self.start_date} - {self.end_date}
visibility: {self.visibility} 
participants: {self.list_of_participants}"""
