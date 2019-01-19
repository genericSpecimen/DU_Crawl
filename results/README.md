# Result Crawler
A simple crawler to download the results of my classmates from a university website, which requires filling up a standard HTML form. The response body for each request is written into a .html file.

### Dependencies
1. [python](https://www.python.org/)
2. [scrapy](https://scrapy.org/)

### Usage
1. To fetch the .html files, run ```python get_results_script.py``` in the [jan_2019/download_html](https://github.com/genericSpecimen/crawl-scripts/tree/master/results/jan_2019/download_html) folder.
2. Before running the scraper [parse_results_script.py](https://github.com/genericSpecimen/crawl-scripts/blob/master/results/jan_2019/parse_html/parse_results_script.py), we need to modify a line in [parse_results.py](https://github.com/genericSpecimen/crawl-scripts/blob/master/results/jan_2019/parse_html/parse_html/spiders/parse_results.py). We will specify the location of these .html files in the [6th line](https://github.com/genericSpecimen/crawl-scripts/blob/403099eefd3fc822640519fdea428c9d48a61773/results/jan_2019/parse_html/parse_html/spiders/parse_results.py#L6).
```
	start_urls = ['file:///home/user/path/to/results/result_' + str(x) + '.html' for x in range(17058570001, 17058570053)]'
```
If you're unsure about the path, simply open any of the .html files in your browser and copy and paste the url in a way that the roll numbers and .html are not in the link, as they are automatically added by + 'str(x)' and + '.html'.

3. You can now run ```python parse_results_script.py``` and data.csv file will be generated. 

### Understanding the code structure

1. The [jan_2019/download_html](https://github.com/genericSpecimen/crawl-scripts/tree/master/results/jan_2019/download_html) folder contains the script to fetch the results. The script [get_results_script.py](https://github.com/genericSpecimen/crawl-scripts/blob/master/results/jan_2019/download_html/get_results_script.py) executes the script [get_html.py](https://github.com/genericSpecimen/crawl-scripts/blob/master/results/jan_2019/download_html/get_html.py) for the range of roll numbers specified in [line 6 of get_results_script.py](https://github.com/genericSpecimen/crawl-scripts/blob/c7318378cd4098ab9c22992f829d4556a0c5cf85/results/jan_2019/download_html/get_results_script.py#L6).

2. The [jan_2019/parse_html](https://github.com/genericSpecimen/crawl-scripts/tree/master/results/jan_2019/parse_html) folder contains the code for scraping the desired data in our previously downloaded .html files. The script [parse_results_scripts.py](https://github.com/genericSpecimen/crawl-scripts/blob/master/results/jan_2019/parse_html/parse_results_script.py) executes the script [parse_results.py](https://github.com/genericSpecimen/crawl-scripts/blob/master/results/jan_2019/parse_html/parse_html/spiders/parse_results.py) in the [jan_2019/parse_html/parse_html/spiders](https://github.com/genericSpecimen/crawl-scripts/tree/master/results/jan_2019/parse_html/parse_html/spiders) folder and writes the required data into a data.csv file.

### License
Do whatever you want to do with this.
