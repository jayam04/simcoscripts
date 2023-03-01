import json


total_items = 140

def get_current_stock(filepath):
    # takes filepath relative to main file
    # returns 1 * n 2D array with nth place holding product
    # of db_letter n

    print('fetching current stocks ...')
    current_stock = [[0] for i in range(total_items)]
    with open(filepath) as file:
        stock = json.load(file)

    for product in stock:
        db_letter = product['kind']['db_letter']
        current_stock[db_letter][0] += product['amount']

    print('current stock ...')
    print(current_stock)
    print('completed fetching stock :)')

    return current_stock
