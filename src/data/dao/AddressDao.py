from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.Address import Address

class AddressDao:
    """
    address data acess object
    """
    #TODO error handling of connection, sql injection
    def __init__(self) -> None:
        db_connection_instance:DBConnectionSingleton = DBConnectionSingleton.get_instance()
        self.__conn = db_connection_instance.get_connection()
        self.__cur = db_connection_instance.get_cursor()
    
    def insert_address(self,event:Address):
        insert_script = "INSERT INTO Address (address_id, street, house_number, city, event_state, zip_code,complement) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        insert_value = (event.get_id(), event.get_street(), event.get_house_number(), event.get_city(), event.get_state(), event.get_zip_code(), event.get_complement())
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
        select_query = "SELECT * FROM Address WHERE address_id = %s"
        self.__cur.execute(select_query,(address_id,))
        record = self.__cur.fetchone()
        if record is None:
            return None
        else:
            return record

    def get_adresses_by_street(self,street):

        query_scrpit = "SELECT * FROM Address WHERE street LIKE %s"
        street = '%' + street + '%' #just get by prefix
        input = (street,)
        self.__cur.execute(query_scrpit,input)
        address_lst = []
        for record in self.__cur.fetchall():
            address_lst.append(record)
        self.__conn.commit()
        return address_lst


    def get_adresses_by_city(self,city):
        query_scrpit = "SELECT * FROM Address WHERE city LIKE %s"
        city = city + '%'  #just get by prefix
        input = (city,)
        self.__cur.execute(query_scrpit,input)
        address_lst = []
        for record in self.__cur.fetchall():
            address_lst.append(record)
        self.__conn.commit()
        return address_lst

    def get_adresses_by_state(self,state):
        query_scrpit = "SELECT * FROM Address WHERE event_state LIKE %s"
        state = state + '%' #just get by prefix
        input = (state,)
        self.__cur.execute(query_scrpit,input)
        address_lst = []
        for record in self.__cur.fetchall():
            address_lst.append(record)
        self.__conn.commit()
        return address_lst
    
    def get_adresses_by_zip_code(self,zip_code):
        query_scrpit = "SELECT * FROM Address WHERE zip_code = %s"
        self.__cur.execute(query_scrpit,(zip_code,))
        address_lst = []
        for record in self.__cur.fetchall():
            address_lst.append(record)
        self.__conn.commit()
        return address_lst





