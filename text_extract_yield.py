#!/usr/bin/env python
# coding:utf-8

def keyword_replace():
	f = open("test.txt")
	line = f.readline()
	while line:
		yield line
		line = f.readline()
	f.close()
	yield None

res = ""
txt = keyword_replace()
line = txt.next()
while line:
#	__import__('pdb').set_trace()
	if len(line.strip()) > 0:
		res = res + '|' + line.strip()
	line = txt.next()
res = res[1:]
print res

def simple_extract():
	lists = (line.strip() for line in open("test.txt") if line.strip())
	res = '|'.join(list(lists))
