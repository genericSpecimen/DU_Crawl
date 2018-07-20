# DU_Crawl
A simple crawler for a college website.

### Dependencies
1. [python](https://www.python.org/)
2. [scrapy](https://scrapy.org/)

### Understanding the code

1. The [DownloadHTMLResults](https://github.com/genericSpecimen/DU_Crawl/tree/master/DownloadHTMLResults) folder contains the script to fetch the results. The script [get_results_script.py](https://github.com/genericSpecimen/DU_Crawl/blob/master/DownloadHTMLResults/get_results_script.py) executes the script [get_html.py](https://github.com/genericSpecimen/DU_Crawl/blob/master/DownloadHTMLResults/get_html.py) for each of the roll numbers 17058570001 to 17058570052. The generated .html files are then automatically moved into the folder [Download](https://github.com/genericSpecimen/DU_Crawl/tree/master/DownloadHTMLResults/Download).
Note that the images required by these .html files are stored in the folder [Images](https://github.com/genericSpecimen/DU_Crawl/tree/master/DownloadHTMLResults/Images) which were manually downloaded. The Images folder must be placed in a directory above the generated .html files. This is already done. If the directory struture breaks, the .html files won't display the images. The Images don't affect the ability to scrape data from these files, as we are only interested in the text.
Here is a sample output for the first four roll numbers.
![.html files](https://github.com/genericSpecimen/DU_Crawl/blob/master/savehtml.PNG)
