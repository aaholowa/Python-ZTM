import requests  # allows us to download html files from a website

# allows us to use the html files and grab different data
from bs4 import BeautifulSoup

import pprint

url = 'https://news.ycombinator.com/news'
response = requests.get(url)  # grabs the html information

# print(response) # Gives the status code
# print(response.text)  # displays the actual html code

# convert the html from a string to an object
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.storylink')  # grab story links
subtext = soup.select('.subtext')  # grab story subtext (scores within subtext)


def sort_stories(hacker_list):
    return sorted(hacker_list, key=lambda k: k['votes'], reverse=True)


def hacker_news(links, subtext):
    news = []
    for index, item in enumerate(links):
        title = item.getText()  # text titles
        # gives us the link to the title (default value of None)
        href = item.get('href', None)
        votes = subtext[index].select('.score')

        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:
                # dict with title and correspnding link
                news.append({'title': title, 'link': href, 'votes': points})

    return news


pprint.pprint(hacker_news(links, subtext))
