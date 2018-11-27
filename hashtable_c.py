# Coltin Lappin-Lux
# lux.coltin@gmail.com
# 10/28/2018

#-----------------------------------------------------------------------------
# HashTable
#-----------------------------------------------------------------------------

class hashtable:
	#-----------------------------------------------------------------------------
	# Initial Constructor
	#-----------------------------------------------------------------------------
	def __init__(self,size):
		self.size = size
		self.slots = [None] * self.size
		self.data = [None] * self.size

	#-----------------------------------------------------------------------------
	# Set Methods
	#-----------------------------------------------------------------------------

	def __setitem__(self,key,data):
		self.insert(key,data)

	def insert(self,key,data):
		hashvalue = self.hashfunction(key,len(self.slots))

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		#Collision
		else:
			if self.slots[hashvalue] == key:
				self.data[hashvalue] = data #replace
			else:
				#Rehash
				nextslot = self.rehashfunction(hashvalue,len(self.slots))
				while self.slots[nextslot] != None and self.slots[nextslot] != key:
					nextslot = self.rehash(nextslot,len(self.slots))

				if self.slots[nextslot] == None:
					self.slots[nextslot] = key
					self.data[nextslot] = data
				else:
					if self.slots[nextslot] == key:
						self.data[nextslot] = data #replace

	#-----------------------------------------------------------------------------
	# Hashing Functions
	#-----------------------------------------------------------------------------

	def hashfunction(self,key,size):
		return key % size

	def rehashfunction(self,oldHashValue,size):
		return (oldHashValue+1) % size

	#-----------------------------------------------------------------------------
	# Get Methods
	#-----------------------------------------------------------------------------

	def __getitem__(self,key):
		return self.getData(key)

	def getData(self,key):
		startSlot = self.hashfunction(key,len(self.slots))

		data = None
		stop = False
		found = False
		position = startSlot

		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position = self.rehashfunction(position, len(self.slots))
				if position == startSlot:
					stop = True
		return data

	def search(self,data):
		key = None
		stop = False
		found = False
		position = 0

		while not found and not stop:
			if self.data[position] == data:
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
				print self.data[i]
		print('\n')

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

	myHashtable.insert(key = ord(words[0][0]), data = words[0])
	myHashtable.printHashTable() #if collision and same key, replace data

	key = myHashtable.search('Android')
	print(key) #None ... Android has been replaced
	key = myHashtable.search('Apple')
	print(key) #key = 65
	data = myHashtable.getData(key)
	print(data) #data = Apple for key = 65

if __name__ == "__main__":
	main()