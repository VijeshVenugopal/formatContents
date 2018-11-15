#!/usr/local/bin/python
import sys
import re

def format_contents():
	asterisk_count = 0
	sub_asterisk_count = 0
	result = {}
	counter = 0
	sub_count = 0
	for line in sys.stdin:		
		if bool(line.strip()):
			line_content = line.rstrip("\n")
			line_details = {}
			if "*" in line_content:			
				sub_count = 0
				if line_content.count('*') == 1:					
					asterisk_count += 1
					star_str = str(asterisk_count)
					line_content = line_content.replace("*", star_str)
				elif line_content.count('*') > 1:
					if sub_asterisk_count < line_content.count('*') - 1:
						sub_asterisk_count = line_content.count('*') - 1
						star_str = str(asterisk_count)+".1"*sub_asterisk_count
					else:
						sub_asterisk_count = line_content.count('*')
						star_str = str(asterisk_count)+".2"+".1"*(sub_asterisk_count-2)	
					line_content = line_content.replace("*"*line_content.count('*'), star_str)
				counter += 1
				line_details['item_symbol'] = star_str
				line_details['item_content'] = line_content
				result[counter] = line_details
			else:
				sub_count += 1
				if 'leafs' in result[counter]:
					result[counter]['leafs'][sub_count] = [line_content.count('.'), line_content]
				else:
					result[counter]['leafs'] = {sub_count:[line_content.count('.'), line_content]}

	for key in result:
		print result[key]['item_content']
		if 'leafs' in result[key]:
			full_text = None
			for sub_key in result[key]['leafs']:
				replace_symbol = '-'
				next_count = None
				curr_count = result[key]['leafs'][sub_key][0]
				if curr_count == 0:
					continue 			
				if sub_key+1 in result[key]['leafs']:		
					next_count = result[key]['leafs'][sub_key+1][0]
				if curr_count < next_count or next_count== 0:
					replace_symbol = '+'
				text = result[key]['leafs'][sub_key][1].replace('.'*curr_count, replace_symbol)
				if next_count == 0:
					spaces = ' '*curr_count 	
					print spaces+text+"\n  "+spaces+result[key]['leafs'][sub_key+1][1]+"\n  "+spaces+result[key]['leafs'][sub_key+2][1]
				else:
					print ' '*curr_count+text


if __name__ == "__main__":
    format_contents()
