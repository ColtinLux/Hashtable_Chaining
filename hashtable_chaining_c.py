# Coltin Lappin-Lux
# lux.coltin@gmail.com
# 10/28/2018

#-----------------------------------------------------------------------------
# Import Linked List and Node Classes
#-----------------------------------------------------------------------------

from linkedlist_c.py import *

#-----------------------------------------------------------------------------
# Chained Hash Table Class to inherate Hash Table Class
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main Function
#-----------------------------------------------------------------------------

def main():
	"""
	This function executes when this file is run as a script.
	"""
	myHashtable = hashtable(size = 256)

	words = ["Apple", "Bar", "Candy", "Dog", "Android"]

	for i in words:
		#key = first letter of word
		myHashtable.insert(key = ord(i[0]), data = i)
	myHashtable.printHashTable()

	key = myHashtable.search('Android')
	print(key) #None ... Android has been replaced
	key = myHashtable.search('Apple')
	print(key) #key = 65
	data = myHashtable.getData(key)
	print(data) #data = Apple for key = 65

if __name__ == "__main__":
	main()