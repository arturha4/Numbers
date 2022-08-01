import time

from db import *


if __name__=="__main__":
    create_orders_table()
    while True:
        delete_all_orders_from_db()
        create_orders_from_sheet_data()
        time.sleep(20)
