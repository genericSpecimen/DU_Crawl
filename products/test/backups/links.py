import scrapy

class CommentSpider(scrapy.Spider):
    name = 'comment-spider'
    base_url = 'https://society6.com/s?q=new+wall-art'
    start_urls = [base_url]

    def parse(self, response):
        product_baseurl = 'https://society6.com'        
        links = []
        divs = response.xpath("//a[@class='link_product_3ebk3']")
        
        for i in divs.xpath(".//@href"):
            if i.extract() not in links:
                links.append(i.extract())
        
        filename = 'product_links'
        with open(filename, 'w') as f:
            for item in links:
                f.write("{}\n".format(product_baseurl + item))
                yield scrapy.Request(url = product_baseurl + item, callback = self.action)
    
    def action(self, response):
        title = response.selector.xpath('//title/text()').extract_first()
        filename = 'product_names'
        with open(filename, 'a') as f:
            f.write("{}\n".format(title))