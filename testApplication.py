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
        Post = {'name': 'nibs event', 'start_date': '2034-09-17', 'end_date': '2034-09-22', 'check_in': '22:44', 'check_out': '00:44', \
        'visibility': 'private', 'street': 'Rua 2', 'house_number': '60', 'zip_code': '9069425', 'state': 'RS', 'city': 'Porto Alegre', \
        'list_of_participants': 'emaildetesteparaevento@teste.eu,emaildetest36eparaevento@teste.eu'}
        Post['host'] = user
        converter = EventConverter()
        event = converter.dict_to_object(Post)
        self.assertIsInstance(event_service.save(event), Event) # verifica se o retorno é do tipo Event
    def test_get_events(self):

        event_service = EventService()
        events = event_service.get_events()
        [print(event) for event in events]
        self.assertIsInstance(events, list) # verifica se o retorno é uma lista
        self.assertIsInstance(events[0], Event) # verifica se o retorno é uma lista de eventos

    def test_get_events_by_name(self):
        print("TEST GET EVENT BY NAME")
        name = 'event name' 
        event_service = EventService()
        events = event_service.get_events_by_name(name)
        [print(event) for event in events]
        self.assertIsInstance(events, list) # verifica se o retorno é uma lista
        self.assertIsInstance(events[0], Event) # verifica se o retorno é uma lista de eventos

    def test_create_user(self):

        user_service = UserService()
        username = 'nikolas'
        email = 'nikolas@gmail.com'
        password = '123'
        user_dao = UserDao()
        user_dao.delete_by_email(email) #delete to create again
        user = User(username,email,password)
        DBConnectionSingleton.destroyer()
        user = user_service.create_user(user)
        self.assertIsInstance(user, User) # verifica se o retorno é do tipo User
    
    def test_login_valido(self):
        user_service = UserService()
        username = 'nikolas'
        email = 'emaildetesteparaevento@teste.eu'
        password = 'senha123'
        user = User(username,email,password)
        user = user_service.login(email,password)
        self.assertIsInstance(user, User) # verifica se o retorno é do tipo User
        try:
            user_service.login(email,'senha errada')
        except:
            self.assertTrue(True)#pass the test
        else:
            self.fail("Login should fail with exception")
    def test_get_events_by_host(self):
        event_service = EventService()
        
        user_id = 1234

        events = event_service.get_events_by_host(user_id)
        print("HOSTED EVENTS BY 1234")
        self.assertIsInstance(events, list) # verifica se o retorno é do tipo User
        for event in events:
            print(event)
            self.assertIsInstance(event, Event) # verifica se o retorno é do tipo User
    def test_get_events_by_participant(self):
        event_service = EventService()
    
        user_id = 1234

        events = event_service.get_events_by_participant(user_id)
        print("ATTENDED EVENTS BY 1234")
        self.assertIsInstance(events, list) # verifica se o retorno é do tipo User
        for event in events:
            print(event)
            self.assertIsInstance(event, Event) # verifica se o retorno é do tipo User

    def test_get_event_by_id(self):
        print("TEST GET EVENT BY ID")
        id = 1
        event_service = EventService()
        event = event_service.get_event_by_id(id)
        self.assertIsInstance(event, Event) # verifica se o retorno é uma lista de eventos
    
    def test_get_user_by_id(self):
        print("TEST GET USER BY ID")
        user_id = 1
        user_service = UserService()
        user = user_service.get_user_by_id(user_id)
        self.assertEqual(user, None) # verifica se o retorno é uma lista de eventos

    def test_has_checked_in(self):
        event_id = 1
        user_id = 1234
        user_service = UserService()
        has_checked_in = user_service.has_checked_in(event_id,user_id)
        user_id = 54321
        has_checked_in2 = user_service.has_checked_in(event_id,user_id)
        self.assertIsInstance(has_checked_in, bool) 
        self.assertIsInstance(has_checked_in2, bool) 
        self.assertEqual(has_checked_in,True)
        self.assertEqual(has_checked_in2,False)

    def test_check_in(self):
        pass
if __name__ == '__main__':
    unittest.main()
