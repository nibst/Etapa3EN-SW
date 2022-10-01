

from src.data.Event import Event
from src.data.User import User
from src.data.dao.EventDao import EventDao
from src.application.event_validation import validate_event
from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.dao.AddressDao import AddressDao
from src.application.EventConverter import EventConverter

class EventService:

    def __init__(self):
        pass


    #TODO dont destroy db connection every single time (it kills the purpose of singleton)
    #TODO get events methods are so similiar, maybe there is a pattern to make this code looks cleaner, maybe a class for queries?
    def save(self,event:Event):
        """
        process input data,create event object and insert in db
        """
        address = event.get_address()
        address_dao = AddressDao()
        if address_dao.get_address_by_id(address.get_id()) is None: #if address is not in database
            address_dao.insert_address(address)
        event_dao = EventDao() 
        try:
            validate_event(event)
        except Exception as e:
            DBConnectionSingleton.rollback()
            raise(e)
        else:
            try:
                event_dao.insert_event(event)
            except Exception as e:
                DBConnectionSingleton.rollback()
                raise(e)
        return event
     
    def get_events(self):
        event_dao = EventDao() 
        events = []
        event_converter = EventConverter()

        try:
            event_dao.print_all_events()
            events_tuples=event_dao.get_all_events()
            for event_tuple in events_tuples:
                event = event_converter.database_tuple_to_object(event_tuple)
                events.append(event)
        except Exception as e:
            DBConnectionSingleton.rollback()
            raise (e)
        else:
            return events


        
    def get_events_by_name(self,name:str):
        event_dao = EventDao() 
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
            DBConnectionSingleton.rollback()
            raise (e)
        else:
            return events

    def get_events_by_host(self,user:User):
        """
        get events that user will host or have hosted
        """
        event_dao = EventDao()
        events_tuples = event_dao.get_events_by_host(user.get_id())
        event_converter = EventConverter()
        events = []
        for event in events_tuples:
            events.append(event_converter.database_tuple_to_object(event))
        return events

    def get_events_by_participant(self,user:User):
        """
        get events that user will attend or have attended
        """
        event_dao = EventDao()
        events_tuples = event_dao.get_events_by_participant(user.get_id())
        event_converter = EventConverter()
        events = []
        for event in events_tuples:
            events.append(event_converter.database_tuple_to_object(event))
        return events
