# Coltin Lappin-Lux
# lux.coltin@gmail.com
# 10/28/2018

#-----------------------------------------------------------------------------
# Import Linked List and Node Classes
#-----------------------------------------------------------------------------

from linkedlist_c import *

#-----------------------------------------------------------------------------
# Chained Hash Table Class to inherate Hash Table Class
#-----------------------------------------------------------------------------

from hashtable_c import *

class chained_hashtable(hashtable):
	#-----------------------------------------------------------------------------
	# Initial Constructor
	#-----------------------------------------------------------------------------
	def __init__(self,size):
		hashtable.__init__(self,size)

	def put(self,key,data):
		hashvalue = self.hashfunction(key,len(self.slots))

		if self.slots[hashvalue] == None:
			myLinkedList = linkedList()
			myLinkedList.insert(data)
			self.slots[hashvalue] = key
			self.data[hashvalue] = myLinkedList
		else:
			if self.slots[hashvalue] != None:
				self.data[hashvalue].insert(data)

	def hashfunction(self,key,size):
		return key%size

	def get(self,key):
		startslot = self.hashfunction(key,len(self.slots))

		data = None
		stop = False
		found = False
		position = startslot
		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
				if data != None:
					data = self.data[position].getOrderedList()
					#print(data)
			if position == startslot:
				stop = True
		return data

	def searchChain(self,data):
		key = None
		stop = False
		found = False
		position = 0

		while not found and not stop:
			if self.data[position] != None and self.data[position].search(data) == True:
				found = True
				key = self.slots[position]
			else:
				position = self.rehashfunction(position, len(self.slots))
				if position == 0:
					stop = True

		return key

	def printHashTable(self):
		print("Hash Table Data: ")
		for i in self.slots:
			if i != None:
				self.data[i].printLinkedList()
		print('\n')

#-----------------------------------------------------------------------------
# Main Function
#-----------------------------------------------------------------------------

def main():
	"""
	This function executes when this file is run as a script.
	"""
	myHashtable = chained_hashtable(size = 256)

	words = ["Apple", "Bar", "Candy", "Dog", "Android"]

	for i in words:
		#key = first letter of word
		myHashtable.put(key = ord(i[0]), data = i)
	myHashtable.printHashTable()

	print("Finding Keys:")
	key = myHashtable.searchChain("Apple")
	print(key)
	key = myHashtable.searchChain("Android")
	print(key)
	key = myHashtable.searchChain("Candy")
	print(key)

if __name__ == "__main__":
	main()