import scrapy

class ResultItem(scrapy.Item):
	Name = scrapy.Field()
	Roll_Number = scrapy.Field()
	SGPA_sem_I = scrapy.Field()
	SGPA_sem_II = scrapy.Field()
	CGPA_1 = scrapy.Field()
	SGPA_sem_III = scrapy.Field()
	SGPA_sem_IV = scrapy.Field()
	CGPA_2 = scrapy.Field()
	SGPA_sem_V = scrapy.Field()