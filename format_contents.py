import sys

def split_lines_without_space(file):
    splitted_lines_list = [line.split(' ', 1) for line in file if line.strip()]
    return splitted_lines_list

def Set_symbols():
   i=0
   asterisk_count = 0
   sub_asterisk_count = 0
   opened_file = open('input.txt')
   splitted_list = split_lines_without_space(opened_file)
   for i in len(splitted_list):
 	if splitted_list[i][0].count('*') == 1:
 	    asterisk_count += 1
	    splitted_list[i][0] = asterisk_count
	elif splitted_list[i][0].count('*') > 1:
	    sub_asterisk_count = splitted_list[i][0].count('*') - 1
	    asterisk_count = str(asterisk_count) + ".1" * sub_asterisk_count


if __name__ == "__main__":
    set_symbols()    
