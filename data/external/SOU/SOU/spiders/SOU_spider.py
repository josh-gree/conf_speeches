import scrapy

from SOU.items import SouItem
from bs4 import BeautifulSoup

class SOUSpider(scrapy.Spider):
    name = "souspider"
    allowed_domains = ["stateoftheunion.onetwothree.net"]
    start_urls = ("http://stateoftheunion.onetwothree.net/texts/index.html",)

    def parse(self, response):

        links = map(response.urljoin,response.css('a::attr(href)')[5:-2].extract())
        for link in links:
            yield scrapy.Request(link,callback=self.extract_speech)

    def extract_speech(self,response):

        text = ''.join(response.css('p').extract())
        text = BeautifulSoup(text).text.replace("\n"," ")
        speaker = response.css('h2::text').extract()[0]
        date = int(response.css('h3::text').extract()[0].split()[-1])

        item = SouItem()
        item['text'] = text
        item['speaker'] = speaker
        item['date'] = date

        yield item
