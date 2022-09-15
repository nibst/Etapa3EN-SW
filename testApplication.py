import unittest
from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.dao.UserDao import UserDao
from src.application.UserService import UserService
from src.application.EventService import  EventService
from src.data.Event import Event
from src.data.Address import Address
from src.data.User import User
from src.application.EventConverter import EventConverter
from datetime import date, time
from random import randint

class TestApplication(unittest.TestCase):
    #exemplo só
    def test_create_event(self):
        
        user = User('nibs','nikolasps7@gmail.com','senha123')
        user.set_id(166)
        event_service = EventService()
        Post = {'name': 'nibs event', 'start_date': '2022-09-17', 'end_date': '2022-09-22', 'check_in': '22:44', 'check_out': '00:44', 'visibility': 'public', 'street': 'Mario Leitao', 'house_number': '60', 'zip-code': '9069425', 'state': 'RS', 'city': 'Porto Alegre'}
        Post['host'] = user
        converter = EventConverter()
        event = converter.dict_to_object(Post)
        self.assertIsInstance(event_service.save(event), Event) # verifica se o retorno é do tipo Event
    def test_get_events(self):

        event_service = EventService()
        events = event_service.get_events()
        #[print(event.name) for event in events]
        self.assertIsInstance(events, list) # verifica se o retorno é uma lista
        self.assertIsInstance(events[0], Event) # verifica se o retorno é uma lista de eventos

    def test_get_events_by_name(self):
        name = 'nibs' 
        event_service = EventService()
        events = event_service.get_events_by_name(name)
        [print(event.name) for event in events]
        self.assertIsInstance(events, list) # verifica se o retorno é uma lista
        self.assertIsInstance(events[0], Event) # verifica se o retorno é uma lista de eventos

    def test_create_user(self):

        user_service = UserService()
        db_connection = DBConnectionSingleton.get_instance()
        name = 'nikolas'
        email = 'nikolas@gmail.com'
        password = '123'
        user_dao = UserDao(db_connection)
        user_dao.delete_by_email(email) #delete to create again
        user = User(name,email,password)
        DBConnectionSingleton.destroyer()
        user = user_service.create_user(user)
        self.assertIsInstance(user, User) # verifica se o retorno é do tipo User
        

if __name__ == '__main__':
    unittest.main()
