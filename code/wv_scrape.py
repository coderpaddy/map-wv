import requests
from bs4 import BeautifulSoup as BS

url = "https://www.mapwv.gov/assessment/Assessment?Counties=1&OwnerName=Weaver&District=1"
request = requests.get(url)
soup = BS(request.content, 'html.parser')
record_count = soup.find("span", id="MainContent_lblRecordCount")
table = soup.find("table", id="MainContent_GridView1")
table_rows = table.find_all("tr")[1:]
print(len(table_rows))
record_dict = {}
for table_row in table_rows:
    tr_index = table_rows.index(table_row)
    record_dict[tr_index] = {
        "root_parcel_id": table.find("a", id=f"MainContent_GridView1_hlCleanParcelID_{tr_index}").get_text(),
        "current_owner": table.find("span", id=f"MainContent_GridView1_Label4_{tr_index}").get_text(),
        "property_address": table.find("span", id=f"MainContent_GridView1_Label13_{tr_index}").get_text(),
        "county": table.find("span", id=f"MainContent_GridView1_Label16_{tr_index}").get_text(),
        "district": table.find("span", id=f"MainContent_GridView1_Label6_{tr_index}").get_text(),
        "tax_map": table.find("a", id=f"MainContent_GridView1_hlMap_{tr_index}").get_text(),
        "parcel": table.find("span", id=f"MainContent_GridView1_Label9_{tr_index}").get_text(),
        "gis_map": table.find("span", id=f"MainContent_GridView1_hlMapLink_{tr_index}").get_text(),
        "flood_tool": table.find("span", id=f"MainContent_GridView1_hlFloodLink_{tr_index}").get_text(),
        "deeded_acres": table.find("span", id=f"MainContent_GridView1_Label10_{tr_index}").get_text(),
        "property_class": table.find("span", id=f"MainContent_GridView1_Label1_{tr_index}").get_text(),
        "land_use_code": table.find("span", id=f"MainContent_GridView1_Label2_{tr_index}").get_text(),
        "tax_class": table.find("span", id=f"MainContent_GridView1_Label11_{tr_index}").get_text(),
        "building_appraisal": table.find("span", id=f"MainContent_GridView1_Label12_{tr_index}").get_text(),
        "land_appraisal": table.find("span", id=f"MainContent_GridView1_Label13_{tr_index}").get_text(),
        "total_appraisal": table.find("span", id=f"MainContent_GridView1_Label14_{tr_index}").get_text(),
        }


print(record_dict[0])