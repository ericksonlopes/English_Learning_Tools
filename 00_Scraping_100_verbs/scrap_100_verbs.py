import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.todamateria.com.br/verbos-em-ingles/')

soup = BeautifulSoup(req.content, 'html.parser')

verbs = []

for line in soup.find('table').find_all('tr')[1:]:
    if 'To ' in line.get_text():
        preset = line.find_all('td')[0].get_text()[3:]
    else:
        preset = line.find_all('td')[0].get_text()

    past = line.find_all('td')[2].get_text()

    with open('100_verbs.csv', 'a') as file_csv:
        file_csv.write(f'{preset},{past}\n')
