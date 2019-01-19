import scrapy
from scrapy_splash import SplashRequest

class CommentSpider(scrapy.Spider):
    name = 'comment'
    login_url = 'https://society6.com/login?done=/'
    start_urls = [login_url]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'email': 'xxxx@yyyyy.com', 'password': '****'},
            callback=self.after_login
        )

    def after_login(self, response):
        if "The password must be at least 6 characters." in str(response.body) or "username or password is invalid" in str(response.body):
            self.logger.error("Login failed!")
            return
        else:
            # continue scraping with authenticated session...
            test_url = 'https://society6.com/product/low-poly-bb-8_print'
            
            script = """
            function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(5.0))

            assert(splash:runjs("document.querySelector('.button_styles_38MW-').click();"))
            assert(splash:wait(2.0))
            
            assert(splash:runjs([[
                var input_box = document.querySelector('.inputComment_styles_35vWd');
                    input_box.value = "Such a clean design, beautiful!"
            ]]))
            assert(splash:wait(2.0))
            assert(splash:runjs("document.getElementById('postComment').click();"))
            assert(splash:wait(2.0))

            return {
                html = splash:html(),
                --png = splash:png(),
            }
            end
            """

            yield SplashRequest(url=test_url,
                    callback=self.action,
                    endpoint='execute',
                    args={'lua_source': script})
    
    def action(self, response):
        title = response.selector.xpath('//title/text()').extract_first()
        filename = 'product_names'
        with open(filename, 'a') as f:
            f.write("{}\n".format(title))
