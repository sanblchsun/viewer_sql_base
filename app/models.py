import pymysql

class MYSQLer:

    def __init__(self, host,
            port,
            user,
            password,
            database):

        self.con = pymysql.connect(host=host,
                              port=port,
                              user=user,
                              password=password,
                              database=database,
                              cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.con.cursor()



    def read_all(self):
        with self.con:
            self.cursor.execute("SELECT full_name, firma, e_mail, telefon, description,	date FROM requests")
            return self.cursor.fetchall()
