import unittest
from src.data.User import User
from src.data.dao.UserDao import UserDao
from src.data.dao.DBConnection import DBConnectionSingleton
from src.application.UserService import UserService



class TestUserDAO(unittest.TestCase):
    def test_query_by_email(self):

        db_connection  = DBConnectionSingleton.get_instance()
        #order of tuple = (address_id, street, house_number, city, event_state, zip_code,apartment,complement)
        user_dao = UserDao(db_connection)

        user = user_dao.get_user_by_email('emaildetesteparaevento@teste.eu')
        user = user[0]
        self.assertEqual(user[1],'nikolas')
        self.assertEqual(len(user),4)

        DBConnectionSingleton.destroyer()
if __name__ == '__main__':
    unittest.main()