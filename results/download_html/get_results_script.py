import os
import shutil
import glob
import time
start = time.time()
for i in range(18058570001, 18058570052):
	print("Welcome {}, please wait while I try to fetch your result.".format(i))
	os.system("scrapy runspider get_html.py -a roll_number={}".format(i))
	time.sleep(5)

if not os.path.isdir("Download"):
	os.mkdir("Download")

files = glob.glob("result_*")
for file in files:
	shutil.move(file, "Download/{}".format(file))
end = time.time()
print("The generated results are in the 'Download' folder.\nTotal time elapsed in execution: {} seconds.\nThank you for using this utility.".format(end-start))
