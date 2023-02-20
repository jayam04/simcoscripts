import json


root_path = "../data/"

def get_current_stock():
    print('fetching current stocks ...')
    current_stock = {}
    with open(root_path + "resource.json") as file:
        stock = json.load(file)

    for product in stock:
        db_letter = product['kind']['db_letter']
        if db_letter in current_stock.keys():
            current_stock[db_letter] += product['amount']
        else:
            current_stock[db_letter] = product['amount']

    print('current stock ...')
    print(current_stock)
    print('completed fetching stock :)')

    return current_stock


get_current_stock()