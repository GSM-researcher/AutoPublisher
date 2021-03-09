import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup   
import requests

class SpiderSpider(CrawlSpider):
        def __init__(self, *a, **kw):
                self.count = 1
                super().__init__(*a, **kw)

        def parse(self, response):
                filename = str(self.count) + '.html'
                self.count +=1
                with open('../downloded_html/'+filename, 'wb') as f:
                        f.write(response.body)
                        soup = BeautifulSoup(response.body,'html.parser')
                        for i in soup.select('link'):
                                if "stylesheet" in i['rel']:
                                        domain = response.url.split('.com')[0]+'.com'
                                        print(domain)
                                        css = i['href'].split('.css')[0]+'.css'
                                        css_address = domain + css
                                        print(css_address)
                                        page = requests.get(css_address,verify=False)
                                        with open('../downloded_html/css/' + self.count + '.css','w') as w:
                                                w.write(page)                    
        
        name = 'spider'
        start_urls = ['https://www.google.com/search?q=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&oq=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&aqs=chrome..69i57j35i39j69i60j69i65l3j69i61l2.3685j0j4&sourceid=chrome&ie=UTF-8']

        rules = [Rule(LinkExtractor(),
                      callback='parse',follow=True)]