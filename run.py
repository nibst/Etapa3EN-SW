from src import app
from src.data.dao.DBConnection import DBConnectionSingleton


if __name__ == '__main__':
    app.run(debug=True)
    DBConnectionSingleton.get_instance() #in case there isnt an instance of DBconnection to destroy
    DBConnectionSingleton.destroyer()