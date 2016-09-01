from bs4 import BeautifulSoup 
import pandas, os, re
#pip install BeautifulSoup4
#pip install lxml
years = [2015,2016]
for year in years[:1]:
	puzzles_list = os.listdir(str(year))
	for puzzle in puzzles_list[:1]:
		puzzle_text = open(str(year)+"/"+puzzle,"r").read()
		puzzle_soup = BeautifulSoup(puzzle_text, "lxml")#parser of choice
		#metadata collecting
		size = puzzle_soup.findAll("size")[0]
		row_length = size.findAll("rows")[0].contents[0]
		col_length = size.findAll("cols")[0].contents[0]
		header_str = puzzle_soup.findAll("title")[0].contents[0]
		day = re.search("NY Times, (.*?),",header_str).group(1)
		author = puzzle_soup.findAll("author")[0].contents[0]

		print(day)
		print(puzzle)
		print(row_length)
		print(col_length)
		#what are our words
		clues = puzzle_soup.find("clues").findChildren()
		word_hint_dict = {}
		for clue in clues:
			print clue.contents[0]
			print clue.attrs["ans"]
			word_hint_dict[clue.attrs["ans"]] = clue.contents[0]

		grid = puzzle_soup.findAll("grid")[0]
		for row in grid.findAll("row"):
			row.contents[0]#returns the data between the <row> tags

