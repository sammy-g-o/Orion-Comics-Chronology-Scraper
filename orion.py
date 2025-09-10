from bs4 import BeautifulSoup
import requests

response = requests.get("https://dc.fandom.com/wiki/Orion_(Prime_Earth)")
soup = BeautifulSoup(response.text, "html.parser")

lists = soup.find("ol", attrs={"class":"references"})
cleaned_text = str(lists.text).replace('\u2191', '?')

with open('orion_reading_guide.txt','w') as file:
    file.write(cleaned_text)