from bs4 import BeautifulSoup
import requests

with open('basketballstats.txt', 'w') as r:
    r.write('NBA_PLAYER_DATA\n')

season_list = ["2015", "2016", "2017", "2018", "2019"]


def make_urls(seasons):
    url = 'https://www.basketball-reference.com/leagues/NBA_'
    urls = []
    for season in seasons:
        urls.append(url + season.replace(' ', '+') + '_per_poss.html')
    return urls


def scraper(urls):
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        stat_table = soup.find_all("table", id="per_poss_stats")
        stat_table = stat_table[0]
        with open('basketballstats.txt', 'a') as r:
            for row in stat_table.find_all('tr'):
                for cell in row.find_all('td'):
                    r.write(cell.text.ljust(30))
                r.write('\n')


scraper(make_urls(season_list))
