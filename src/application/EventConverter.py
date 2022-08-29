
from src.data.Event import Event
from src.data.Address import Address


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
            
    def input_to_event_object(self,input_data:dict):
        """
        process input data and create event object
        """
        #copy of input data, just to make sure
        input_data = dict(input_data)
        
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

    #TODO
    def event_to_input_dict(self,event:Event):
        pass