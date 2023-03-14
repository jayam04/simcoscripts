import os
import json

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from cloud_functions import batch_update_values

import quantity as quantity
import cloud_functions as cf
from dev_tools import dev_print, start_dev_mode
import sys

credentials_path = "../secrets/simcoscripts-dfb9b2048a6e.json"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']
automation_path = "../automations/"
data_folder = "../data/"


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
        if data:
            return data
    return None


def sync_resources(file_data, sheet_data):
    resources = quantity.get_current_stock(automation_path + file_data["path"])

    creds = None
    if os.path.exists(credentials_path):
        creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
        print("got credentials!")
    else:
        return 1

    body = {"values": resources}
    range_name = "warehouse!" + sheet_data["column_start"] + str(sheet_data["row_start"]) + ":" + sheet_data[
        "column_start"] + str(sheet_data["row_start"] + 200)
    # range_name = "warehouse!B1:B200"
    print(range_name)

    cf.batch_update_values(sheet_data["id"], range_name, resources)

    # service = build('sheets', 'v4', credentials=creds)
    # result = service.spreadsheets().values().update(
    #     spreadsheetId=attributes["sheet_id"], range=range_name,
    #     valueInputOption="USER_ENTERED", body=body).execute()
    # print(f"{result.get('updatedCells')} cells updated.")


def get_credentials():
    return Credentials.from_service_account_file(credentials_path)


def get_sheet_upload_data(upload_values, sheet_attributes):
    # takes all automation data
    # return sheet_update data block
    cs = sheet_attributes["column_start"]
    rs_int = sheet_attributes["row_start"]
    sheet_range = cs + str(rs_int) + ":" + chr(ord(cs) + len(upload_values[0]) - 1) + str(rs_int + len(upload_values) - 1)

    return {
        'range': sheet_range,  # sheet range ie. A1:B3
        'values': upload_values  # 2D sheet data array
    }


def get_from_json(filepath):
    with open(filepath) as file:
        data = json.load(file)
    return data


def get_sync_data(automation_data):
    # takes automation data and
    # return 2D array of data to sync

    match automation_data["type"]:
        case "warehouse sync":
            return [[]]
            pass
        case "resource name":
            return get_from_json(data_folder + "defaults/resource_name.json")
    return [[]]


def main():
    # credentials
    creds = get_credentials()
    dev_print("got credentials!", "checkpoint")

    # automations
    automation_files = get_automations("../automations/")
    dev_print("got automation files!", "checkpoint")

    for automation_file in automation_files:

        #  get basic data
        automation_data = get_automation_data(automation_file)
        sheet_upload_data = []

        sub_automations = [sub for sub in automation_data["sub_automations"]]
        for sub_automation in sub_automations:
            sync_data = get_sync_data(sub_automation)
            sheet_upload_data.append(get_sheet_upload_data(sync_data, sub_automation["sheet"]))

        batch_update_values(creds, automation_data["sheet_id"], sheet_upload_data)

        # print(automation_data)
        # if automation_data["type"] == "resource sync":
        #     sync_resources(automation_data["file"], automation_data["sheet"])
        # if automation_data["type"] == "resource name":
        #     sync_resources(automation_data["file"], automation_data["sheet"])


if __name__ == "__main__":
    if "--dev" in sys.argv or "-d" in sys.argv:
        start_dev_mode()

    main()
