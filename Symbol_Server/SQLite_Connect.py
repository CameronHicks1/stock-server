import sqlite3

from Symbol_Class import Symbol


def create_symbol(symbol):
    conn = sqlite3.connect('pyramid.db')

    symbol = Symbol(symbol)
    symbol_name = symbol.get_name()
    symbol_cp = symbol.get_current_price()
    symbol_lc = symbol.get_last_close()
    symbol_div = symbol.get_dividend()
    symbol_yield = symbol.get_div_yield()
    symbol_low = symbol.get_year_low()
    symbol_high = symbol.get_year_high()
    symbol_rating = symbol.get_rating()

    c = conn.cursor()
    c.execute('INSERT INTO Stocks VALUES(' + '"' + symbol_name + '"' + ', ' + '"' + symbol_cp + '", ' +
              '"' + symbol_lc + '", ' + '"' + symbol_div + '", ' + '"' + symbol_yield + '", ' + '"' +
              symbol_low + '", ' + '"' + symbol_high + '", ' + '"' + symbol_rating + '"' + ');')

    conn.commit()
    conn.close()

create_symbol('AMD')