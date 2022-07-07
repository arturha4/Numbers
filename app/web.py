from flask import Flask
from db import get_orders_from_db, orders_to_dataframe
import pretty_html_table

app = Flask(__name__)


@app.route('/home', methods=['GET'])
def home():
    df = orders_to_dataframe(get_orders_from_db())
    return pretty_html_table.build_table(df, 'grey_dark', text_align='center', font_family="cursive")


if __name__ == "__main__":
    app.run(debug=True)
