BOT_NAME = 'parse_html'

SPIDER_MODULES = ['parse_html.spiders']
NEWSPIDER_MODULE = 'parse_html.spiders'

ROBOTSTXT_OBEY = True

FEED_EXPORT_FIELDS = ['Name', 'Roll_Number', 'SGPA_sem_I', 'SGPA_sem_II', 'CGPA_1', 'SGPA_sem_III', 'SGPA_sem_IV', 'CGPA_2', 'SGPA_sem_V']
