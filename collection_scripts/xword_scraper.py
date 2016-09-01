#tm 9/1/2016
#Q n D scraper
import urllib2, re, os
if(not(os.path.isdir("2015"))):
	os.mkdir("2015")
if(not(os.path.isdir("2016"))):
	os.mkdir("2016")
years = [2016]
base_url = "http://www.xwordinfo.com"
for year in years:
	year_url = "http://www.xwordinfo.com/xml/Puzzles/"+ str(year)
	response = urllib2.urlopen(year_url)
	resp_string = response.read()
	puzzle_urls = re.findall('HREF="(.*?)">', resp_string)
	for puzzle in puzzle_urls[1:]:#first url is a reference back to the root directory
		out_name = re.search(str(year)+"\/(.*?)\.xml", puzzle).group(1)
		puz_url = base_url + puzzle
		response = urllib2.urlopen(puz_url)
		resp_string = response.read()
		outfile = open(str(year)+"/"+out_name+".xml","w")
		outfile.write(resp_string)
		outfile.close()