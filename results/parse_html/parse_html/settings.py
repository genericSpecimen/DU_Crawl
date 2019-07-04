BOT_NAME = 'parse_html'

SPIDER_MODULES = ['parse_html.spiders']
NEWSPIDER_MODULE = 'parse_html.spiders'

FEED_EXPORT_FIELDS = ['Name', 'Roll_Number', 'SGPA_sem_I', 'SGPA_sem_II', 'CGPA_1', 'SGPA_sem_III', 'SGPA_sem_IV', 'CGPA_2', 'SGPA_sem_V', 'SGPA_sem_VI', 'CGPA_3', 'Grand_CGPA', 'Division']