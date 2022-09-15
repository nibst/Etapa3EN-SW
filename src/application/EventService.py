
import copy
from src.data.Event import Event
from src.data.Address import Address
from datetime import date, time
from src.data.dao.EventDao import EventDao
from src.application.event_validation import validate_event
from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.dao.AddressDao import AddressDao
from src.application.EventConverter import EventConverter

#TODO, maybe do in a class?




 


class EventService:

    def __init__(self):
        pass


    #TODO dont destroy db connection every single time (it kills the purpose of singleton)
    #TODO get events methods are so similiar, maybe there is a pattern to make this code looks cleaner, maybe a class for queries?
    def save(self,event:Event):
        """
        process input data,create event object and insert in db
        """
        db_connection  = DBConnectionSingleton.get_instance()
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
        return event
     
    def get_events(self):
        db_connection  = DBConnectionSingleton.get_instance()
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


        
    def get_events_by_name(self,name:str):
        db_connection  = DBConnectionSingleton.get_instance()
        event_dao = EventDao(db_connection) 
        events = []
        event_converter = EventConverter()
        #this address is an id of the address in the database, these are keys of the event object
        keys = ('host','name','address','start_date','end_date','visibility','check_in','check_out','event_parent','list_of_participants')
        try:
            events_tuples=event_dao.get_events_by_name(name)
            for event_tuple in events_tuples:
                event = event_converter.database_tuple_to_object(event_tuple)
                events.append(event)
        except Exception as e:
            raise (e)
        else:
            return events