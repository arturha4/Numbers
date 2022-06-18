from pprint import pprint

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials


# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'keys.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1Xtks4E1uXEFdrkpovrYc5VLBPvxuopl4KE_drQevavk'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

# Пример чтения файла
values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:D51',
    majorDimension='ROWS'
).execute()
for item in values['values']:
    print(item)

