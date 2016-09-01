from bs4 import BeautifulSoup 
import pandas, os

years = [2015,2016]
for year in years[:1]:
	puzzles_list = os.listdir(str(year))
	for puzzle in puzzles_list[:1]:
		puzzle_text = open(str(year)+"/"+puzzle,"r").read()
		puzzle_soup = BeautifulSoup(puzzle_text, "lxml")
		print puzzle_soup
