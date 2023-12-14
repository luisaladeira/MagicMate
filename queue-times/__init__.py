import requests
from bs4 import BeautifulSoup
import os



date = '2023-12-11'
url = f"https://queue-times.com/pt-BR/parks/65/rides/6006?given_date={date}"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Find the table based on the title
target_h2 = soup.find('h2', text='\nTempo médio de fila por hora (desde o começo)\n').find_next('table')

# Extract data from the table
if target_h2:
    matrix = []
    rows = target_h2.find_all('tr')
    for row in rows:
        # if 'Hora' not in row[0]:
            cols = row.find_all(['th', 'td'])
            cols = [col.text.strip() for col in cols]
        # matrix.append(cols)

else:
    print("Table not found.")
    

    

