import unittest
from src.application.create_event import  EventService
from src.data.Event import Event
from src.data.Address import Address
from src.data.User import User
from datetime import date, time


class TestEvent(unittest.TestCase):
    #exemplo só
    def test_create_event(self):
        
        user = User('nibs','nikolasps7@gmail.com','senha123')
        user.set_id(166)
        event_service = EventService()
        Post = {'name': 'nibs event', 'start_date': '2022-09-17', 'end_date': '2022-09-22', 'check_in': '22:44', 'check_out': '00:44', 'visibility': 'public', 'street': 'Mario Leitao', 'house_number': '60', 'zip-code': '9069425', 'state': 'RS', 'city': 'Porto Alegre'}
        self.assertIsInstance(event_service.create_event(user,Post), Event) # verifica se o retorno é do tipo Event
    def test_get_events(self):
        user = User('nibs','nikolasps7@gmail.com','senha123')
        user.set_id(166)
        event_service = EventService()
        events = event_service.get_events()
        
        self.assertIsInstance(events, list) # verifica se o retorno é uma lista
        self.assertIsInstance(events[0], Event) # verifica se o retorno é uma lista de eventos
if __name__ == '__main__':
    unittest.main()
