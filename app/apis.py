import requests
import httplib2
import apiclient

from oauth2client.service_account import ServiceAccountCredentials

import cfg


def get_google_sheet_data():
    """
    Получает данные с google-таблицы
    :return: вложенный лист с [номер заказа, цена в $, дата прибытия]
    """
    CREDENTIALS_FILE = '../keys.json'
    spreadsheet_id = cfg.SPREADSHEET_ID
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A2:D51',
        majorDimension='ROWS'
    ).execute()
    return [[item[1], float(item[2]), item[3]] for item in values['values']]


def get_usd_course():
    """
    Получает курс доллара с API ЦБ РФ, записывает в переменную cfg
    :return: Курс, если API недоступно то ConnectionError
    """
    try:
        data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        cfg.USD_COURSE=data['Valute']['USD']['Value']
        return cfg.USD_COURSE
    except Exception as e:
        return cfg.USD_COURSE
