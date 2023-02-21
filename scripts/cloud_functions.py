from __future__ import print_function

import os

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.service_account import Credentials


credentials_path = "../secrets/simcoscripts-626ed5ba69d0.json"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']


def sync_sheet(sheet_id, worksheet_range, data):
    creds = None
    if os.path.exists(credentials_path):
        creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
        print("got credentials!")
    else:
        return 1




def batch_update_values(spreadsheet_id, range_name,
                        _values, value_input_option="USER_ENTERED"):
    """
        Creates the batch_update the user has access to.
        Load pre-authorized user credentials from the environment.
        TODO(developer) - See https://developers.google.com/identity
        for guides on implementing OAuth2 for the application.
            """
    creds = None
    if os.path.exists(credentials_path):
        creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
        print("got credentials!")
    else:
        return 1
    # pylint: disable=maybe-no-member
    try:
        service = build('sheets', 'v4', credentials=creds)

        # values = [
        #     [
        #         0
        #     ],
        #     [
        #         2
        #     ],
        # ]
        data = [
            {
                'range': range_name,
                'values': _values
            },
            # Additional ranges to update ...
        ]
        body = {
            'valueInputOption': value_input_option,
            'data': data
        }
        result = service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id, body=body).execute()
        print(f"{(result.get('totalUpdatedCells'))} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


if __name__ == '__main__':
    # Pass: spreadsheet_id, range_name value_input_option and _values)
    batch_update_values("12vGQGLtSCsaMo-nj8N6sGRqzgAX81091tNdAXW7Uz5Y",
                        "A1:C2", "USER_ENTERED",
                        [
                            ['F', 'B'],
                            ['C', 'D']
                        ])