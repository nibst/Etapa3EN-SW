from src.data.dao.UserDao import UserDao
from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.User import User
import re

class UserService:
    
    def __init__(self) -> None:
        pass 
    #TODO maybe pass an User as parameter, dontknow. And maybe encrypt password
    def create_user(self,name,email,password):
        #regex for email
        #shorter version of the RFC 5322-compliant Regular Expression 
        regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
        if  re.match(regex,email) is None:
            raise Exception("Email not valid")
        
        db_connection  = DBConnectionSingleton.get_instance()
        user_dao = UserDao(db_connection)
        try:
            user_dao.insert_user(User(name,email,password))
        except Exception as e:
            #probably user already exist
            raise(e)
        finally:
            DBConnectionSingleton.destroyer()

        return User(name,email,password)
    
    def login(self,name,email,password):

        pass
    
