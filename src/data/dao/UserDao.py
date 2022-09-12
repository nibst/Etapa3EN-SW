from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.User import User
class UserDao:
    """
    user data acess object
    """
    #TODO error handling of connection
    def __init__(self,connection:DBConnectionSingleton) -> None:
        self.__conn = connection.get_connection()
        self.__cur = connection.get_cursor()
    
    def insert_user(self,user:User):
        inser_script = "INSERT INTO Users (user_id,user_name,email,passw) VALUES (%s, %s, %s,%s)"

        insert_value = (user.get_id(), user.get_name(),user.get_email(),user.get_password())
        self.__cur.execute(inser_script, insert_value)
        self.__conn.commit()

        return user.get_id()
        
    