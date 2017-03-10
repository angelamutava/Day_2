import urllib2, urllib, json
from prettytable import PrettyTable

def get_universities(country_name):
    base_url = "http://universities.hipolabs.com/search?"
    full_url = base_url + country_name + "&format=json"
    try:
        result = urllib2.urlopen(full_url).read()
        data = json.loads(result)
        university_table = PrettyTable(["Key", "Value"])
        for item in data:
            for key, value in item.items():
                university_table.add_row([key, value])
            print university_table    
    except urllib2.URLError as e:
        print "No internet connection, connect and try again."    


get_universities("middle")