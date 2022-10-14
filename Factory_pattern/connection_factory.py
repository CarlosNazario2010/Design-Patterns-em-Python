import MySQLdb

class ConnectionFactory(object):

    def get_connection(self):
        return MySQLdb.connect(
            host="localhost",
            user='root',
            password='',
            db='alura')
