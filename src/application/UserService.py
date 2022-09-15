from src.data.dao.UserDao import UserDao
from src.data.dao.DBConnection import DBConnectionSingleton
from src.data.User import User
import re

class UserService:
    
    def __init__(self) -> None:
        pass 
    
    def create_user(self,user:User):
        #regex for email
        #shorter version of the RFC 5322-compliant Regular Expression 
        regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
        if  re.match(regex,user.get_email()) is None:
            raise Exception("Email not valid")
        db_connection  = DBConnectionSingleton.get_instance()
        user_dao = UserDao(db_connection)
        try:
            user_dao.insert_user(user)
        except Exception as e:
            #probably user already exist
            raise(e)

        return user
    
    def login(self,email,password):
        db_connection  = DBConnectionSingleton.get_instance()
        user_dao = UserDao(db_connection)
        user = user_dao.get_user_by_email(email)
        #TODO maybe raise one unique exception for email and password (more security)
        #TODO transform user in User object before doing logic to it
        if user is None:
            raise Exception("Invalid Email")
        if user[2] != password: #user[2] its the password on db
            raise Exception("Invalid Password")
        return user
    
