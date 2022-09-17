
from dataclasses import dataclass
import datetime
import time
from typing import List
from datetime import date
from src.data.User import User
from src.data.Address import Address
import random

@dataclass
class Event:

    host:User 
    name:str 
    address:Address 
    start_date:date 
    end_date:date 
    visibility:bool #True if public, False if private
    check_in:time 
    check_out:time 
    event_parent:"Event" = None
    list_of_participants:List[str] = None # list of emails of the participants
    id:int = int(str(int(time.time()*10)) + str(random.randrange(0,9)) + str(random.randrange(0,9))) #internal ID, unique for each event, random number is to guarantee uniqueness
    
        
    def __post_init__(self):
        #TODO, is this the right place to do this processing?
        self.start_date = datetime.datetime.strptime(self.start_date, '%Y-%m-%d') if isinstance(self.start_date, str) else self.start_date
        self.end_date = datetime.datetime.strptime(self.end_date, '%Y-%m-%d') if isinstance(self.end_date, str) else self.end_date
        self.check_in = datetime.datetime.strptime(self.check_in, '%H:%M') if isinstance(self.check_in, str) else self.check_in
        if self.check_out=="":
            self.check_out = None
        else:
            self.check_out = datetime.datetime.strptime(self.check_out, '%H:%M') if isinstance(self.check_out, str) else self.check_out
        self.event_parent = None if self.event_parent == "" else self.event_parent
        self.list_of_participants = [] if self.list_of_participants == "" or self.list_of_participants == None else self.list_of_participants

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
        return self.list_of_participants

    def add_participant(self,user):
        self.list_of_participants.append(user)

    def remove_participant(self,user):
        self.list_of_participants.remove(user)

    def get_host(self):
        #TODO careful, returning not a copy of the object
        return self.host

    def get_id(self):
        return self.id
        
    def set_id(self,id):
        self.id = id

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


