import json


def address_image(symbol, name):
    """Checks the Image Address book for a symbols image"""
    file = open('image_address_book', 'r')
    file_json = file.readline()

    file_json = json.loads(file_json)

    symbol = str(symbol)
    symbol.lower()
    #   Needs a default value to return if site not in 'image_address_book.json'
    try:
        symbol_object = file_json['sites'][symbol]
    except KeyError:
        # Returns the default image on error
        image = 'http://placehold.it/150x80?text=IMAGE'
    else:
        image = symbol_object['image']
    file.close()

    return str(image)


def no_address(name):
    """Eventually create a spider to find a stock's logo/images if not already in address book"""
    pass
