# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.insert(0,'/home/neehar/Desktop/webdevTutorials/moviePrediction/movie_rating_prediction/movie')
from scrapy.selector import Selector
from items import MovieBudgetItem

# shell command to run:
# $ scrapy crawl movie_budget -o movie_budget.json


class MovieBudgetSpider(scrapy.Spider):
    name = "movie_budget"
    allowed_domains = ["the-numbers.com"]

#    start_urls = (
#        'http://www.the-numbers.com/movie/budgets/all/' + str(page),
#    )

    def start_requests(self):
	url = "http://www.the-numbers.com/movie/budgets/all/{}"
	page_num = list(range(1, 5402, 100))
	links = [url.format(i) for i in page_num]
	for link in links:
		yield scrapy.Request(url=link, callback=self.parse)

    def parse(self, response):
        base_link = 'http://www.the-numbers.com'

        print "=" * 50  
        rows_in_big_table = response.xpath("//table/tr") 
        
        # now we only consider rows with odd index number, namely, skip useless rows
        for i, onerow in enumerate(rows_in_big_table):
            if i % 2 == 0:
                continue

            movie_budget_item = MovieBudgetItem()

            release_date = onerow.xpath('td/a/text()').extract()[0]
            _partial_url = onerow.xpath('td/b/a/@href').extract()[0]
            movie_link = base_link + _partial_url
            movie_name = onerow.xpath('td/b/a/text()').extract()[0]

            budgets = onerow.xpath('td[@class="data"]/text()').extract()[1:]
            production_budget = budgets[0]
            domestic_gross = budgets[1]
            worldwide_gross = budgets[2]

            movie_budget_item['release_date'] = release_date
            movie_budget_item['movie_link'] = movie_link
            movie_budget_item['movie_name'] = movie_name
            movie_budget_item['production_budget'] = production_budget
            movie_budget_item['domestic_gross'] = domestic_gross
            movie_budget_item['worldwide_gross'] = worldwide_gross

            print "=" * 50 
            yield movie_budget_item
