#!/usr/bin/python2.7

Dictionary = {'AFAIK':'As Far As I Know', 'AFK':'Away From Keyboard', 'OMG':'Oh My Gosh', 'IMPOV':'In my point of view'}

def expand():
	raw_data = raw_input()
	for word in Dictionary:
		if raw_data.find(word) != -1:
			raw_data = raw_data.replace(word,Dictionary[word])
	print raw_data

expand()
