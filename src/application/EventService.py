
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


    #TODO validate object on EventConverter maybe?
    def save(self,event:Event):
        """
        process input data,create event object and insert in db
        """
        db_connection  = DBConnectionSingleton.get_singleton()
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