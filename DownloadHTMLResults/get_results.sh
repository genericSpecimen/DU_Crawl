#!/bin/bash
for i in {17058570001..17058570002}; do
	echo "Welcome $i, please wait while I try to fetch your result."
	scrapy runspider --nolog get_html.py -a roll_number=$i

done

mkdir Downloaded && mv result_* ./Downloaded
echo "Find results in the "Downloaded" folder"
