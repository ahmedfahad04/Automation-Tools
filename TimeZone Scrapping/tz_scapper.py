import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://en.wikipedia.org/wiki/List_of_tz_database_time_zones')

print("Website Loaded...")

## Create Df for saving the info
df = pd.DataFrame(columns=['Id', 'TimeZone', 'UTC'])
info_tuple = []

# Find all card-body elements
table_data = driver.find_elements(By.TAG_NAME, 'tr')

i = 1

for data in table_data:
    
    timezone = ""
    utc = ""
    cell_data = data.text.split(' ')
    tz = [data for data in cell_data if '/' in data]
    std = [data for data in cell_data if ':' in data]
    
    if len(tz) >= 1:
        if '/' in tz[0]:
            timezone = tz[0]
        elif '/' in tz[1]:
            timezone = tz[1]
        
        if len(std) >= 1:
            print(timezone, '->', std[0].replace('Link†\n', ''))
            utc = std[0].replace('Link†\n', '')
            print("=========")
    
        if len(timezone) > 0:
            info_tuple.append([i, timezone, utc])
    
        i += 1
    
temp_df = pd.DataFrame(info_tuple, columns=['Id', 'TimeZone', 'UTC'])
df = df._append(temp_df)
df.to_csv('TimeZones.csv', index=False)
