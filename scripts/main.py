import os
import json

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

import quantity as quantity
import cloud_functions as cf

credentials_path = "../secrets/simcoscripts-f5d853cce669.json"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']


def get_automations(filepath):
    files = os.listdir(filepath)
    json_files = []

    for file in files:
        if file[-5:] == ".json":
            json_files.append(filepath + file)

    return json_files


def get_automation_data(filepath):
    with open(filepath) as file:
        data = json.load(file)
    if data[0] in ["automation!+", "!default"]:
        return data[1], data[0]
    return None


def sync_resources(attributes, root_path):
    resources = quantity.get_current_stock(root_path + attributes['path'])

    creds = None
    if os.path.exists(credentials_path):
        creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
        print("got credentials!")
    else:
        return 1

    body = {"values": resources}
    range_name = "warehouse!" + attributes["column_start"] + str(attributes["row_start"]) + ":" + attributes[
        "column_start"] + str(attributes["row_start"] + 200)
    # range_name = "warehouse!B1:B200"
    print(range_name)

    cf.batch_update_values(attributes["sheet_id"], range_name, resources)

    # service = build('sheets', 'v4', credentials=creds)
    # result = service.spreadsheets().values().update(
    #     spreadsheetId=attributes["sheet_id"], range=range_name,
    #     valueInputOption="USER_ENTERED", body=body).execute()
    # print(f"{result.get('updatedCells')} cells updated.")


def main():
    automations = get_automations("../automations/")

    for automation in automations:
        values, automation_type = get_automation_data(automation)
        print(values)
        if not values:
            continue
        if automation_type == "automation!+":
            if values["type"] == "resource sync":
                sync_resources(values, "../automations/")

        elif automation_type == "!default":
            pass
    pass


if __name__ == "__main__":
    main()