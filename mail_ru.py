import requests
from lxml import html
from pprint import pprint

def get_dom(url, header):
    response = requests.get(url, headers=header)
    dom = html.fromstring(response.text)
    return dom

url = 'https://news.mail.ru/'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/87.0.4280.88 Safari/537.36'}
raw_dom = get_dom(url, header)

raw_links_xpath = "//a[contains(@class, 'js-topnews__item')]/@href"
raw_links = raw_dom.xpath(raw_links_xpath)

all_news = []
for link in raw_links:
    data_news={}
    news_dom = get_dom(link, header)
    text = news_dom.xpath("//span[@class='hdr__text']//h1/text()")[0]
    source = news_dom.xpath("//span[@class='breadcrumbs__item']//span[@class='link__text']/text()")[0]
    date = news_dom.xpath("//span[@class='breadcrumbs__item']//span[@class='note__text breadcrumbs__text js-ago']"
                          "/@datetime")[0]
    data_news['text'] = text
    data_news['source'] = source
    data_news['link'] = link
    data_news['date'] = date
    all_news.append(data_news)
pprint(all_news)
