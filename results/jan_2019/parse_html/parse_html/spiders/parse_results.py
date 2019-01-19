import scrapy
from parse_html.items import ResultItem
import os
class ParseResultsSpider(scrapy.Spider):
	name = 'parse_results'
	start_urls = ['file:///home/hooman/Documents/tutorial-env/captcha-test/Download/result_' + str(x) + '.html' for x in range(16058570001, 16058570042)]
	
	def parse(self, response):
		item = ResultItem()
		item['Name'] = response.selector.xpath('//span[@id="lblname"]/text()').extract()
		item['Roll_Number'] = response.selector.xpath('//span[@id="lblrollno"]/text()').extract()
		item['SGPA_sem_I'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[2]/td[4]/text()').extract()
		item['SGPA_sem_II'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[3]/td[4]/text()').extract()
		item['CGPA_1'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[3]/td[6]/text()').extract()
		item['SGPA_sem_III'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[4]/td[4]/text()').extract()
		item['SGPA_sem_IV'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[5]/td[4]/text()').extract()
		item['SGPA_sem_IV'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[5]/td[4]/text()').extract()
		item['CGPA_2'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[5]/td[6]/text()').extract()
		item['SGPA_sem_V'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[6]/td[4]/text()').extract()
		yield item
