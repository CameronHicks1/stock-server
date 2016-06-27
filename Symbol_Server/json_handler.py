import json


def read_json():
    """Reads sites.json file and converts to python friendly data type"""
    file = open('sites', 'r')
    sites = file.read()

    sites_list = []

    converted = json.loads(sites)
    # Appends sites from JSON object 'sites' to sites_list for python usable object(Array)
    for site in converted['sites']:
        sites_list.append(site)

    file.close()
    # Returns array for Updater.py
    return sites_list


def add_site(site):
    """Opens 'sites.json' and appends site."""
    file = open('sites', 'r+')
    sites = file.read()

    site = str(site.upper())
    sites_list = []

    converted = json.loads(sites)
    # Appends sites from JSON object 'sites' to sites_list for python usable object(Array)
    for site_x in converted['sites']:
        sites_list.append(site_x)

    # Adds new site to sites list
    if site in sites_list:
        return
    else:
        sites_list.append(site)

    # JSON serializes new list and saves to 'sites.json'
    #   -closes file then reopens in 'w' mode to erase original content
    json_text = '{"sites": ' + str(sites_list) + '}'
    new_json = json_text.replace("'", "\"")  # json.dumps(json_text)
    file.close()

    update_file = open('sites', 'w')
    update_file.write(new_json)

    update_file.close()


def remove_site(site):
    """Opens 'sites.json' removes site"""
    file = open('sites', 'r+')
    sites = file.read()

    site = str(site.upper())
    sites_list = []

    converted  = json.loads(sites)
    # Appends sites from JSON object 'sites' to sites_list for python usable object(Array)
    for site_x in converted['sites']:
        sites_list.append(site_x)

    # Removes site from sites list
    if site in sites_list:
        sites_list.remove(site)
    else:
        return

    # JSON serializes new list and saves to 'sites.json'
    #   -closes file then reopens in 'w' mode to erase original content
    json_text = '{"sites": ' + str(sites_list) + '}'
    new_json = json_text.replace("'", "\"")  # json.dumps(json_text)
    file.close()

    update_file = open('sites', 'w')
    update_file.write(new_json)

    update_file.close()
