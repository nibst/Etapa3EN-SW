import unittest
from src.data.dao.AddressDao import AddressDao
from src.data.dao.DBConnection import DBConnectionSingleton



class TestAddress(unittest.TestCase):
    def test_query_by_street(self):

        #order of tuple = (address_id, street, house_number, city, event_state, zip_code, ,complement)
        address_dao = AddressDao()
        
        addresses = address_dao.get_adresses_by_street('Mario Leitao')
        regex = "Mario Leitao/*"
        for address_tuple in addresses:
            self.assertRegex(address_tuple[1],regex) #1 is street
            print(address_tuple[1])
        addresses = address_dao.get_adresses_by_street('sa')
        regex = "sa/*"
        for address_tuple in addresses:
            self.assertRegex(address_tuple[1],regex) #1 is street
            print(address_tuple[1])
        DBConnectionSingleton.destroyer()

    def test_query_by_state(self):
        #order of tuple = (address_id, street, house_number, city, event_state, zip_code, ,complement)
        address_dao = AddressDao()
        
        addresses = address_dao.get_adresses_by_state('Rio Grande do Sul')
        regex = "Rio Grande do Sul/*"
        for address_tuple in addresses:
            self.assertRegex(address_tuple[4],regex) #4 is state
            print(address_tuple[4])
        addresses = address_dao.get_adresses_by_state('rs')
        regex = "rs/*"
        for address_tuple in addresses:
            self.assertRegex(address_tuple[4],regex) #4 is state
        DBConnectionSingleton.destroyer()

    def test_query_by_city(self):
        #order of tuple = (address_id, street, house_number, city, event_state, zip_code, ,complement)
        address_dao = AddressDao()
        
        addresses = address_dao.get_adresses_by_city('Porto Alegre')
        regex = "Porto Alegre/*"
        for address_tuple in addresses:
            self.assertRegex(address_tuple[3],regex) #3 is city
            print(address_tuple[3])
        addresses = address_dao.get_adresses_by_city('POA')
        regex = "POA/*"
        for address_tuple in addresses:
            self.assertRegex(address_tuple[3],regex) #3 is city
            print(address_tuple[3])
        DBConnectionSingleton.destroyer()

    def test_query_by_zip(self):
        #order of tuple = (address_id, street, house_number, city, event_state, zip_code,complement)
        address_dao = AddressDao()
        
        addresses = address_dao.get_adresses_by_zip_code(90690425)
        for address_tuple in addresses:
            self.assertEqual(address_tuple[5],90690425) #5 is zip
            print(address_tuple[5])
        DBConnectionSingleton.destroyer()
if __name__ == '__main__':
    unittest.main()
