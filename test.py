import unittest
from src.application.create_event import  create_event
from src.data.Event import Event
from src.data.Address import Address
from src.data.User import User
from datetime import date, time


class TestEvent(unittest.TestCase):
    #exemplo só
    def test_create_event(self):
        user = User('nibs','nikolasps7@gmail.com','senha123')
        user.set_id(1660521522845)
        Post = {'name': ['nibs event'], 'date_start': ['2022-08-17'], 'date_end': ['2022-08-22'], 'time_start': ['22:44'], 'time_end': ['00:44'], 'visibility': ['public'], 'street': ['Mario Leitao'], 'house-number': ['60'], 'zip-code': ['90690425'], 'state': ['RS'], 'city': ['Porto Alegre']}
        self.assertIsInstance(create_event(user,Post), Event) # verifica se o retorno é do tipo Event
if __name__ == '__main__':
    unittest.main()
