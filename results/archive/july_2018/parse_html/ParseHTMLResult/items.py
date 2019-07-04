import scrapy

class ResultItem(scrapy.Item):
	Name = scrapy.Field()
	Roll_Number = scrapy.Field()
	SGPA_sem_I = scrapy.Field()
	SGPA_sem_II = scrapy.Field()
	CGPA = scrapy.Field()