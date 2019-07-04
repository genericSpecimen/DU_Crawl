# Result Crawler
A simple crawler to download the results of my classmates from a university website, which requires filling up a standard HTML form. The response body for each request is written into a .html file and a .csv file can be generated from these HTML files if required.

### Dependencies
1. [python](https://www.python.org/)
2. [scrapy](https://scrapy.org/)

### Usage
1. To fetch the .html files, run ```python get_results_script.py``` in the [download_html](./download_html) folder.
2. Before running the scraper [parse_results_script.py](./parse_html/parse_results_script.py), we need to modify a line in [parse_results.py](./parse_html/parse_html/spiders/parse_results.py). We will specify the location of these .html files in the [6th line](./parse_html/parse_html/spiders/parse_results.py#L6).
```
	start_urls = ['file:///home/user/path/to/results/result_' + str(x) + '.html' for x in range(17058570001, 17058570053)]'
```
If you're unsure about the path, simply open any of the .html files in your browser and copy and paste the url in a way that the roll numbers and .html are not in the link, as they are automatically added by + 'str(x)' and + '.html'.

3. You can now run ```python parse_results_script.py``` in the [parse_html](./parse_html) folder and a data.csv file will be generated. 

### Understanding the code structure

I've broken this project into two parts, one downloads the .html files and the other will use these downloaded files to scrape data from them. The reason for doing this was because the university website responds to requests lazily. So, I chose to separate the network part. Another reason was to maintain the philosophy of a tool doing only one thing, and then such tools can be combined to perform what is required.

1. The [download_html](./download_html) folder contains the script to fetch the results. The script [get_results_script.py](./download_html/get_results_script.py) executes the script [get_html.py](./download_html/get_html.py) for the range of roll numbers specified in [line 6 of get_results_script.py](./download_html/get_results_script.py#L6).

2. The [parse_html](./parse_html) folder contains the code for scraping the desired data in our previously downloaded .html files. The script [parse_results_scripts.py](./parse_html/parse_results_script.py) executes the script [parse_results.py](./parse_html/parse_html/spiders/parse_results.py) in the [parse_html/parse_html/spiders](./parse_html/parse_html/spiders) folder and writes the required data into a data.csv file.

### License
Do whatever you want to do with this.
