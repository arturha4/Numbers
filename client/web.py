from flask import Flask
from db import get_orders_from_db
import pretty_html_table
import pandas
import datetime

app = Flask(__name__)


def orders_to_dataframe(data):
    return pandas.DataFrame.from_dict({
        "№": [i for i in range(1, len(data) + 1)],
        "Номер поставки": [item[1] for item in data],
        "Цена в $": [str(item[2]) for item in data],
        "Цена в ₽": [str(item[4]) for item in data],
        "Дата поставки": [datetime.datetime.strftime(item[3], "%d.%m.%y") for item in data],
    })


@app.route('/home', methods=['GET'])
def home():
    df = orders_to_dataframe(get_orders_from_db())
    return pretty_html_table.build_table(df, 'grey_dark', text_align='center', font_family="cursive")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
