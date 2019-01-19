import scrapy
import os.path
current_roll_number = 0
class ResultSpider(scrapy.Spider):
    name = 'result-spider'
    result_url = 'http://duresult.in/students/Combine_GradeCard.aspx'
    start_urls = [result_url]
    
    def __init__(self, roll_number=16058570001):
        global current_roll_number
        self.roll_number = roll_number
        current_roll_number = self.roll_number

    def parse(self, response):
        captcha_src = response.xpath('//img[@id="imgCaptcha"]/@src').extract_first()
        captcha = captcha_src.split('=')[1].split('&')[0]
        data = {
                'txtrollno': str(self.roll_number),
                'ddlcollege': '058',
                'txtcaptcha': captcha,
                'btnsearch' : 'Print+Score+Card'
                }
        yield scrapy.FormRequest.from_response(
                response,
                formdata=data,
                callback=self.parse_result,
                )
        print("Fetching result for roll number: {}".format(self.roll_number))

    def parse_result(self, response):
        filename = "result_" + str(current_roll_number) + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        if os.path.isfile("result_" + str(current_roll_number) + '.html'):
            print("Your result has been successfully generated.")
            print("--------------------------------------------")
