import os
from sqlite3 import *

package_dir = os.path.dirname(os.path.abspath(__file__))
db_Data_dir = os.path.join(package_dir, '../Data/DB/dataNCU.db')


class SQLiteDB:
    def tableExist(self, nameTable, conf=True):
        result = False
        db_dir = db_Data_dir
        if conf:
            db_dir = db_Global_dir
        conn = connect(db_dir)
        curs = conn.cursor()
        # get the count of tables with the name
        curs.execute(
            "SELECT COUNT(name) FROM sqlite_master WHERE type='table' AND name='{TBLs}'".format(TBLs=nameTable))
        # if the count is 1, then table exists
        if curs.fetchone()[0] == 1:
            result = True
        # commit the changes to db
        conn.commit()
        # close the connection
        conn.close()
        return result

    def executeSQL(self, query, conf=True):
        try:
            db_dir = db_Data_dir
            if conf:
                db_dir = db_Global_dir
            conn = connect(db_dir)
            curs = conn.cursor()
            curs.execute(query)
            conn.commit()
            conn.close()
            return "Execute successfully!"
        except Exception as e:
            print(e)
            return None

    def listObject(self, query, conf=True):
        try:
            db_dir = db_Data_dir
            if conf:
                db_dir = db_Global_dir
            conn = connect(db_dir)
            curs = conn.cursor()
            result = curs.execute(query).fetchall()
            conn.commit()
            conn.close()
            return result
        except Exception as e:
            print(e)
            return None

    def getObject(self, query, conf=True):
        try:
            db_dir = db_Data_dir
            if conf:
                db_dir = db_Global_dir
            conn = connect(db_dir)
            curs = conn.cursor()
            result = curs.execute(query).fetchone()[0]
            conn.commit()
            conn.close()
            return result
        except Exception as e:
            print(e)
            return None

    def countObject(self, query, conf=True):
        try:
            db_dir = db_Data_dir
            if conf:
                db_dir = db_Global_dir
            conn = connect(db_dir)
            curs = conn.cursor()
            result = curs.execute(query).fetchone()[0]
            conn.commit()
            conn.close()
            return int(result)
        except Exception as e:
            print(e)
            return None
