import os
os.system("scrapy crawl --nolog parse_results -o data.csv -t csv")
print(".csv file generated.")