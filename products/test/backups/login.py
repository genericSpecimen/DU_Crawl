import scrapy

class LoginSpider(scrapy.Spider):
    name = 'login-spider'
    start_urls = ['https://society6.com/login?done=/']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'email': 'xxxx@yyy.com', 'password': '*****'},
            callback=self.after_login
        )

    def after_login(self, response):
        filename = 'login.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        # continue scraping with authenticated session...
