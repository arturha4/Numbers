import time

from app.db import create_orders_from_sheet_data, delete_all_orders_from_db

if __name__ == "__main__":
    while True:
        delete_all_orders_from_db()
        create_orders_from_sheet_data()
        time.sleep(20)
