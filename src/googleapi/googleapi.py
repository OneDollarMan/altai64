from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime


class Api:
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # The ID and range of a sample spreadsheet.
    spreadsheet_id = '1ZQ1MYJ220BZ0j6KV567vdwzfRIBB0xMEDA0dLybWXJc'
    range_name = 'Лист1'
    value_input_option = 'RAW'
    service = None

    def __init__(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('../webserver/token.pickle'):
            with open('../webserver/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    '../webserver/credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=8080)
            # Save the credentials for the next run
            with open('../webserver/token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def write(self, name, phone):
        values = [
            [
                name, phone, str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
            ]
        ]
        body = {
            'values': values
        }
        result = self.service.spreadsheets().values().append(
            spreadsheetId=self.spreadsheet_id, range=self.range_name,
            valueInputOption=self.value_input_option, body=body).execute()
        print('{0} cells appended.'.format(result.get('updates').get('updatedCells')))
