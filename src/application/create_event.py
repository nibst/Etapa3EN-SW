
import copy
from src.data.Event import Event
from src.data.Address import Address
from datetime import date, time
from src.data.dao.EventDao import EventDao
from src.application.event_validation import validate_event
from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.dao.AddressDao import AddressDao
import sys
#TODO, maybe do in a class?




 


class EventService:

    def __init__(self):
        pass

    def __process_visibility(self,visibility:str):
        if visibility == 'public':
            return True
        elif visibility == 'private':
            return False
        else:
            raise ValueError("Invalid visibility")
    def __process_optional_field(self,optional_field:str,input_data:dict,default_value=None):
        if optional_field in input_data and input_data[optional_field] != '':
            return input_data[optional_field]
        else:
            return default_value
    #TODO maybe pass this method to another class 
    def input_to_event_object(self,input_data:dict):
        """
        process input data and create event object
        """
        apartment = self.__process_optional_field('apartment',input_data)
        complement = self.__process_optional_field('complement',input_data)
        
        address = Address(input_data['street'],input_data['city'],input_data['state'],input_data['house_number'],input_data['zip-code'] ,apartment,complement)
        remove_keys = ('street','city','state','house_number','zip-code','apartment','complement') #remove these keys from input_data to use input_data as dict for event object
        input_data['address'] = address
        for key in remove_keys:
            input_data.pop(key,None)
        input_data['visibility']  = self.__process_visibility(input_data['visibility'])
        event = Event(**input_data)
        return event

    def create_event(self,host,input_data:dict):
        """
        process input data,create event object and insert in db
        """
        db_connection  = DBConnectionSingleton.get_singleton()
        #copy input data dict, because we will remove some keys from it
        print(input_data, flush=True)
        input_data = dict(input_data)
        print(input_data, flush=True)
        input_data['host'] = host #TODO for now host is the only user and do not get passed with input_data
        print('oi', flush=True)
        event:Event = self.input_to_event_object(input_data)
        print(input_data, flush=True)
        address = event.get_address()
        address_dao = AddressDao(db_connection)
        if address_dao.get_address_by_id(address.get_id()) is None: #if address is not in database
            address_dao.insert_address(address)
        event_dao = EventDao(db_connection) 
        try:
            validate_event(event)
        except Exception as e:
            raise(e)
        else:
            try:
                event_dao.insert_event(event)
            except Exception as e:
                raise(e)
        finally:
            DBConnectionSingleton.destroyer()
        return event
     
    def get_events(self):
        db_connection  = DBConnectionSingleton.get_singleton()
        event_dao = EventDao(db_connection) 
        events = []
        #this address is an id of the address in the database
        keys = ('host','name','address','start_date','end_date','visibility','check_in','check_out','event_parent','list_of_participants')
        try:
            #TODO this dont get all info, need info from table Participants
            #Later on, get the address using the address id from the event
            events_tuples=event_dao.get_all_events()
            for event_tuple in events_tuples:
                input_data = dict(zip(keys,event_tuple[1:]))
                event = Event(**input_data)
                event.set_id(event_tuple[0])
                events.append(event)
        except Exception as e:
            raise (e)
        else:
            return events
        finally:
            DBConnectionSingleton.destroyer()