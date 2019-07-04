import scrapy
from parse_html.items import ResultItem
import os
class ParseResultsSpider(scrapy.Spider):
	name = 'parse_results'
	start_urls = ['file:///home/hooman/Downloads/results/Keshav_SEM-VI-CS/result_' + str(x) + '.html' for x in range(16035570001, 16035570100)]
	
	def parse(self, response):
		item = ResultItem()
		item['Name'] = response.selector.xpath('//span[@id="lblname"]/text()').extract()
		item['Roll_Number'] = response.selector.xpath('//span[@id="lblrollno"]/text()').extract()
		item['SGPA_sem_I'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[2]/td[4]/text()').extract()
		item['SGPA_sem_II'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[3]/td[4]/text()').extract()
		item['CGPA_1'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[3]/td[6]/text()').extract()
		item['SGPA_sem_III'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[4]/td[4]/text()').extract()
		item['SGPA_sem_IV'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[5]/td[4]/text()').extract()
		item['CGPA_2'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[5]/td[6]/text()').extract()
		item['SGPA_sem_V'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[6]/td[4]/text()').extract()
		item['SGPA_sem_VI'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[7]/td[4]/text()').extract()
		item['CGPA_3'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[7]/td[6]/text()').extract()

		gcgpa = response.selector.xpath('//*[@id="lbl_gr_cgpa"]/font/text()').extract()
		if gcgpa:
			gcgpa_str = gcgpa.pop().split(':')[1].split(',')[0].lstrip()
		else:
			gcgpa_str = 'NA'
		item['Grand_CGPA'] = gcgpa_str

		division = response.selector.xpath('//*[@id="lbldiv"]/font/text()').extract()
		if division:
			division_str = division.pop().split(':')[1].lstrip()
		else:
			division_str = 'NA'
		item['Division'] = division_str

		yield item
