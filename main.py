import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.hopkinsmedicine.org/profiles/search"

data = {"Name": [], "Title": []}


    

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify)

#code to scrape names of doctors
spans = soup.find_all('span', class_ = "doctor-name info")

for span in spans:
    print(span.text)
    data["Name"].append(span.text) 
  
    
#code to scrape expertise of doctors
spans2 = soup.find_all('div', class_ = "bottom")

for span2 in spans2:
    print(span2.string)    







df = pd.DataFrame.from_dict(data)
df.to_excel("data.xlsx", index=False)
