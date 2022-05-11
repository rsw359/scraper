import requests
from bs4 import BeautifulSoup


def get_citation_count(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    anchors = soup.find_all('a', text='citation needed')  # can use find_all
    print(len(anchors))


get_citation_count("https://en.wikipedia.org/wiki/History_of_Mexico")


def get_citations_needed_report(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    anchors = soup.find_all('a', text='citation needed')

    for anchor in anchors:
        print(anchor.parent.parent.parent.text)


get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")
