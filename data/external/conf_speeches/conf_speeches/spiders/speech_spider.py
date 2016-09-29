# -*- coding: utf-8 -*-
import scrapy
from conf_speeches.items import ConfSpeechesItem
from bs4 import BeautifulSoup

class ConfSpeechesSpider(scrapy.Spider):
    name = "conf"
    allowed_domains = ["www.britishpoliticalspeech.org"]
    start_urls = (
        'http://www.britishpoliticalspeech.org/speech-archive.htm?q=Leader%27s+speech&speaker=&party=&searchRangeFrom=1895&searchRangeTo=2015',
    )

    def parse(self, response):
        res = {}
        out = response.css('tbody')[1].css('tr')
        for sel in out:
            url = sel.css('td')[-1].css('::attr(href)').extract_first()
            url = response.urljoin(url)
            yield scrapy.Request(url,callback=self.extract_speech)

    def extract_speech(self, response):
        item = ConfSpeechesItem()
        text = ''.join(response.xpath('//div[@class="speech"]').xpath('//div[@class="speech-content"]').css('p').extract())
        item['text'] = BeautifulSoup(text).text
        item['speaker'] = response.xpath('//div[@class="speech"]').xpath('//p[@class="speech-speaker"]').css('::text').extract()[0]
        date = response.xpath('//div[@class="speech"]').css('h3').extract()[0]
        item['date'] = BeautifulSoup(date).text

        yield item #cleantext,speaker,date
