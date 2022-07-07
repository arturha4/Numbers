import datetime
import pandas
import psycopg2

from app.apis import get_usd_course, get_google_sheet_data
from cfg import *


def get_connection():
    connection = psycopg2.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME
    )
    connection.autocommit = True
    return connection


def try_connection(func):
    def wrapper(*args):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                if args:
                    func(cursor, *args)
                else:
                    func(cursor)
        except Exception as ex:
            print("Error", ex)
        finally:
            if connection:
                connection.close()
                print("Connection closed")
    return wrapper


@try_connection
def create_orders_table(cursor):
    cursor.execute(
        """CREATE TABLE orders(
                id serial PRIMARY KEY,
                order_number integer NOT NULL,
                usd_price numeric (12,2) NOT NULL,
                supply_date date NOT NULL,
                rub_price numeric(12,2) NOT NULL);"""
    )


@try_connection
def create_order(cursor, *args):
    cursor.execute(
        """INSERT INTO orders
        VALUES (DEFAULT,%s,%s,%s,%s);""", args
    )


@try_connection
def delete_all_orders_from_db(cursor):
    cursor.execute(
        """TRUNCATE orders;
        """
    )


def get_orders_from_db():
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM public.orders""")
            return cursor.fetchall()
    except Exception as ex:
        print("Error", ex)
    finally:
        if connection:
            connection.close()
            print("Connection closed")


def create_orders_from_sheet_data():
    usd_course = get_usd_course()
    for item in get_google_sheet_data():
        create_order(item[0], item[1], item[2], item[1] * usd_course)


def orders_to_dataframe(data):
    return pandas.DataFrame.from_dict({
        "№": [i for i in range(1, len(data) + 1)],
        "Номер поставки": [item[1] for item in data],
        "Цена в $": [str(item[2]) for item in data],
        "Цена в ₽": [str(item[4]) for item in data],
        "Дата поставки": [datetime.datetime.strftime(item[3], "%d.%m.%y") for item in data],
    })
