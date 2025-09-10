# Orion-Comics-Chronology-Scraper
This Python script uses BeautifulSoup and requests to scrape the DC Fandom wiki for the chronological appearances of the character Orion. It extracts a reading guide and saves the list of comics to a local text file.
# Prerequisites
Python installed on your system.
The requests and beautifulsoup4 libraries:
pip install requests beautifulsoup4


# How to Use
Make sure all prerequisites are installed.
Run the script from your terminal:
python orion.py


The script will connect to the dc.fandom.com page for Orion, scrape the reference list, and save the cleaned-up text to a new file named orion_reading_guide.txt.
