import os
os.system("scrapy crawl parse_results -o data.csv -t csv")
print(".csv file generated.")