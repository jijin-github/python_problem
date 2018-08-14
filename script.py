#!/usr/local/bin/python
import sys
import re

def main():
	star_count = 0
	sub_star_count = 0
	details = {}
	counter = 0
	sub_count = 0
	for line in sys.stdin:		
		if bool(line.strip()):
			line_content = line.rstrip("\n")
			line_details = {}
			if "*" in line_content:			
				sub_count = 0
				if line_content.count('*') == 1:					
					star_count += 1
					star_str = str(star_count)
					line_content = line_content.replace("*", star_str)
				elif line_content.count('*') > 1:
					if sub_star_count < line_content.count('*') - 1:
						sub_star_count = line_content.count('*') - 1
						star_str = str(star_count)+".1"*sub_star_count
					else:
						sub_star_count = line_content.count('*')
						star_str = str(star_count)+".2"+".1"*(sub_star_count-2)	
					line_content = line_content.replace("*"*line_content.count('*'), star_str)
				counter += 1
				line_details['item_symbol'] = star_str
				line_details['item_content'] = line_content
				details[counter] = line_details
			else:
				sub_count += 1
				if 'sub_items' in details[counter]:
					details[counter]['sub_items'][sub_count] = [line_content.count('.'), line_content]
				else:
					details[counter]['sub_items'] = {sub_count:[line_content.count('.'), line_content]}

	for key in details:
		print details[key]['item_content']
		if 'sub_items' in details[key]:
			full_text = None
			for sub_key in details[key]['sub_items']:
				replace_symbol = '-'
				next_count = None
				curr_count = details[key]['sub_items'][sub_key][0]
				if curr_count == 0:
					continue 			
				if sub_key+1 in details[key]['sub_items']:		
					next_count = details[key]['sub_items'][sub_key+1][0]
				if curr_count < next_count or next_count== 0:
					replace_symbol = '+'
				text = details[key]['sub_items'][sub_key][1].replace('.'*curr_count, replace_symbol)
				if next_count == 0:		
					print ' '*curr_count+text+" "+details[key]['sub_items'][sub_key+1][1]+" "+details[key]['sub_items'][sub_key+2][1]
				else:
					print ' '*curr_count+text

if __name__ == "__main__":
    main()