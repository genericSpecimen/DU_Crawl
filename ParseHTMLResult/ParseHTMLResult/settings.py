BOT_NAME = 'ParseHTMLResult'

SPIDER_MODULES = ['ParseHTMLResult.spiders']
NEWSPIDER_MODULE = 'ParseHTMLResult.spiders'

ROBOTSTXT_OBEY = True

FEED_EXPORT_FIELDS = ['Name', 'Roll_Number', 'SGPA_sem_I', 'SGPA_sem_II', 'CGPA']