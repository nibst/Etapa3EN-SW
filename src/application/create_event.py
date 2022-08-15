
from src.data.Event import Event
from src.data.Address import Address
from datetime import date, time
from src.data.dao.EventDao import EventDaoSingleton
from src.application.event_validation import validate_event

#TODO, maybe do in a class?

def __process_date(date):
    return date.split('-')

def __process_time(time):
    return time.split(':')

def __process_visibility(visibility):
    return True if visibility == 'public' else False

def __process_participants(participants):
    return participants.split(',')
 
def __process_optional_field(optional_field:str,input_data:dict,default_value=None):
    if optional_field in input_data:
        return input_data[optional_field][0]
    else:
        return default_value
def create_event(host,input_data:dict):
    """
    process input data and create event object
    """
    event_dao  = EventDaoSingleton.get_event_dao()
    

    name = input_data['name'][0]

    string_start_date = __process_date(input_data['date_start'][0])
    start_date = date(int(string_start_date[0]),int(string_start_date[1]),int(string_start_date[2]))

    string_end_date = __process_date(input_data['date_end'][0])
    end_date = date(int(string_end_date[0]),int(string_end_date[1]),int(string_end_date[2]))
    
    time_start = __process_optional_field('time_start',input_data)
    if time_start: #if time_start is not None
        string_time_start = __process_time(time_start)
        time_start = time(int(string_time_start[0]),int(string_time_start[1]))
    time_end = __process_optional_field('time_end',input_data)
    if time_end: #if time_end is not None
        string_time_end = __process_time(time_end)
        time_end = time(int(string_time_end[0]),int(string_time_end[1]))
    apartment = __process_optional_field('apartment',input_data)
    complement = __process_optional_field('complement',input_data)
    parent = __process_optional_field('parent',input_data)
    invited_users =__process_optional_field('invited_users',input_data,default_value=[])
    
    
    address = Address(input_data['street'][0],input_data['city'][0],input_data['state'][0],input_data['house-number'][0],input_data['zip-code'][0] ,apartment,complement)
    
    visibility = __process_visibility(input_data['visibility'][0])
    event = Event(host,name,address,start_date,end_date,visibility,time_start,time_end,parent,invited_users) 
    try:
        validate_event(event)
    except Exception as e:
        print(e)
        return None
    else:
        try:
            event_dao.insert_event(event)
        except Exception as e:
            print(e)
            return None
        try:
            event_dao.print_all_events()
        except Exception as e:
            print("NO EVENTS YET")
    finally:
        EventDaoSingleton.destroyer()
    return event
     