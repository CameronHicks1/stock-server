import urllib.request
import re


class Symbol:
    """Stock with methods to grab stats from Yahoo!Finance"""
    def __init__(self, symbol):

        self.symbol = symbol.replace(".", "-")

        self.name = ""
        self.year_high = ""
        self.year_low = ""
        self.rating = ""
        self.last_close = ""
        self.current_price = ""
        self.dividend = ""
        self.div_yield = ""
        self.no_shares = 0
        self.unit_cost = 0

        self.xhref = "http://finance.yahoo.com/q?s=" + str(self.symbol)

    def get_symbol(self):
        print(self.symbol)
        return self.symbol

    def get_name(self):
        """Grabs the stock name from Yahoo!Finance"""
#       Creating the Xpath
        self.xpath = '//*[@id="yfi_rt_quote_summary"]/div[1]/div/h2'
        self.path = re.compile(self.xpath)

#       Creating Socket
        self.sock = urllib.request.urlopen(self.xhref).read().decode("utf-8")

#       Filtering the scrape
        filtered = self.sock.split('<meta property="og:title" content="')
        pure_filter = filtered[1].split('"')

#       Setting name
        self.name = str(str(pure_filter[0]).replace("&amp;", "&"))

#       Return name
        # print(str(self.name))
        return self.name

    def get_year_high(self):
        """Grabs 52 week high from Yahoo!Finance"""
#       Creating the Xpath
        self.xpath = '//*[@id="table2"]/tbody/tr[2]/td/span[1]'
        self.path = re.compile(self.xpath)

#       Creating Socket
        self.sock = urllib.request.urlopen(self.xhref).read().decode("utf-8")

#       Filtering the scrape
        filtered = self.sock.split('52wk Range:</th><td class="yfnc')
        pure_filter = filtered[1].split('</span>')
        extra_filter = pure_filter[1].split('<span>')

#       Setting year_high
        self.year_high = extra_filter[1]

#       Return year_low
        # print('52 Week High: ' + str(self.year_high))
        return self.year_high

    def get_year_low(self):
        """Grabs 52 week low from Yahoo!Finance"""
#       Creating the Xpath
        self.xpath = '//*[@id="table2"]/tbody/tr[2]/td/span[1]'
        self.path = re.compile(self.xpath)

#       Creating Socket
        self.sock = urllib.request.urlopen(self.xhref).read().decode("utf-8")

#       Filtering the scrape
        filtered = self.sock.split('52wk Range:</th><td class="yfnc')
        pure_filter = filtered[1].split('</span>')
        extra_filter = pure_filter[0].split('<span>')

#       Setting year_low
        self.year_low = extra_filter[1]

#       Return year_low
        # print('52 Week Low: ' + str(self.year_low))
        return self.year_low

    def get_rating(self):
        """Grabs analyst average rating from Yahoo!Finance"""
#       Creating the Xpath
        self.xpath = '//*[@id="yfi_analysts"]/div[2]/table/tbody/tr[3]/td'
        self.path = re.compile(self.xpath)

#       Creating Socket
        self.sock = urllib.request.urlopen(self.xhref).read().decode("utf-8")

#       Filtering the scrape
        filtered = self.sock.split('Mean Recommendation')
        pure_filter = filtered[1].split('</td>')
        extra_filter = pure_filter[0].split('tabledata1">')

#       Setting rating
        self.rating = str(extra_filter[1])

#       Return rating
        # print('Mean Recommendation: ' + str(self.rating))
        return self.rating

    def get_last_close(self):
        """Grabs the last close from Yahoo!Finance"""
#       Creating the Xpath
        self.xpath = '//*[@id="yfs_l84_' + str(self.symbol) + '"]'
        self.path  = re.compile(self.xpath)

#       Creating Socket
        self.sock = urllib.request.urlopen(self.xhref).read().decode("utf-8")

#       Filtering the scrape
        filtered = self.sock.split('<td class="yfnc_tabledata1">')
        pure_filter = filtered[1].split('</td>')

#       Setting last_close
        self.last_close = pure_filter[0]

#       Return last_close
        # print('Last Close: ' + str(self.last_close))
        return self.last_close

    def get_current_price(self):
        """Grabs the current price"""
#       Creating the Xpath
        regex_safe = str(self.symbol.replace("-", "\-"))
        self.xpath = str('//*[@id="yfs_l84_' + regex_safe + '"]')
        self.path = re.compile(self.xpath)

#       Creating Socket
        self.sock = urllib.request.urlopen(self.xhref).read().decode("utf-8")

#       Filtering the scrape
        filtered = self.sock.split('time_rtq_ticker"><span id="yfs_l84_')
        pure_filter = filtered[1].split(str(self.symbol))
        extra_filter = pure_filter[0].split('</')
        double_filter = extra_filter[0].split('>')

#       Setting current_price
        self.current_price = double_filter[1]

#       Return current price
        # print('Current Price: ' + self.current_price)
        return self.current_price

#       print(double_filter[1])

    def get_dividend(self):
        """Grabs the last close from Yahoo!Finance"""
#       Creating the Xpath
        self.xpath = '//*[@id="table2"]/tbody/tr[8]/td"]'
        self.path  = re.compile(self.xpath)

#       Creating Socket
        self.sock = urllib.request.urlopen(self.xhref).read().decode("utf-8")

#       Filtering the scrape
        filtered = self.sock.split('Yield:</th><td class="yfnc_tabledata1">')
        pure_filter = filtered[1].split('</td>')
        extra_filter = pure_filter[0].split(' ')

#       Setting dividend
        self.dividend = extra_filter[0]

#       Return dividend
        # print('Dividend: ' + str(self.dividend))
        return self.dividend

    def get_div_yield(self):
        """Grabs the Yield from Yahoo!Finance"""
#       Creating the Xpath
        self.xpath = '//*[@id="table2"]/tbody/tr[8]/td"]'
        self.path  = re.compile(self.xpath)

#       Creating Socket
        self.sock = urllib.request.urlopen(self.xhref).read().decode("utf-8")

#       Filtering the scrape
        filtered = self.sock.split('Yield:</th><td class="yfnc_tabledata1">')
        pure_filter = filtered[1].split('</td>')
        extra_filter = pure_filter[0].split(' ')

#       Setting dividend
        self.dividend = extra_filter[1]

#       Return dividend
        # print('Yield: ' + str(self.dividend))
        return self.dividend

    def get_stats(self):
        """Returns all stats"""
        self.get_name()
        self.get_current_price()
        self.get_last_close()
        self.get_dividend()
        self.get_div_yield()
        self.get_year_low()
        self.get_year_high()
        self.get_rating()

    def get_table_data(self):
        """Returns Table data"""
        return [self.get_name(), self.get_current_price(), self.get_last_close(),
                self.get_dividend(), self.get_div_yield(), self.get_year_low(),
                self.get_year_high(), self.get_rating()]

    def stat_writer(self):
        """Writes symbol data to text file"""
#       Opening file
        f = open('stats_text.txt', 'a')

        f.write('##########################' + '\n')
        f.write(str(self.get_name()) + '\n')
        f.write('Current Price: ' + str(self.get_current_price()) + '\n')
        f.write('Last Close: ' + str(self.get_last_close()) + '\n')
        f.write('Dividend: ' + str(self.get_dividend()) + '\n')
        f.write('Yield: ' + str(self.get_div_yield()) + '\n')
        f.write('52 Week Low: ' + str(self.get_year_low()) + '\n')
        f.write('52 Week High: ' + str(self.get_year_high()) + '\n')
        f.write('Mean Recommendation: ' + str(self.get_rating()) + '\n')
        f.write('##########################' + '\n' + '\n')

#       Closing File
        f.close()
