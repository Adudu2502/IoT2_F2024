import sqlite3
from datetime import datetime
import json
import paho.mqtt.subscribe as subscribe
print("Subscribe MQTT script running!")

def create_table():
    query = """CREATE TABLE IF NOT EXISTS stue (daytime TEXT NOT NULL, temperature REAL NOT NULL, humidity REAL NOT NULL);"""
    try:
        conn = sqlite3.connect("database/sensor_data.db")
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    except sqlite3.Error as sql_e:
        print(f"sqlite error occrued: {sql_e}")
    except Exception as e:
        print(f"Error occured: {e}")
    finally:
        conn.close()
    
create_table()       

def on_message_print(client, userdata, message):
    
    query = """INSERT INTO stue (datetime, temperature, humidity) VALUES(?, ?, ?)"""
    now = datetime.now()
    now = now.strftime("%d/%m/%y %H:%M:%S")
    
    dht11_data = json.loads(message.payload.decode())
    data = (now, dht11_data['temperature'], dht11_data['humidity'])

    try:
        conn = sqlite3.connect("database/sensor_data.db")
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    except sqlite3.Error as sql_e:
        print(f"sqlite error occrued: {sql_e}")
    except Exception as e:
        print(f"Error occured: {e}")
    finally:
        conn.close()
    

subscribe.callback(on_message_print, "paho/test/topic", hostname="20.234.68.196", userdata={"message_count": 0})