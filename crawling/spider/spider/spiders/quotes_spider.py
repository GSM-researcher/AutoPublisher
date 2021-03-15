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
                if "google" in response.url:
                        return
                print(response.url)
                filename = str(self.count) + '.html'
                flag = 1
                soup = BeautifulSoup(response.body,'html.parser')
                for i in soup.select('link'):
                        if "stylesheet" in i['rel']:
                                flag = 0
                                domain = response.url.split('.com')[0]+'.com'
                                css = i['href'].split('.css')[0]+'.css'
                                
                                '''css_address = domain + css
                                print(css_address)
                                page = requests.get(css_address,verify=False)
                                with open('../downloded_html/css/' + self.count + '.css','w') as w:
                                        w.write(page)'''   
                if flag == 1:
                        with open('../downloded_html/'+filename, 'wb') as f:
                                print()
                                print(filename)
                                print()
                                
                                f.write(response.body)
                                self.count +=1
                                        
        
        name = 'spider'
        start_urls = ['https://www.google.com/search?q=%ED%81%AC%EB%A1%A4%EB%A7%81&oq=%ED%81%AC%EB%A1%A4%EB%A7%81&aqs=chrome..69i57j35i39j0i131i433j0i433j0i131i433j0i433j0j69i61.2498j1j4&sourceid=chrome&ie=UTF-8']

        rules = [Rule(LinkExtractor(),
                      callback='parse',follow=True,)]