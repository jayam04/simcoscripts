from __future__ import print_function

import os

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.service_account import Credentials


credentials_path = "../secrets/simcoscripts-f5d853cce669.json"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']


def sync_sheet(sheet_data, data, creds):
    if not creds:
        raise ValueError("got empty credentials!!")

    batch_update_values(sheet_data)


def batch_update_values(sheet_data, range_name,
                        _values, value_input_option="USER_ENTERED"):
    """
        Creates the batch_update the user has access to.
        Load pre-authorized user credentials from the environment.
        TODO(developer) - See https://developers.google.com/identity
        for guides on implementing OAuth2 for the application.
            """

    spreadsheet_id = sheet_data["id"],

    creds = None
    if os.path.exists(credentials_path):
        creds = Credentials.from_service_account_file(
            credentials_path, scopes=SCOPES)
        print("got credentials!")
    else:
        return 1
    # pylint: disable=maybe-no-member
    try:
        service = build('sheets', 'v4', credentials=creds)

        data = [
            {
                'range': range_name,
                'values': _values
            },
        ]
        body = {
            'valueInputOption': value_input_option,
            'data': data
        }
        result = service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id, body=body).execute()
        print(f"{(result.get('totalUpdatedCells'))} cells updated.")
        print("dome")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


if __name__ == '__main__':
    pass
    # Pass: spreadsheet_id, range_name value_input_option and _values)
    # batch_update_values("12vGQGLtSCsaMo-nj8N6sGRqzgAX81091tNdAXW7Uz5Y",
    #                     "A1:C2", "USER_ENTERED",
    #                     [
    #                         ['F', 'B'],
    #                         ['C', 'D']
    #                     ])
