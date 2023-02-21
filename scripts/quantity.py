import json



def get_current_stock(filepath):
    print('fetching current stocks ...')
    current_stock = [[0] for i in range(200)]
    with open(filepath) as file:
        stock = json.load(file)

    for product in stock:
        db_letter = product['kind']['db_letter']
        current_stock[db_letter][0] += product['amount']

    print('current stock ...')
    print(current_stock)
    print('completed fetching stock :)')

    return current_stock
