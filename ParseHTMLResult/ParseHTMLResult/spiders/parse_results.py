import scrapy
from ParseHTMLResult.items import ResultItem

class ParseResultsSpider(scrapy.Spider):
    name = 'parse_results'
    start_urls = ['file:///home/hooman/Documents/dev/DownloadHTMLResults/Downloaded/result_' + str(x) + '.html' for x in range(17058570001, 17058570053)]

    def parse(self, response):
        item = ResultItem()
        item['Name'] = response.selector.xpath('//span[@id="lblname"]/text()').extract()
        item['Roll_Number'] = response.selector.xpath('//span[@id="lblrollno"]/text()').extract()
        item['SGPA_sem_I'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[2]/td[4]/text()').extract()
        item['SGPA_sem_II'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[3]/td[4]/text()').extract()
        item['CGPA'] = response.selector.xpath('//table[@id="gv_sgpa"]/tr[3]/td[6]/text()').extract()

        yield item
