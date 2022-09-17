
from dataclasses import asdict
from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.Event import Event
from src.data.Address import Address
from src.data.dao.AddressDao import AddressDao

class EventConverter:
    def __init__(self) -> None:
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
            
    def dict_to_object(self,input_data:dict):
        """
        process input data and create event object
        """
        #copy of input data, just to make sure
        input_data = dict(input_data)
        
        apartment = self.__process_optional_field('apartment',input_data)
        complement = self.__process_optional_field('complement',input_data)
        
        address = Address(input_data['street'],input_data['house_number'],input_data['city'],input_data['state'],input_data['zip-code'] ,apartment,complement)
        remove_keys = ('street','city','state','house_number','zip-code','apartment','complement') #remove these keys from input_data to use input_data as dict for event object
        input_data['address'] = address
        for key in remove_keys:
            input_data.pop(key,None)
        input_data['visibility']  = self.__process_visibility(input_data['visibility'])
        event = Event(**input_data)
        return event

    #TODO check if this works
    def object_to_dict(self,event:Event):
        return asdict(event)

    def database_tuple_to_object(self,event_tuple):
        #TODO this dont get all info, need info from table Participants
        #Later on, get the address using the address id from the event
        address_dao  = AddressDao(DBConnectionSingleton.get_instance())
        keys = ('id','host','name','address','start_date','end_date','visibility','check_in','check_out','event_parent','list_of_participants')
        event_input_data = dict(zip(keys,event_tuple))
        
        address_keys = ('id','street','house_number','city','state','zip_code','apartment','complement') 
        address_tuple = address_dao.get_address_by_id(event_input_data['address'])
        address_input_data = dict(zip(address_keys,address_tuple))
        address = Address(**address_input_data)
        event_input_data['address'] = address
        

        event = Event(**event_input_data)
        return event