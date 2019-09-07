import pymysql
from loadconfig import Config

# load configuration
config = Config()


class Database:
    def __init__(self):
        db = config.get_db_config()
        self.con = pymysql.connect(host=db['host'], port=db['port'], user=db['user'],
                                   password=db['password'], db=db['db'],
                                   cursorclass=pymysql.cursors.DictCursor)

        self.cur = self.con.cursor()

    def list_employees(self):
        self.cur.execute("SELECT firstname, lastname, gender FROM employee")
        result = self.cur.fetchall()

        return result

