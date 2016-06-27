from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from json_handler import read_json, add_site, remove_site
from image_finder import address_image
from updater import write_new_file


def stock_symbol(request):
    """ Home Page for individual stock"""
    html = open('stock_symbol.html', 'r')
    response = ''
    for line in html:
        response += str(line)
    html.close()

    symbol = '%(symbol)s' % request.matchdict
    #   Open stock file and read lines for data
    file_name = str(symbol) + '.txt'
    file = open(file_name, 'r')

    name = str(file.readline())
    current_price = str(file.readline())
    last_close = str(file.readline())
    dividend = str(file.readline())
    div_yield = str(file.readline())
    low = str(file.readline())
    high = str(file.readline())
    rating = str(file.readline())
    datetime = str(file.readline())

    file.close()

    # Retrieve Image
    image1 = address_image(str(symbol.lower()), name)

    return Response(response.replace('{symbol}', symbol).replace('{name}', name).replace(
        '{current_price}', current_price).replace('{last_close}', last_close).replace(
        '{dividend}', dividend).replace('{yield}', div_yield).replace('{low}', low).replace(
        '{high}', high).replace('{rating}', rating).replace('{datetime}', datetime).replace(
        '{image1}', image1
    )
    )


def stock_home(request):
    """Home for Stock portion of site"""
    html = open('stock_home.html', 'r')
    response = ''
    for line in html:
        response += str(line)

    html.close()

    # Create HTML element for each stock in list
    symbols = read_json()
    symbols = reversed(sorted(symbols))

    for symbol in symbols:
        # Creates element for each stock
        element = ('<div class="list-group">' + '<a href="#" class="list-group-item" id="' + str(symbol) + '">' +
                   symbol + '<span class="badge" style="background-color: white;  vertical-align: middle;' +
                   'margin-top: -0.5em;">' +
                   '<button class="remove btn btn-danger" id="' + str(symbol) + '" style="padding: ' +
                   '2px;">remove</button></span>' +
                   '</a>' + '\n')
        #   Adds link for each element
        link = ('/stocks/' + symbol)
        element = element.replace('#', link)
        response = response.replace('<div class="list-group">', element)

    return Response(response)


#                                       AJAX TESTING
def post_handler(request):
    """Accepts JSON object with new site, adds site to list"""
    js = request.json_body
    # Filter JSON
    if "remove_site" in str(js):
        js_object = str(js).replace("{'remove_site': '", "")
        symbol = js_object.replace("'}", "")

        # Removes stock site from json list
        remove_site(symbol)
        return Response("{response: 'OK'}")

    elif "new_site" in str(js):
        js_object = str(js).replace("{'new_site': '", "")
        symbol = js_object.replace("'}", "")

        # Add stock site to json list
        add_site(symbol)
        write_new_file(symbol)

    else:
        pass

    return Response("{response: 'OK'}")
#                                      /AJAX TESTING

if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_chameleon')

    config.add_route('stock_home', '/stocks/')
    config.add_view(stock_home, route_name='stock_home')

    config.add_route('stocks', '/stocks/{symbol}')
    config.add_view(stock_symbol, route_name='stocks')

    # AJAX Config
    config.add_view(post_handler)

    app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
