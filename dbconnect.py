import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
hostname = os.getenv("hostname")
database = os.getenv("database")
username = os.getenv("username")
password = os.getenv("password")
port_id = os.getenv("port_id")
connect = os.getenv("connect")


def add_data(data):
    with psycopg2.connect(host=hostname,
                          dbname=database,
                          user=username,
                          password=password,
                          port=port_id) as connect:
        cursor = connect.cursor()

        create_script = ''' CREATE TABLE IF NOT EXISTS exchange_rates (
                                currency1   varchar(3) NOT NULL,
                                currency2   varchar(3) NOT NULL,
                                rate    FLOAT NOT NULL,
                                time    varchar(40) NOT NULL,
                                increase BOOLEAN NOT NULL)'''
        cursor.execute(create_script)

        insert_script = '''INSERT INTO exchange_rates 
                            (currency1, currency2, rate, time, increase) 
                            VALUES (%s, %s, %s, %s, %s)'''
        cursor.execute(insert_script, data)
    connect.close()


def read_data():
    with psycopg2.connect(host=hostname,
                          dbname=database,
                          user=username,
                          password=password,
                          port=port_id) as connect:
        cursor = connect.cursor()

        create_script = 'CREATE TABLE IF NOT EXISTS exchange_rates ()'
        cursor.execute(create_script)

        select = "SELECT * FROM exchange_rates"
        cursor.execute(select)

        dblist = cursor.fetchall()
    return dblist
