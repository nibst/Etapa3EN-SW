from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.User import User
class UserDao:
    """
    user data acess object
    """
    #TODO error handling of connection
    def __init__(self) -> None:
        db_connection_instance:DBConnectionSingleton = DBConnectionSingleton.get_instance()
        self.__conn = db_connection_instance.get_connection()
        self.__cur = db_connection_instance.get_cursor()
    
    def insert_user(self,user:User):
        inser_script = "INSERT INTO Users (user_id,user_name,email,passw) VALUES (%s, %s, %s,%s)"

        insert_value = (user.get_id(), user.get_name(),user.get_email(),user.get_password())
        self.__cur.execute(inser_script, insert_value)
        self.__conn.commit()

        return user.get_id()
    def get_user_by_email(self,email):

        query_script = "SELECT * FROM Users WHERE email = %s"
        self.__cur.execute(query_script, (email,))
        user = self.__cur.fetchone()
        self.__conn.commit()
        return user
    def get_user_by_id(self,id):

        query_script = "SELECT * FROM Users WHERE user_id = %s"
        self.__cur.execute(query_script, (id,))
        user = self.__cur.fetchone()
        self.__conn.commit()
        return user

    def print_all_users(self):
        query_scrpit = "SELECT * FROM Users;"
        self.__cur.execute(query_scrpit)
        for record in self.__cur.fetchall():
            print(record)
        self.__conn.commit()

    def delete_by_email(self,email):
        delete_script = "DELETE FROM Users WHERE email = %s"
        self.__cur.execute(delete_script, (email,))
        self.__conn.commit()
        #Return something?
        

        
    