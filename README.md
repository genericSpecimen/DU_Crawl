# DU_Crawl
A simple crawler for a college website.

### Dependencies
1. [python](https://www.python.org/)
2. [scrapy](https://scrapy.org/)

### Understanding the code

1. The [DownloadHTMLResults](https://github.com/genericSpecimen/DU_Crawl/tree/master/DownloadHTMLResults) folder contains the script to fetch the results. The script [get_results_script.py](https://github.com/genericSpecimen/DU_Crawl/blob/master/DownloadHTMLResults/get_results_script.py) executes the script [get_html.py](https://github.com/genericSpecimen/DU_Crawl/blob/master/DownloadHTMLResults/get_html.py) for each of the roll numbers 17058570001 to 17058570052. The generated .html files are then automatically moved into the folder [Download](https://github.com/genericSpecimen/DU_Crawl/tree/master/DownloadHTMLResults/Download).
Note that the images required by these .html files are stored in the folder [Images](https://github.com/genericSpecimen/DU_Crawl/tree/master/DownloadHTMLResults/Images) which were manually downloaded. The Images folder must be placed in a directory above the generated .html files. This is already done. If the directory struture breaks, the .html files if opened in a browser, won't display the images. The Images don't affect the ability to scrape data from these files, as we are only interested in the text.
Here is a sample output for the first four roll numbers.
![.html files](https://github.com/genericSpecimen/DU_Crawl/blob/master/savehtml.PNG)

2. The [ParseHTMLResult](https://github.com/genericSpecimen/DU_Crawl/tree/master/ParseHTMLResult) folder contains the code for scraping the data in our previously downloaded .html files. The script [parse_results_scripts.py](https://github.com/genericSpecimen/DU_Crawl/blob/master/ParseHTMLResult/parse_results_script.py) executes the script [parse_results.py](https://github.com/genericSpecimen/DU_Crawl/tree/master/ParseHTMLResult/ParseHTMLResult/spiders) in the [ParseHTMLResult/spiders](https://github.com/genericSpecimen/DU_Crawl/tree/master/ParseHTMLResult/ParseHTMLResult/spiders) folder and writes the required data into a data.csv file.

### Usage
1. To fetch the .html files, run ```python get_results_script.py```. The website is often down and our [get_results_script.py](https://github.com/genericSpecimen/DU_Crawl/blob/master/DownloadHTMLResults/get_results_script.py) script will fail to generate the .html files, which is why there's a folder [Downloaded](https://github.com/genericSpecimen/DU_Crawl/tree/master/DownloadHTMLResults/Downloaded) that contains pre-downloaded .html files.
2. Before running the scraper [parse_results_script.py](https://github.com/genericSpecimen/DU_Crawl/blob/master/ParseHTMLResult/parse_results_script.py), we need to modify a line in [parse_results.py](https://github.com/genericSpecimen/DU_Crawl/blob/master/ParseHTMLResult/ParseHTMLResult/spiders/parse_results.py). We will specify the location of these .html files in the [6th line](https://github.com/genericSpecimen/DU_Crawl/blob/3c2ce47ae48deca10790498b2406cae1f8207ec5/ParseHTMLResult/ParseHTMLResult/spiders/parse_results.py#L6).
```
	start_urls = ['file:///home/hooman/Documents/dev/test/DownloadHTMLResults/Downloaded/result_' + str(x) + '.html' for x in range(17058570001, 17058570053)]'
```
If you're unsure about the path, simply open any of the .html files in your browser and copy and paste the url in a way that the roll numbers and .html is not in the link, as they are automatically added by + 'str(x)' and + '.html'.
3. You can now run [parse_results_script.py](https://github.com/genericSpecimen/DU_Crawl/blob/master/ParseHTMLResult/parse_results_script.py) and data.csv file will be generated. 

### License
Do whatever you want to do with this.
