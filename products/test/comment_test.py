import scrapy

# scrapy runspider -s DOWNLOAD_DELAY=5.0 comment.py

class CommentSpider(scrapy.Spider):
    name = 'comment-spider'
    login_url = 'https://society6.com/login?done=/'
    start_urls = [login_url]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'email': 'xxxx@yyyy.com', 'password': '****'},
            callback=self.after_login
        )

    def after_login(self, response):
        if "The password must be at least 6 characters." in str(response.body) or "username or password is invalid" in str(response.body):
            self.logger.error("Login failed!")
            return
        else:
            # continue scraping with authenticated session...
            test_url = 'https://society6.com/product/low-poly-bb-8_print'
            return scrapy.FormRequest.from_response(
                response,
                formdata={'inputComment_styles_35vWd': 'Such a clean design! Beautiful.'}
            )
