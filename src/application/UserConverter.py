
from dataclasses import asdict
from src.data.User import User

class UserConverter:

    def __init__(self) -> None:
        pass

    #TODO maybe encrypt password
    def dict_to_object(self,dict):
        return User(**dict)

    def object_to_dict(self,user:User):
        return asdict(user)

    def database_tuple_to_object(self,user_tuple):
        if user_tuple is None:
            return None
            
        keys = ('name','email','password')
        input_data = dict(zip(keys,user_tuple[1:])) #dont take id field, set later
        user = User(**input_data)
        user.set_id(user_tuple[0]) #event_id is in tuple[0], then its host,name....
        return user

