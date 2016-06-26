#       Opens single stock file and prints name
# amd = open('amd.txt', 'r')
# symbol = str(amd.read()).split("|")
# amd.close()
#
# name = symbol[0]
#
# print(name)
from datetime import datetime

from json_handler import read_json
from Symbol_Class import Symbol


def update_all(symbols_list):
    """Updates all files in list"""

    symbols_list = symbols_list

    for symbol in symbols_list:
        file_name = (str(symbol) + '.txt')
        symbol = Symbol(str(symbol))

        file = open(file_name, 'w')
        #   Create Attributes
        symbol_name = symbol.get_name()
        symbol_cp = symbol.get_current_price()
        symbol_lc = symbol.get_last_close()
        symbol_div = symbol.get_dividend()
        symbol_yield = symbol.get_div_yield()
        symbol_low = symbol.get_year_low()
        symbol_high = symbol.get_year_high()
        symbol_rating = symbol.get_rating()

        updated = str(datetime.today().now())

        file.write(str(symbol_name + '\n'))
        file.write(str(symbol_cp + '\n'))
        file.write(str(symbol_lc + '\n'))
        file.write(str(symbol_div + '\n'))
        file.write(str(symbol_yield + '\n'))
        file.write(str(symbol_low + '\n'))
        file.write(str(symbol_high + '\n'))
        file.write(str(symbol_rating + '\n'))

        file.write(updated)

        file.close()


def write_new_file(symbol):
    """Writes new file for new symbol"""
    file_name = (str(symbol) + '.txt')
    symbol = Symbol(str(symbol))

    file = open(file_name, 'w')
    #   Create Attributes
    symbol_name = symbol.get_name()
    symbol_cp = symbol.get_current_price()
    symbol_lc = symbol.get_last_close()
    symbol_div = symbol.get_dividend()
    symbol_yield = symbol.get_div_yield()
    symbol_low = symbol.get_year_low()
    symbol_high = symbol.get_year_high()
    symbol_rating = symbol.get_rating()

    updated = str(datetime.today().now())

    file.write(str(symbol_name + '\n'))
    file.write(str(symbol_cp + '\n'))
    file.write(str(symbol_lc + '\n'))
    file.write(str(symbol_div + '\n'))
    file.write(str(symbol_yield + '\n'))
    file.write(str(symbol_low + '\n'))
    file.write(str(symbol_high + '\n'))
    file.write(str(symbol_rating + '\n'))

    file.write(updated)

    file.close()


# update_all(read_json())
