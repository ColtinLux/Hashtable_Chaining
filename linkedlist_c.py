#Coltin Lappin-Lux
#lux.coltin@gmail.com
#10-29-2018

#-----------------------------------------------------------------------------
# node Class
#-----------------------------------------------------------------------------

class node:
    #-----------------------------------------------------------------------------
    # Initial Constructor
    #-----------------------------------------------------------------------------
    def __init__(self, initData):
        self.data = initData
        self.next_pointer = None

    #-----------------------------------------------------------------------------
    # Set Methods
    #-----------------------------------------------------------------------------
    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next_pointer = newnext

    #-----------------------------------------------------------------------------
    # Get Methods
    #-----------------------------------------------------------------------------
    def getData(self):
        return self.data

    def getNext(self):
        return self.next_pointer

#-----------------------------------------------------------------------------
# linkedList Class
#-----------------------------------------------------------------------------

class linkedList:
    #-----------------------------------------------------------------------------
    # Initial Constructor
    #-----------------------------------------------------------------------------
    def __init__(self):
        self.head = None

    #-----------------------------------------------------------------------------
    # Set Method
    #-----------------------------------------------------------------------------
    def insert(self,new_data):
        current_node = self.head
        previous = None
        stop = False

        #loop until data in current position is greater than new_data (sorting in order)
        while current_node != None and not stop:
            if current_node.getData() > new_data:
                stop = True
            else:
                previous = current_node
                current_node = current_node.getNext()

        #add new node
        temp = node(new_data)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current_node)
            previous.setNext(temp)

    def remove(self,remove_data):
        current_node = self.head
        stop = False
        previous = None

        while current_node.data != remove_data and not stop:
            if current_node.getNext == None:
                stop == True
            else:
                previous = current_node
                current_node = current_node.getNext()

        if previous == None:
            self.head = current_node.getNext()
        else:
            previous.setNext(current_node.getNext())

    #-----------------------------------------------------------------------------
    # Get Method
    #-----------------------------------------------------------------------------
    def search(self,search_data):
        current_node = self.head
        found = False
        stop = False

        while current_node != None and not found and not stop:
            if current_node.getData() == search_data:
                found = True
            else:
                if current_node.getData() > search_data:
                    stop = True
                else:
                    current_node = current_node.getNext()

        return found

    #-----------------------------------------------------------------------------
    # additional Methods
    #-----------------------------------------------------------------------------
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
    
    def printLinkedList(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            print(current.getData())
            current = current.getNext()

#-----------------------------------------------------------------------------
# Main method
#-----------------------------------------------------------------------------

def main():
    """
    This function executes when this file is run as a script.
    """

    myLinkedList = linkedList()

    myLinkedList.insert("Apple")
    myLinkedList.insert("Bar")
    myLinkedList.insert("Computer Science")

    print(myLinkedList.search("Bar"))
    myLinkedList.printLinkedList()

    myLinkedList.remove("Apple")

    print(myLinkedList.search(""))
    myLinkedList.printLinkedList()

if __name__ == "__main__":
    main()