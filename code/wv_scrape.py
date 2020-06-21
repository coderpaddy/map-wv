import csv
import os

from requests_html import HTMLSession
from bs4 import BeautifulSoup as BS

from sheet_data import counties, get_refiner

session = HTMLSession()

def check_if_csv(url):
    request = session.get(url)
    has_csv = request.html.search('<a id="MainContent_hlExportURL" href="{csv_url}" style="color:Blue;font-size:12px;">Click here</a>')['csv_url']
    if has_csv:
        return has_csv
    else:
        return False

def get_csv(url):
    request = session.get(url)
    link_for_csv = request.html.search('<a id="MainContent_hlExportURL" href="{csv_url}" style="color:Blue;font-size:12px;">Click here</a>')['csv_url']
    return link_for_csv

def save_csv(csv_file, csv_content):
    csv_file.write(csv_content)
    csv_file.close()
    


print(counties.keys())

which_county = input("Please enter the number of the county: ")
county_code = list(counties.keys())[list(counties.values()).index(which_county)]

url = f"https://www.mapwv.gov/assessment/Assessment?Counties={which_county}"
request = session.get(url)
soup = BS(request.html.html, 'html.parser')
district_select = soup.find("select", id="MainContent_ddlbDistrict")
select_options = [x.get_text() for x in district_select.find_all("option")]
print("Which District? :", select_options)
district_code = input("Please enter the number of the district ")

#
#
#Scrape
#
#

url = f"https://www.mapwv.gov/assessment/Assessment?Counties={which_county}&District={district_code}"
check_csv_url = check_if_csv(url)
if check_csv_url is not False:
    r = session.get(check_csv_url, allow_redirects=True)
    open(f'{which_county}-{district_code}.csv', 'wb').write(r.content)
else:
    print("Too Many Results. Scrapin Manually: ")
    page_list = request.html.search('<span id="MainContent_lblPageRange" style="font-size:12px;">Page {page_count}</span>')['page_count'].split(" ")[-1]


# Check if has csv
# if not narrow search
#       Check if has csv
#       if not narrow search
