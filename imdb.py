
import scrapy
#from ..items import ImdbItem
#from scrapy import Request
#from urllib.parse import urljoin
#from urllib.parse import urlparse
import requests
#from bs4 import BeautifulSoup
import sys
sys.path.append('/Users/redkit/Desktop/imdb-odev/imdb/imdb')
from items import ImdbItem




class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ["https://www.imdb.com/list/ls004610270/?st_dt=&mode=detail&page=1&sort=list_order,asc&ref_=ttls_vm_dtlhttps://www.imdb.com/list/ls004610270/?st_dt=&mode=detail&page=1&sort=list_order,asc&ref_=ttls_vm_dtl"]

    def parse(self, response):
        hrefs = response.css("div.lister-item-content a ::attr(href)").extract()

        for href in hrefs:
            url = response.urljoin(href)
            #html = requests.get(url).content
            #self.soup=BeautifulSoup(html,"html.parser")
            yield scrapy.Request(url,callback=self.parse_page)


        next_page = response.css("a.flat-button.lister-page-next.next-page ::attr(href)")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url,self.parse)

    def parse_page(self,response):
        item = ImdbItem()

        film_name = response.css("div.title_wrapper h1 ::text")[0].extract().strip()
        film_date = response.css("div.subtext a ::text")[-1].extract().strip().split("(")[0]
        film_country = response.css("div.subtext a ::text")[-1].extract().strip().split()[3].strip("()")
        film_director = response.css("div.credit_summary_item a ::text")[0].extract()
        film_stars = response.css("div.credit_summary_item a ::text")[-4:-1].extract()
        film_rate = response.css('div.ratingValue span::text')[0].extract()

        item['film'] = film_name
        item['date'] = film_date
        item['country'] = film_country
        item['director'] = film_director
        item['stars'] = film_stars
        item['rate'] = film_rate

        yield item

