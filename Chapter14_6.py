######################## Exercise 14_6 ############################
# Access http://Uszip.com with a Zipcode received from user input #
# Process site contents to filter out the City Name and Population#
# Quoc Bao                                           13/12/2018   #
###################################################################
import urllib
from pprint import pprint
from structshape import structshape


def getSitecontent(siteURL):
    '''Access siteURL <str> site contents using Urllib and
    grab these contents down to var sitecontent <list of str>'''
    print('Accessing site...')
    conn = urllib.request.urlopen(siteURL)
    sitecontent = []
    for line in conn:
        sitecontent.append(line.decode("utf8"))
    return sitecontent


def siteprocessing(sitecontent):
    '''Find,extract City name <str> and Zipcode <str>,
     population <str> from sitecontent'''
    # Find city name and zipcode to extract"
    print('Processing...')
    ZC_text_find = '<meta name="description"'
    Pop_text_find = 'Total population'
    for line in sitecontent:
        if ZC_text_find in line:
            # found city name and zipcode line
            CZtmp = line
        if Pop_text_find in line:
            Poptmp = line
            break
    # Extract the name
    CityText_start = CZtmp.find('code for ') + 9
    CityText_end = CZtmp.find('?', 50)
    CityName = CZtmp[CityText_start:CityText_end]
    ZipText_end = CZtmp.find(':', CityText_end)
    Zipcode = CZtmp[CityText_end + 2:ZipText_end]
    # Extract polulation information
    PopText_start = (Poptmp.find('Total population') + 25)
    PopText_end = (Poptmp.find('<', PopText_start))
    Population = Poptmp[PopText_start:PopText_end]
    return (CityName, Zipcode, Population)


def questZip(Zipcode):
    'Adding Zipcode <str> requested to Url'
    URL = 'https://www.uszip.com/zip/' + Zipcode
    site = getSitecontent(URL)
    (CityName, Zipcode, Population) = siteprocessing(site)
    print('%s has Zipcode: %s , Population are: %s' % (CityName, Zipcode, Population))


if __name__ == '__main__':
    Zipcode = input('Please give me a Zipcode:  ')
    questZip(Zipcode)
