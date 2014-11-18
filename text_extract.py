#!/usr/bin/env python
# coding: utf-8
# author: yu
# create_at: 2014-9-16
# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=4:

"""
	读取有引号内容文本处理处理
"""
def extract1():
	lists = (line.strip() for line in open("text_extract") if line.strip()) # 生成器表达式
	file_list = []

	for line in lists:
		fields_line = quote_split(line)
		file_list.append(fields_line)

def quote_split(line):
	'''
	>>> quote_split('112 "a" "" "a b" " x "')
	['112', 'a', '', 'a b', ' x ']
	>>> quote_split('" x" "x " " x " "" " " "   "')
	[' x', 'x ', ' x ', '', ' ', '   ']
	'''

	str_list = line.split('"')
	fields_line = []
	for i in range(len(str_list)):
		if i%2 == 0:
			fields_line.extend(str_list[i].split())
		else:
			fields_line.append(str_list[i])
	return fields_line

def extract2():
	lists = [reduce(lambda x,y:x.extend(y) or x,[[strs.split('"')[i].strip()] if i%2 else [fields.strip() \
		for fields in strs.split('"')[i] if fields.strip()] for i in range(len(strs.split('"')))]) for strs in open("text_extract")]

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	extract2()
	#extract1()


