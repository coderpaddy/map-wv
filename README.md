# Map-WV Scraper


# Install
 
 ```
 git clone https://github.com/coderpaddy/map-wv.git
 cd map-wv
 # You may want to create a virtual environment
 # python3 -m venv env
 pip3 install -r requirements.txt
 ```

# Usage
 
 ```
 python3 code/wv_scrape.py

 # You will be asked to choose a number for the county

 30

 # you will be asked to pick a number for the district

 # If there are too many results (the site doesnt like it)
 # So the search narrows by value

 {county_num}-{county_name}.csv in root folder
 ```