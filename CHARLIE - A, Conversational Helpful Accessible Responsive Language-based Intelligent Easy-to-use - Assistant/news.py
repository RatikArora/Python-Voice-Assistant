import requests
from bs4 import BeautifulSoup
from texttovoice import speakandprinttext

def news():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')

    count = 0
    speakandprinttext("the top 5 headlines are : ")
    for x in headlines:
        count = count +1
        speakandprinttext(x.text.strip())
        if count ==5:
            break