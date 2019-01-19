import scrapy
import os.path
current_roll_number = 0
class ResultSpider(scrapy.Spider):
    name = 'result-spider'
    result_url = 'http://duexam.du.ac.in/RSLT_MJ2018/Students/Combine_GradeCard.aspx'
    start_urls = [result_url]
    
    def __init__(self, roll_number=17058570001):
        global current_roll_number
        self.roll_number = roll_number
        current_roll_number = self.roll_number

    def parse(self, response):
        data = {
                'txtrollno': str(self.roll_number),
                'ddlcollege': '058',
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
