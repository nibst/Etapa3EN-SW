from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.Address import Address

class AddressDao:
    """
    address data acess object
    """
    #TODO error handling of connection
    def __init__(self,connection:DBConnectionSingleton) -> None:
        self.__conn = connection.get_connection()
        self.__cur = connection.get_cursor()
    
    def insert_address(self,event:Address):
        insert_script = "INSERT INTO Address (address_id, street, house_number, city, event_state, zip_code,apartment,complement) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        insert_value = (event.get_id(), event.get_street(), event.get_house_number(), event.get_city(), event.get_state(), event.get_zip_code(), event.get_apartment(), event.get_complement())
        self.__cur.execute(insert_script, insert_value)
        self.__conn.commit()
        return event.get_id()
        
    def print_all_addresses(self):
        select_query = "SELECT * FROM Address"
        self.__cur.execute(select_query)
        for record in self.__cur.fetchall():
            print(record)
        self.__conn.commit()

    def get_address_by_id(self,address_id):
        select_query = "SELECT address_id FROM Address WHERE address_id = %s"
        self.__cur.execute(select_query,(address_id,))
        record = self.__cur.fetchone()
        if record is None:
            return None
        else:
            return record[0] # just the id of the address



