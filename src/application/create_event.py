
from src.data.Event import Event
from src.data.Address import Address
from datetime import date, time


#TODO, maybe do in a class?

def __process_date(date):
    return date.split('-')

def __process_time(time):
    return time.split(':')

def __process_visibility(visibility):
    return True if visibility == 'public' else False

def create_event(host,input_data:dict):
    """
    process input data and create event object
    """
    name = input_data['name'][0]

    string_start_date = __process_date(input_data['date_start'][0])
    start_date = date(int(string_start_date[0]),int(string_start_date[1]),int(string_start_date[2]))

    string_end_date = __process_date(input_data['date_end'][0])
    end_date = date(int(string_end_date[0]),int(string_end_date[1]),int(string_end_date[2]))

    time_start = None 
    time_end = None
    if 'time_start' in input_data:
        string_time_start = __process_time(input_data['time_start'][0])
        time_start = time(int(string_time_start[0]),int(string_time_start[1]))
    if 'time_end' in input_data:
        string_time_end = __process_time(input_data['time_end'][0])
        time_end = time(int(string_time_end[0]),int(string_time_end[1]))

    apartment = None
    complement = None
    if 'apartment' in input_data:
        apartment = input_data['apartment'][0]
    if 'complement' in input_data:
        complement = input_data['complement'][0]
    address = Address(input_data['street'][0],input_data['city'][0],input_data['state'][0],input_data['house-number'][0],apartment,complement)
    
    visibility = __process_visibility(input_data['visibility'][0])  

    return Event(host,name,address,start_date,end_date,visibility,time_start,time_end)
     