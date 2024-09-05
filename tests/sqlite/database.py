import sqlite3

class myTestDatabase:
    def __init__(self, db_location):
        self._db_loc = db_location
        self._sysTableName = "systeminfo"

    def create(self):
        # Connect to database
        conn = sqlite3.connect(self._db_loc)
        # Create a cursor
        c = conn.cursor()
 
        create_table_query = f"""CREATE TABLE {self._sysTableName} (
                    serial_number text,
                    hardware_version text,
                    firmware_version text,
                    partnumber text,
                    manufacture_date text,
                    tech_initial text);"""
        # Create a table
        try:
            c.execute(create_table_query)
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            # Commit
            conn.commit()
            # close connection
            conn.close()

    # Query the DB and Return all records
    def show_all(self):
        # Connect to database
        #conn = sqlite3.connect(':memory:')
        conn = sqlite3.connect(self._db_loc)

        # Create a cursor
        c = conn.cursor()
        
        show_all_query = f"""
        SELECT rowid, * FROM {self._sysTableName}
        """
        c.execute(show_all_query)
        items = c.fetchall()
        #print(items)
        for item in items:
            print(item)

        print("!execute!")

        # close our connection
        conn.close()

    def add_one(self, sn, hw, fw, pn, mdate, tech):
        # Connect to database
        #conn = sqlite3.connect(':memory:')
        conn = sqlite3.connect(self._db_loc)

        # Create a cursor
        c = conn.cursor()
        insert_record_query = f"""
        INSERT INTO {self._sysTableName} VALUES('{sn}','{hw}','{fw}','{pn}', '{mdate}', '{tech}')
        """
        c.execute(insert_record_query)
        
        conn.commit()

        # close our connection
        conn.close()

    def delete_one(self, id):
        # Connect to database
        #conn = sqlite3.connect(':memory:')
        conn = sqlite3.connect(self._db_loc)

        # Create a cursor
        c = conn.cursor()
        delete_record_query = f"""
        DELETE from {self._sysTableName} WHERE rowid = ({id})
        """
        c.execute(delete_record_query)
        
        conn.commit()

        # close our connection
        conn.close()

    def add_many(self, items):
        conn = sqlite3.connect(self._db_loc)

        # Create a cursor
        c = conn.cursor()
        insert_records_query = f"""
        INSERT INTO {self._sysTableName} VALUES(?,?,?)
        """
        c.executemany(insert_records_query, (items))
        
        conn.commit()

        # close our connection
        conn.close()

    def part_loopup(self, pn):
        #print(email)
        conn = sqlite3.connect(self._db_loc)

        # Create a cursor
        c = conn.cursor()
        pn_query = f"""
        SELECT rowid, * from {self._sysTableName} WHERE partnumber = (?)
        """
        c.execute(pn_query, (pn,))

        items = c.fetchall()
        for item in items:
            print(item)
        # close our connection
        conn.close()


