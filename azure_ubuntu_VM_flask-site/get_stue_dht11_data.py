import sqlite3
from datetime import datetime
from random import randint
from time import sleep

def get_stue_data(number_of_rows):
        query = """SELECT * FROM stue ORDER BY datetime DESC;"""
        datetimes = []
        temperatures = []
        humidities = []
        try:
            conn = sqlite3.connect("database/sensor_data.db")
            cur = conn.cursor()
            cur.execute(query)
            rows = cur.fetchmany(number_of_rows)
            for row in reversed (rows):
                datetime.append(row[0])
                temperatures.append(row[1])
                humidities.append(row[2])
            return datetimes, temperatures, humidities     
        except sqlite3.Error as sql_e:
            print(f"sqlite error occrued: {sql_e}")
            conn.rollback()
        except Exception as e:
            print(f"Error occured: {e}")
        finally:
            conn.close()
get_stue_data(10)