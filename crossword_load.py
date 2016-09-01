from bs4 import BeautifulSoup 
import pandas, os

years = [2015,2016]
for year in years[:1]:
	puzzles_list = os.listdir(str(year))
	for puzzle in puzzles_list[:1]:
		puzzle_text = open(str(year)+"/"+puzzle,"r").read()
		puzzle_soup = BeautifulSoup(puzzle_text, "lxml")
		grid = puzzle_soup.findAll("grid")[0]
		print grid.findAll("row")[0].contents[0]

