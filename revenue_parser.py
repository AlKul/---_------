import pandas as pd
import requests
from lxml.html import fromstring
from fp.fp import FreeProxy

df = pd.read_pickle('./pickle_files/All_companies.pkl')

companies = df['company_name'].to_list()

def get_revenue_for_company(company_name):
    url = 'https://bo.nalog.ru/search'
    headers = {
        'User Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        }
    params = {
        'query':company_name,
        'page':'1',
    }
proxies = FreeProxy().get_proxy_list()[0]
url = 'https://bo.nalog.ru/search'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
params = {
    'query':companies[0],
    'page':'1',
}
xpath = '//div[contains(@class, "results-search-tbody")]/a[1]'
response = requests.get(url, headers=headers, params=params, proxies={"http": proxies})
dom = fromstring(response._content)
items = dom.xpath(xpath)
print(len(items))



from requests_html import HTMLSession
from requests_html import AsyncHTMLSession

url2search = url
session = HTMLSession()
r = session.get(url2search, headers=headers, params=params)

dom = fromstring(r.content)
items = dom.xpath(xpath)
print(len(items))

from requests_html import HTMLSession

s  = HTMLSession()
response = s.get(url)
response.html.render()

print(response)

get_revenue_for_company(companies[0])